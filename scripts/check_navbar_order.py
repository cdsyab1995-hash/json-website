#!/usr/bin/env python3
"""Check navbar item order consistency across all pages"""
import os
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

pages_dir = r'd:\网站开发-json\pages'
root_dir = r'd:\网站开发-json'

# Standard order we want
STANDARD_ORDER = ['Home', 'Tools', 'Tutorial', 'Practices', 'News', 'About', 'Changelog']

def extract_nav_items(content):
    """Extract nav items from navbar HTML"""
    # Find navbar section
    nav_match = re.search(r'<nav[^>]*class="nav"[^>]*>(.*?)</nav>', content, re.DOTALL)
    if not nav_match:
        return []
    
    nav_html = nav_match.group(1)
    
    items = []
    
    # Find dropdown (Tools)
    if 'dropdown-toggle' in nav_html and 'Tools' in nav_html:
        items.append('Tools')
    
    # Find regular nav links
    for link in re.finditer(r'<a[^>]*class="nav-link[^"]*"[^>]*>(.*?)</a>', nav_html, re.DOTALL):
        text = re.sub(r'<[^>]+>', '', link.group(1)).strip()
        if text and text not in items:
            items.append(text)
    
    return items

print("Checking navbar order consistency...\n")

# Check root index.html
root_index = os.path.join(root_dir, 'index.html')
if os.path.exists(root_index):
    with open(root_index, 'r', encoding='utf-8') as f:
        content = f.read()
    items = extract_nav_items(content)
    status = "OK" if items == STANDARD_ORDER else "MISMATCH"
    print(f"ROOT index.html: {' | '.join(items)} [{status}]")

print()

# Check all pages
html_files = sorted([f for f in os.listdir(pages_dir) if f.endswith('.html')])

for fname in html_files:
    fpath = os.path.join(pages_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    items = extract_nav_items(content)
    
    if not items:
        print(f"{fname}: NO NAV FOUND")
        continue
    
    status = "OK" if items == STANDARD_ORDER else "MISMATCH"
    print(f"{fname}: {' | '.join(items)} [{status}]")
