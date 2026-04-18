#!/usr/bin/env python3
"""Check navbar link order consistency across all pages"""
import os
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

pages_dir = r'd:\网站开发-json\pages'
root_dir = r'd:\网站开发-json'

def get_navbar_links(content):
    """Extract nav link hrefs and texts from navbar HTML"""
    # Find navbar
    nav_match = re.search(r'<nav[^>]*class="navbar[^"]*"[^>]*>(.*?)</nav>', content, re.DOTALL)
    if not nav_match:
        return None, None
    
    nav_html = nav_match.group(1)
    
    # Get all nav-link items (excluding dropdown menu items)
    links = []
    texts = []
    
    # Find all nav-link a tags
    for match in re.finditer(r'<a\s[^>]*class="[^"]*nav-link[^"]*"[^>]*>(.*?)</a>', nav_html, re.DOTALL):
        text = re.sub(r'<[^>]+>', '', match.group(1)).strip()
        href = re.search(r'href="([^"]*)"', match.group(0))
        if href and text:
            links.append(href.group(1))
            texts.append(text)
    
    return links, texts

def check_tutorial_dropdown(content):
    """Check if Tutorial dropdown exists"""
    if 'tutorial' in content.lower() and 'dropdown' in content.lower():
        return True
    return False

print("=" * 80)
print("Checking navbar links order (excluding dropdown items)...")
print("=" * 80)

# Standard expected order
STANDARD_LINKS = {
    'Home': '../index.html',  # or 'index.html' for root
    'Tools': '#',  # dropdown toggle
    'Tutorial': '../tutorial.html',  # or similar
}

# Check root index.html
print("\n[ROOT] index.html:")
root_index = os.path.join(root_dir, 'index.html')
with open(root_index, 'r', encoding='utf-8') as f:
    content = f.read()
links, texts = get_navbar_links(content)
print(f"  Links: {links}")
print(f"  Texts: {texts}")

# Check all pages
html_files = sorted([f for f in os.listdir(pages_dir) if f.endswith('.html')])

for fname in html_files:
    fpath = os.path.join(pages_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    links, texts = get_navbar_links(content)
    
    if texts is None:
        print(f"\n{fname}: NO NAVBAR FOUND!")
        continue
    
    # Check for key nav items
    has_home = 'Home' in texts
    has_tools = 'Tools' in texts
    has_tutorial = 'Tutorial' in texts
    has_practices = 'Practices' in texts
    has_news = 'News' in texts
    has_about = 'About' in texts
    has_changelog = 'Changelog' in texts
    
    # Check order
    issues = []
    expected = ['Home', 'Tools', 'Tutorial', 'Practices', 'News', 'About', 'Changelog']
    # Adjust for blog (no tutorial)
    if 'Blog' in fname or fname == 'blog.html':
        expected = ['Home', 'Tools', 'Practices', 'News', 'About', 'Changelog']
    
    if texts != expected:
        issues.append(f"ORDER: expected {expected}, got {texts}")
    
    # Check if all expected items present
    for item in expected:
        if item not in texts:
            issues.append(f"MISSING: {item}")
    
    status = "OK" if not issues else f"ISSUES: {'; '.join(issues)}"
    
    # Special markers
    markers = []
    if not has_tutorial:
        markers.append("(no Tutorial)")
    if 'Blog' in fname or fname == 'blog.html':
        markers.append("(blog page)")
    
    marker_str = " ".join(markers)
    print(f"\n{fname}: {status} {marker_str}")
