#!/usr/bin/env python3
"""Fix links to pages/index.html -> should be ../index.html"""
import os
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

pages_dir = r'd:\网站开发-json\pages'
root_dir = r'd:\网站开发-json'

def fix_links(content, fname):
    """Fix pages/index.html links"""
    changes = []
    
    # Pattern: href="pages/index.html" or href='pages/index.html'
    if 'href="pages/index.html"' in content:
        content = content.replace('href="pages/index.html"', 'href="../index.html"')
        changes.append('fixed pages/index.html -> ../index.html')
    
    if "href='pages/index.html'" in content:
        content = content.replace("href='pages/index.html'", "href='../index.html'")
        changes.append("fixed pages/index.html -> ../index.html (single quote)")
    
    return content, changes

# Fix all pages
html_files = sorted([f for f in os.listdir(pages_dir) if f.endswith('.html')])

all_changes = []
for fname in html_files:
    fpath = os.path.join(pages_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content, changes = fix_links(content, fname)
    
    if changes:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        all_changes.extend([f"{fname}: {c}" for c in changes])
        print(f"Fixed: {fname}")

# Also check root index.html
root_index = os.path.join(root_dir, 'index.html')
with open(root_index, 'r', encoding='utf-8') as f:
    content = f.read()

new_content, changes = fix_links(content, 'index.html (root)')
if changes:
    with open(root_index, 'w', encoding='utf-8') as f:
        f.write(new_content)
    all_changes.extend([f"root index.html: {c}" for c in changes])
    print(f"Fixed: root index.html")

print(f"\nTotal fixes: {len(all_changes)}")
for c in all_changes:
    print(f"  - {c}")
