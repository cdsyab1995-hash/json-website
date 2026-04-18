#!/usr/bin/env python3
"""Final navbar check"""
import os
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

pages_dir = r'd:\网站开发-json\pages'

def get_top_nav_links(content):
    """Extract only top-level nav links, excluding dropdown menu items"""
    nav_match = re.search(r'<nav[^>]*class="navbar[^"]*"[^>]*>(.*?)</nav>', content, re.DOTALL)
    if not nav_match:
        return None
    
    nav_html = nav_match.group(1)
    
    # Remove dropdown menu content
    nav_html = re.sub(r'<div class="nav-dropdown-menu[^"]*"[^>]*>.*?</div>\s*</div>', '', nav_html, flags=re.DOTALL)
    
    links = []
    for match in re.finditer(r'<a\s[^>]*class="[^"]*nav-link[^"]*"[^>]*>(.*?)</a>', nav_html, re.DOTALL):
        text = re.sub(r'<[^>]+>', '', match.group(1)).strip()
        if text:
            links.append(text)
    
    return links

html_files = sorted([f for f in os.listdir(pages_dir) if f.endswith('.html')])

print("FINAL NAVBAR CHECK:")
print("=" * 70)

all_ok = True
for fname in html_files:
    fpath = os.path.join(pages_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    links = get_top_nav_links(content)
    
    if links is None:
        print(f"NO NAV: {fname}")
        all_ok = False
        continue
    
    # Expected
    expected = ['Home', 'Tools', 'Tutorial', 'Practices', 'News', 'About', 'Changelog', 'Try Formatter']
    # Blog pages and hash/uuid don't have Tutorial
    if 'blog' in fname.lower() or fname in ['hash-generator.html', 'uuid-generator.html']:
        expected = ['Home', 'Tools', 'Practices', 'News', 'About', 'Changelog', 'Try Formatter']
    
    status = "OK" if links == expected else "MISMATCH"
    if status != "OK":
        all_ok = False
        print(f"{fname}: {status}")
        print(f"  Got:      {links}")
        print(f"  Expected: {expected}")
    else:
        print(f"{fname}: {status}")

print("=" * 70)
print(f"All OK: {all_ok}")
