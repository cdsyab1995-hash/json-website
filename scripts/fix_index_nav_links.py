#!/usr/bin/env python3
"""Fix index.html nav links: add pages/ prefix to all tool page links"""

import re

index_path = r"d:\网站开发-json\index.html"

# All tool/content pages that live in pages/
PAGES = [
    "format.html", "escape.html", "extract.html", "sort.html", "clean.html",
    "xml.html", "yaml.html", "viewer.html", "json2csv.html", "compare.html",
    "regex-tester.html", "base64.html", "url-encoder.html", "csv-to-excel.html",
    "excel-remove-duplicates.html", "merge-csv.html", "batch-file-renamer.html",
    "pdf-split.html", "timestamp-converter.html", "css-minifier.html",
    "html-encoder.html", "jwt-decoder.html", "hash-generator.html",
    "uuid-generator.html", "blog.html", "news.html", "best-practices.html",
    "about.html", "changelog.html"
]

with open(index_path, 'r', encoding='utf-8') as f:
    content = f.read()

original = content
fixed = 0

for page in PAGES:
    # Fix: href="page.html" -> href="pages/page.html"
    # But don't double-fix: skip if already pages/page.html
    pattern = r'href="(?!pages/)' + re.escape(page) + r'"'
    replacement = f'href="pages/{page}"'
    new_content = re.sub(pattern, replacement, content)
    if new_content != content:
        print(f"  Fixed: {page}")
        fixed += 1
        content = new_content

if content != original:
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"\nTotal fixed: {fixed} links in index.html")
else:
    print("No changes needed or links already correct.")
