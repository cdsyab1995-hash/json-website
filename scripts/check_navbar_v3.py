#!/usr/bin/env python3
"""Check actual top-level navbar links (excluding dropdown menu items)"""
import os
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

pages_dir = r'd:\网站开发-json\pages'
root_dir = r'd:\网站开发-json'

def get_top_nav_links(content):
    """Extract only top-level nav links, excluding dropdown menu items"""
    nav_match = re.search(r'<nav[^>]*class="navbar[^"]*"[^>]*>(.*?)</nav>', content, re.DOTALL)
    if not nav_match:
        return None
    
    nav_html = nav_match.group(1)
    
    # Remove dropdown menu content (everything inside nav-dropdown-menu)
    nav_html = re.sub(r'<div class="nav-dropdown-menu[^"]*"[^>]*>.*?</div>\s*</div>', '', nav_html, flags=re.DOTALL)
    
    # Now get nav-link items
    links = []
    for match in re.finditer(r'<a\s[^>]*class="[^"]*nav-link[^"]*"[^>]*>(.*?)</a>', nav_html, re.DOTALL):
        text = re.sub(r'<[^>]+>', '', match.group(1)).strip()
        href = re.search(r'href="([^"]*)"', match.group(0))
        if href and text:
            links.append(text)
    
    return links

print("=" * 80)
print("Checking TOP-LEVEL navbar links (excluding dropdown menu items)...")
print("=" * 80)

# Check root index.html
print("\n[ROOT] index.html:")
root_index = os.path.join(root_dir, 'index.html')
with open(root_index, 'r', encoding='utf-8') as f:
    content = f.read()
links = get_top_nav_links(content)
print(f"  Items: {links}")

# Check all pages
html_files = sorted([f for f in os.listdir(pages_dir) if f.endswith('.html')])

mismatches = []
no_nav = []

for fname in html_files:
    fpath = os.path.join(pages_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    links = get_top_nav_links(content)
    
    if links is None:
        no_nav.append(fname)
        print(f"\n{fname}: NO NAVBAR!")
        continue
    
    # Expected for most pages
    expected = ['Home', 'Tools', 'Tutorial', 'Practices', 'News', 'About', 'Changelog', 'Try Formatter']
    
    # Blog pages don't have Tutorial
    if 'blog' in fname.lower():
        expected = ['Home', 'Tools', 'Practices', 'News', 'About', 'Changelog', 'Try Formatter']
    
    if links != expected:
        mismatches.append((fname, links, expected))
        print(f"\n{fname}: MISMATCH")
        print(f"  Got:      {links}")
        print(f"  Expected: {expected}")

print("\n" + "=" * 80)
print(f"Summary: {len(mismatches)} pages with mismatches, {len(no_nav)} with no navbar")
print("=" * 80)
if no_nav:
    print(f"No navbar: {no_nav}")
