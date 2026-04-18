#!/usr/bin/env python3
"""
Build Long-tail Content Strategy
Optimize pages for low-competition keywords
"""

import os
import re

# Long-tail keywords to target
LONG_TAIL_KEYWORDS = {
    "json2csv.html": {
        "title": "JSON to CSV for Excel - Free Online Converter | AI JSON",
        "description": "Convert JSON to CSV for Excel in seconds. Free online tool to export JSON data to spreadsheet format. No signup required.",
        "keywords": "json to csv for excel, json to spreadsheet, json export to excel, json array to csv, convert json to spreadsheet",
        "h1": "JSON to CSV for Excel - Free Online Converter"
    },
    "compare.html": {
        "title": "JSON Compare Tool - Find Differences Between JSON Files | AI JSON",
        "description": "Compare two JSON files or documents online. Find differences instantly with our free JSON diff tool. Perfect for API versioning and debugging.",
        "keywords": "json compare tool, json diff tool, compare json files, json difference checker, json file comparison",
        "h1": "JSON Compare Tool - Find Differences Between JSON Files"
    },
    "viewer.html": {
        "title": "JSON Viewer Online - Visual JSON Tree View | AI JSON",
        "description": "View JSON data in a visual tree structure online. Expand, collapse, search, and navigate complex JSON. Free JSON viewer with syntax highlighting.",
        "keywords": "json viewer online, json tree view, json visualizer, json viewer tree, view json in browser",
        "h1": "JSON Viewer Online - Visual JSON Tree View"
    }
}

def optimize_long_tail_page(filepath, config):
    """Optimize a page for long-tail keywords"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Update <title>
    content = re.sub(
        r'<title>.*?</title>',
        f'<title>{config["title"]}</title>',
        content
    )
    
    # Update meta description
    content = re.sub(
        r'<meta name="description" content="[^"]*">',
        f'<meta name="description" content="{config["description"]}">',
        content
    )
    
    # Update keywords
    content = re.sub(
        r'<meta name="keywords" content="[^"]*">',
        f'<meta name="keywords" content="{config["keywords"]}">',
        content
    )
    
    # Update og:title
    content = re.sub(
        r'<meta property="og:title" content="[^"]*">',
        f'<meta property="og:title" content="{config["title"]}">',
        content
    )
    
    # Update og:description
    content = re.sub(
        r'<meta property="og:description" content="[^"]*">',
        f'<meta property="og:description" content="{config["description"]}">',
        content
    )
    
    # Update JSON-LD description
    content = re.sub(
        r'"description":\s*"[^"]*"',
        f'"description": "{config["description"]}"',
        content
    )
    
    # Update h1 (find the main heading)
    content = re.sub(
        r'<h1[^>]*>.*?</h1>',
        f'<h1>{config["h1"]}</h1>',
        content,
        flags=re.DOTALL
    )
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def add_long_tail_section(filepath):
    """Add long-tail keyword section to page"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '<!-- Long-tail Content -->' in content:
        return False
    
    # Find where to insert (after main tool area, before footer)
    long_tail_content = '''
    <!-- Long-tail Content Section -->
    <section class="tool-area mt-lg" style="margin-top: 2rem;">
        <h2 style="font-size: 1.5rem; margin-bottom: 1rem;">Related Searches</h2>
        <div style="display: flex; flex-wrap: wrap; gap: 0.5rem; margin-top: 1rem;">
            <a href="../pages/json2csv.html" class="nav-link" style="background: var(--bg-secondary);">JSON to CSV</a>
            <a href="../pages/format.html" class="nav-link" style="background: var(--bg-secondary);">JSON Formatter</a>
            <a href="../pages/compare.html" class="nav-link" style="background: var(--bg-secondary);">JSON Compare</a>
            <a href="../pages/viewer.html" class="nav-link" style="background: var(--bg-secondary);">JSON Viewer</a>
        </div>
    </section>
    '''
    
    # Insert before </main>
    if '</main>' in content:
        content = content.replace('</main>', long_tail_content + '\n</main>')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    pages_dir = r"d:\网站开发-json\pages"
    optimized = []
    
    print("=" * 50)
    print("Long-tail Content Optimization")
    print("=" * 50)
    
    for filename, config in LONG_TAIL_KEYWORDS.items():
        filepath = os.path.join(pages_dir, filename)
        if os.path.exists(filepath):
            if optimize_long_tail_page(filepath, config):
                optimized.append(filename)
                print(f"[OK] Optimized: {filename}")
            
            if add_long_tail_section(filepath):
                print(f"[OK] Added related searches: {filename}")
    
    print(f"\n[Summary] Optimized {len(optimized)} pages for long-tail keywords")
    print("Pages:", ", ".join(optimized))

if __name__ == "__main__":
    main()
