# -*- coding: utf-8 -*-
"""
aijsons.com 技术全面分析
"""
import os
import re
import json
from datetime import datetime

BASE_DIR = r'd:\网站开发-json'

def safe_read(path, encoding='utf-8'):
    """安全读取文件"""
    try:
        with open(path, 'r', encoding=encoding) as f:
            return f.read()
    except UnicodeDecodeError:
        try:
            with open(path, 'r', encoding='latin-1') as f:
                return f.read()
        except:
            return ""

def analyze_website():
    results = {'pages': {}, 'seo_elements': {}, 'performance': {}, 'files': {}}
    
    # 1. 统计页面
    pages_dir = os.path.join(BASE_DIR, 'pages')
    pages = [f for f in os.listdir(pages_dir) if f.endswith('.html')]
    results['pages']['total'] = len(pages)
    results['pages']['list'] = sorted(pages)
    
    # 2. 检查关键文件
    results['files']['sitemap'] = os.path.exists(os.path.join(BASE_DIR, 'sitemap.xml'))
    results['files']['robots'] = os.path.exists(os.path.join(BASE_DIR, 'robots.txt'))
    results['files']['og_image'] = os.path.exists(os.path.join(BASE_DIR, 'og-image.png'))
    results['files']['favicon'] = os.path.exists(os.path.join(BASE_DIR, 'images', 'favicon.ico'))
    
    # 3. robots.txt
    robots_path = os.path.join(BASE_DIR, 'robots.txt')
    if os.path.exists(robots_path):
        robots_content = safe_read(robots_path)
        results['robots_content'] = robots_content
        results['robots_issues'] = []
        if 'Google-Extended' in robots_content:
            results['robots_issues'].append('Google-Extended blocked')
        if 'User-agent: *' not in robots_content:
            results['robots_issues'].append('Missing User-agent: *')
    
    # 4. sitemap.xml
    sitemap_path = os.path.join(BASE_DIR, 'sitemap.xml')
    if os.path.exists(sitemap_path):
        sitemap_content = safe_read(sitemap_path)
        results['sitemap_urls'] = sitemap_content.count('<url>')
    
    # 5. index.html
    index_path = os.path.join(BASE_DIR, 'index.html')
    if os.path.exists(index_path):
        index_content = safe_read(index_path)
        
        results['seo_elements'] = {
            'title': bool(re.search(r'<title>', index_content)),
            'meta_description': bool(re.search(r'<meta name="description"', index_content)),
            'canonical': bool(re.search(r'<link rel="canonical"', index_content)),
            'og_tags': bool(re.search(r'<meta property="og:', index_content)),
            'twitter_card': bool(re.search(r'<meta name="twitter:', index_content)),
            'json_ld': bool(re.search(r'<script type="application/ld\+json"', index_content)),
        }
        
        results['performance'] = {
            'preconnect': 'preconnect' in index_content,
            'preload': 'preload' in index_content,
            'defer_js': 'defer' in index_content,
            'async_css': 'media="print"' in index_content or 'onload=' in index_content,
            'lazy_load': 'loading="lazy"' in index_content,
        }
    
    # 6. CSS
    css_path = os.path.join(BASE_DIR, 'css', 'styles.css')
    if os.path.exists(css_path):
        css_content = safe_read(css_path)
        results['css_size'] = len(css_content)
        results['css_lines'] = len(css_content.split('\n'))
    
    # 7. JS
    js_path = os.path.join(BASE_DIR, 'js', 'app.js')
    if os.path.exists(js_path):
        js_content = safe_read(js_path)
        results['js_size'] = len(js_content)
        results['js_lines'] = len(js_content.split('\n'))
    
    return results

