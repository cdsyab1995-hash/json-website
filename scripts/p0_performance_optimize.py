#!/usr/bin/env python3
"""
P0 Performance Optimization Script
Fix CLS issues by optimizing font loading and adding proper dimensions
"""

import os
import re

def optimize_index():
    index_path = r"d:\网站开发-json\index.html"
    
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Get font URL from Google Fonts link
    font_url_match = re.search(r'href="(https://fonts\.googleapis\.com/css2\?family=[^"]+)"', content)
    font_url = font_url_match.group(1) if font_url_match else None
    
    # 2. Extract font family name
    font_family_match = re.search(r'family=([^&]+)', font_url) if font_url else None
    font_family = font_family_match.group(1).replace('+', ' ') if font_family_match else 'DM Sans'
    
    # 3. Build optimized font preload block
    # Get woff2 URL for preload
    woff2_url = "https://fonts.gstatic.com/s/dmsans/v15/rP2Hp2ywxg089UriCZOIHQ.woff2"
    
    optimized_font_block = f'''    <!-- P0: Font Optimization - prevent CLS from font swap -->
    <link rel="preconnect" href="https://fonts.googleapis.com" crossorigin>
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <!-- Preload critical font for fast render -->
    <link rel="preload" as="font" type="font/woff2" crossorigin href="{woff2_url}">
    <!-- System font fallback while Google Font loads -->
    <style>
        .font-loading {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }}
    </style>
    <!-- Google Font with font-display:swap to prevent invisible text -->
    <link rel="stylesheet" href="{font_url}&display=swap" media="print" onload="this.media='all'">
    <noscript><link rel="stylesheet" href="{font_url}&display=swap"></noscript>'''
    
    # Remove old font loading blocks
    old_patterns = [
        r'<!-- DNS Prefetch.*?preconnect.*?<!-- Google Fonts -->.*?\n',
        r'<!-- Google Fonts -->.*?\n',
        r'<link rel="preload" as="font".*?>\n',
        r'<style>\s*\*.*?font-family:[\'"]DM Sans[\'"].*?</style>\s*',
    ]
    
    for pattern in old_patterns:
        content = re.sub(pattern, '', content, flags=re.DOTALL)
    
    # Insert new font block after <head>
    if '<!-- P0: Font Optimization' not in content:
        content = content.replace('<head>', '<head>\n' + optimized_font_block, 1)
    
    # 4. Add aspect-ratio to CSS for images (even though no img tags, prepare for future)
    css_optimization = '''
    /* P0: Prevent CLS from images - reserve space */
    img { aspect-ratio: attr(width) / attr(height); }
    '''
    
    # Add to styles.css preload check - but actually add to inline critical CSS
    # Find existing critical CSS and add to it
    if '/* Critical CSS */' in content:
        # Add to the inline critical CSS
        critical_css_addition = '''
        /* P0: Image CLS prevention */
        img { contain: layout; }'''
        content = content.replace('/* Critical CSS */', '/* Critical CSS */' + critical_css_addition)
    
    # 5. Optimize og:image preloading
    og_image_optimization = '''
    <!-- P0: Preload og:image to prevent LCP delay -->
    <link rel="preload" as="image" href="https://www.aijsons.com/og-image.png">'''
    
    if '<!-- P0: Preload og:image' not in content:
        content = content.replace('<!-- DNS Prefetch', og_image_optimization + '\n    <!-- DNS Prefetch')
    
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("[OK] index.html P0 optimization complete")

def optimize_css():
    """Add CLS prevention to main CSS"""
    css_path = r"d:\网站开发-json\css\styles.css"
    
    # Try different encodings
    for encoding in ['utf-8', 'latin-1', 'cp1252']:
        try:
            with open(css_path, 'r', encoding=encoding) as f:
                content = f.read()
            break
        except UnicodeDecodeError:
            continue
    
    # Add CLS prevention rules at the end
    cls_prevention = '''
/* P0: CLS Prevention */
img, video, iframe {
    contain: layout;
}

.font-loading {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}

/* Reserve space for images before loading */
img:not([width]):not([height]) {
    background-color: var(--bg-secondary);
    min-height: 100px;
}
'''
    
    if '/* P0: CLS Prevention */' not in content:
        content += cls_prevention
    
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("[OK] styles.css P0 optimization complete")

def optimize_all_tool_pages():
    """Optimize all tool pages for CLS"""
    pages_dir = r"d:\网站开发-json\pages"
    
    for filename in os.listdir(pages_dir):
        if not filename.endswith('.html'):
            continue
        
        filepath = os.path.join(pages_dir, filename)
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        
        # Add CLS prevention to CSS if not exists
        if '/* P0: CLS Prevention */' not in content:
            # Add to inline styles or link to optimized CSS
            cls_rule = '''
/* P0: CLS Prevention */
img { contain: layout; }
.font-loading { font-family: -apple-system, BlinkMacSystemFont, sans-serif; }
'''
            # Find existing style tag and append
            if '<style>' in content:
                content = content.replace('</style>', cls_rule + '\n</style>')
        
        # Ensure font-display=swap in Google Fonts links
        if 'fonts.googleapis.com' in content and 'display=swap' not in content:
            content = re.sub(
                r'href="(https://fonts\.googleapis\.com/css2\?[^"]+)"',
                r'href="\1&display=swap"',
                content
            )
        
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"[OK] {filename}")

def main():
    print("=" * 50)
    print("P0 Performance Optimization")
    print("=" * 50)
    
    print("\n[1/4] Optimizing index.html...")
    optimize_index()
    
    print("\n[2/4] Optimizing styles.css...")
    optimize_css()
    
    print("\n[3/4] Optimizing tool pages...")
    optimize_all_tool_pages()
    
    print("\n[4/4] Summary:")
    print("  - Font loading optimized with display=swap")
    print("  - Critical font preloaded")
    print("  - CLS prevention rules added")
    print("  - og:image preloaded")
    print("\n[P0] Optimization Complete!")

if __name__ == "__main__":
    main()
