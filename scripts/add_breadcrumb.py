#!/usr/bin/env python3
"""
Add BreadcrumbList structured data to all tool pages.
"""
import os
import re

# Define pages and their names for breadcrumb
PAGES = {
    'format.html': 'Format',
    'escape.html': 'Escape',
    'extract.html': 'Extract',
    'sort.html': 'Sort',
    'clean.html': 'Clean',
    'xml.html': 'XML',
    'yaml.html': 'YAML',
    'viewer.html': 'Viewer',
    'json2csv.html': 'JSON to CSV',
    'compare.html': 'Compare',
    'regex-tester.html': 'Regex Tester',
    'base64.html': 'Base64',
    'url-encoder.html': 'URL Encoder',
    'csv-to-excel.html': 'CSV to Excel',
    'excel-remove-duplicates.html': 'Remove Duplicates',
    'merge-csv.html': 'Merge CSV',
    'batch-file-renamer.html': 'Batch Rename',
    'pdf-split.html': 'PDF Split',
    'timestamp-converter.html': 'Timestamp',
    'css-minifier.html': 'CSS Minifier',
    'html-encoder.html': 'HTML Encoder',
    'jwt-decoder.html': 'JWT Decoder',
    'hash-generator.html': 'Hash Generator',
    'uuid-generator.html': 'UUID Generator',
    'blog.html': 'Blog',
    'news.html': 'News',
    'best-practices.html': 'Best Practices',
    'about.html': 'About',
    'changelog.html': 'Changelog',
}

# BreadcrumbList JSON-LD template
BREADCRUMB_JSON_LD = '''<!-- BreadcrumbList -->
<script type="application/ld+json">
{{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
        {{
            "@type": "ListItem",
            "position": 1,
            "name": "Home",
            "item": "https://www.aijsons.com/"
        }},
        {{
            "@type": "ListItem",
            "position": 2,
            "name": "{page_name}",
            "item": "https://www.aijsons.com/pages/{page_url}"
        }}
    ]
}}
</script>
'''

def add_breadcrumb_to_file(filepath, page_name, page_url):
    """Add BreadcrumbList JSON-LD to a file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if BreadcrumbList already exists
    if 'BreadcrumbList' in content:
        print(f"  [SKIP] {filepath} - Already has BreadcrumbList")
        return False
    
    # Find the closing </head> tag and insert before it
    breadcrumb_json = BREADCRUMB_JSON_LD.format(page_name=page_name, page_url=page_url)
    
    # Try to insert before the first </head>
    if '</head>' in content:
        content = content.replace('</head>', breadcrumb_json + '\n</head>', 1)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  [OK] Added BreadcrumbList to {filepath}")
        return True
    else:
        print(f"  [ERROR] {filepath} - No </head> tag found")
        return False

def main():
    pages_dir = os.path.join(os.path.dirname(__file__), '..', 'pages')
    pages_dir = os.path.abspath(pages_dir)
    
    print("Adding BreadcrumbList to tool pages...")
    
    updated = 0
    for page_file, page_name in PAGES.items():
        filepath = os.path.join(pages_dir, page_file)
        if os.path.exists(filepath):
            if add_breadcrumb_to_file(filepath, page_name, page_file):
                updated += 1
        else:
            print(f"  [SKIP] {page_file} - File not found")
    
    print(f"\nDone! Updated {updated} files.")

if __name__ == '__main__':
    main()