def print_report(results):
    ok = "[OK]"
    fail = "[FAIL]"
    
    print("=" * 70)
    print("  aijsons.com Website Technical Analysis Report")
    print("  Generated: " + datetime.now().strftime('%Y-%m-%d %H:%M'))
    print("=" * 70)
    
    print("\n" + "-" * 70)
    print(" I. PAGE STATISTICS")
    print("-" * 70)
    print("  Total pages: %d" % results['pages']['total'])
    
    tool_pages = [p for p in results['pages']['list'] if not any(x in p for x in ['about', 'blog', 'news', 'best', 'changelog'])]
    content_pages = [p for p in results['pages']['list'] if any(x in p for x in ['about', 'blog', 'news', 'best', 'changelog'])]
    print("  Tool pages: %d" % len(tool_pages))
    print("  Content pages: %d" % len(content_pages))
    print("  File sizes:")
    print("    - CSS: %d bytes (%d lines)" % (results.get('css_size', 0), results.get('css_lines', 0)))
    print("    - JS:  %d bytes (%d lines)" % (results.get('js_size', 0), results.get('js_lines', 0)))
    
    print("\n" + "-" * 70)
    print(" II. SEO STATUS")
    print("-" * 70)
    
    seo = results.get('seo_elements', {})
    print("\n  [Implemented]")
    for item, status in seo.items():
        status_str = ok if status else fail
        print("    %s %s" % (status_str, item))
    
    sitemap_urls = results.get('sitemap_urls', 0)
    print("\n  Sitemap: %d URLs (page count: %d)" % (sitemap_urls, results['pages']['total']))
    
    if 'robots_issues' in results:
        print("\n  Robots.txt issues:")
        for issue in results['robots_issues']:
            print("    - %s" % issue)
    
    print("\n" + "-" * 70)
    print(" III. PERFORMANCE OPTIMIZATION")
    print("-" * 70)
    
    perf = results.get('performance', {})
    print("\n  [Implemented]")
    for item, status in perf.items():
        status_str = ok if status else fail
        print("    %s %s" % (status_str, item))
    
    print("\n  [Need to check]")
    print("    - Lighthouse Performance Score (target: 90+)")
    print("    - Core Web Vitals (CLS < 0.1, LCP < 2.5s)")
    print("    - TTFB (Time to First Byte)")
    print("    - Bundle size optimization")
    
    print("\n" + "-" * 70)
    print(" IV. MISSING FEATURES")
    print("-" * 70)
    
    print("\n  [Suggested Tool Pages]")
    tools = [
        ("Timestamp Converter", "Convert Unix timestamp", "P2"),
        ("HTML Encoder/Decoder", "Encode/decode HTML entities", "P2"),
        ("CSS Minifier", "Minify CSS code", "P3"),
        ("JavaScript Minifier", "Minify JS code", "P3"),
        ("Color Converter", "Color format converter", "P3"),
        ("SQL Formatter", "Format SQL queries", "P3"),
    ]
    for tool, desc, priority in tools:
        print("    [%s] %s - %s" % (priority, tool, desc))
    
    print("\n  [Missing Pages]")
    missing_pages = [
        ("Pricing", "P3"),
        ("Contact", "P3"),
        ("FAQ", "P3"),
        ("API Documentation", "P3"),
    ]
    for page, priority in missing_pages:
        print("    [%s] %s" % (priority, page))
    
    print("\n" + "-" * 70)
    print(" V. TECHNICAL ARCHITECTURE GAPS")
    print("-" * 70)
    
    gaps = [
        "No SSR (Server-Side Rendering)",
        "No CDN configuration",
        "No HTTP/2 optimization",
        "No image CDN/optimization",
        "No WebP/AVIF format",
        "No Service Worker / PWA",
        "No lazy loading for images",
    ]
    for gap in gaps:
        print("    [X] %s" % gap)
    
    print("\n" + "-" * 70)
    print(" VI. UX IMPROVEMENTS")
    print("-" * 70)
    
    ux_items = [
        "Dark mode toggle",
        "Tool usage statistics",
        "Keyboard shortcuts",
        "Related tools recommendation",
        "i18n support",
        "Browser extension",
    ]
    for item in ux_items:
        print("    [ ] %s" % item)
    
    print("\n" + "-" * 70)
    print(" VII. PRIORITY FIXES (P0-P2)")
    print("-" * 70)
    
    priority_fixes = [
        ("P0", "robots.txt", "Check AI crawler access"),
        ("P0", "sitemap.xml", "Verify all pages indexed"),
        ("P0", "Nav consistency", "All pages have same Tools menu"),
        ("P1", "Performance", "Lighthouse score 90+"),
        ("P1", "CLS fix", "Layout shift < 0.1"),
        ("P2", "New tools", "Add popular tools"),
        ("P2", "Dark mode", "User experience boost"),
    ]
    
    for priority, item, desc in priority_fixes:
        print("    [%s] %s" % (priority, item))
        print("         -> %s" % desc)
    
    print("\n" + "=" * 70)

if __name__ == '__main__':
    results = analyze_website()
    print_report(results)
