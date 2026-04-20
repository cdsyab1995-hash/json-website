#!/usr/bin/env python3
"""
Add active class to current page nav link.
"""
import os
import re

# Define pages and their nav link patterns
PAGE_ACTIVATIONS = {
    'format.html': [
        ('href="format.html"', 'href="format.html" class="active"'),
    ],
    'escape.html': [
        ('href="escape.html"', 'href="escape.html" class="active"'),
    ],
    'extract.html': [
        ('href="extract.html"', 'href="extract.html" class="active"'),
    ],
    'sort.html': [
        ('href="sort.html"', 'href="sort.html" class="active"'),
    ],
    'clean.html': [
        ('href="clean.html"', 'href="clean.html" class="active"'),
    ],
    'xml.html': [
        ('href="xml.html"', 'href="xml.html" class="active"'),
    ],
    'yaml.html': [
        ('href="yaml.html"', 'href="yaml.html" class="active"'),
    ],
    'viewer.html': [
        ('href="viewer.html"', 'href="viewer.html" class="active"'),
    ],
    'json2csv.html': [
        ('href="json2csv.html"', 'href="json2csv.html" class="active"'),
    ],
    'compare.html': [
        ('href="compare.html"', 'href="compare.html" class="active"'),
    ],
    'regex-tester.html': [
        ('href="regex-tester.html"', 'href="regex-tester.html" class="active"'),
    ],
    'base64.html': [
        ('href="base64.html"', 'href="base64.html" class="active"'),
    ],
    'url-encoder.html': [
        ('href="url-encoder.html"', 'href="url-encoder.html" class="active"'),
    ],
    'csv-to-excel.html': [
        ('href="csv-to-excel.html"', 'href="csv-to-excel.html" class="active"'),
    ],
    'excel-remove-duplicates.html': [
        ('href="excel-remove-duplicates.html"', 'href="excel-remove-duplicates.html" class="active"'),
    ],
    'merge-csv.html': [
        ('href="merge-csv.html"', 'href="merge-csv.html" class="active"'),
    ],
    'batch-file-renamer.html': [
        ('href="batch-file-renamer.html"', 'href="batch-file-renamer.html" class="active"'),
    ],
    'pdf-split.html': [
        ('href="pdf-split.html"', 'href="pdf-split.html" class="active"'),
    ],
    'timestamp-converter.html': [
        ('href="timestamp-converter.html"', 'href="timestamp-converter.html" class="active"'),
    ],
    'css-minifier.html': [
        ('href="css-minifier.html"', 'href="css-minifier.html" class="active"'),
    ],
    'html-encoder.html': [
        ('href="html-encoder.html"', 'href="html-encoder.html" class="active"'),
    ],
    'jwt-decoder.html': [
        ('href="jwt-decoder.html"', 'href="jwt-decoder.html" class="active"'),
    ],
    'hash-generator.html': [
        ('href="hash-generator.html"', 'href="hash-generator.html" class="active"'),
    ],
    'uuid-generator.html': [
        ('href="uuid-generator.html"', 'href="uuid-generator.html" class="active"'),
    ],
    'blog.html': [
        ('href="blog.html"', 'href="blog.html" class="active"'),
    ],
    'news.html': [
        ('href="news.html"', 'href="news.html" class="active"'),
    ],
    'best-practices.html': [
        ('href="best-practices.html"', 'href="best-practices.html" class="active"'),
    ],
    'about.html': [
        ('href="about.html"', 'href="about.html" class="active"'),
    ],
    'changelog.html': [
        ('href="changelog.html"', 'href="changelog.html" class="active"'),
    ],
}

def add_active_class(filepath, activations):
    """Add active class to nav links."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    changed = False
    for old, new in activations:
        if old in content and new not in content:
            content = content.replace(old, new, 1)
            changed = True
    
    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    pages_dir = os.path.join(os.path.dirname(__file__), '..', 'pages')
    pages_dir = os.path.abspath(pages_dir)
    
    print("Adding active class to nav links...")
    
    updated = 0
    for page_file, activations in PAGE_ACTIVATIONS.items():
        filepath = os.path.join(pages_dir, page_file)
        if os.path.exists(filepath):
            if add_active_class(filepath, activations):
                print(f"  [OK] {page_file}")
                updated += 1
            else:
                print(f"  [SKIP] {page_file} - No changes needed")
        else:
            print(f"  [ERROR] {page_file} - File not found")
    
    print(f"\nDone! Updated {updated} files.")

if __name__ == '__main__':
    main()
