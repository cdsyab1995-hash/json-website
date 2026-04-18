#!/usr/bin/env python3
"""Check navbar HTML structure"""
import os
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

pages_dir = r'd:\网站开发-json\pages'

# Check a few representative pages
test_files = [
    'format.html',     # Standard tool page
    'blog.html',       # Blog page
    'best-practices.html',  # Practices page
]

for fname in test_files:
    fpath = os.path.join(pages_dir, fname)
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find nav element
        nav_match = re.search(r'<nav[^>]*>(.*?)</nav>', content, re.DOTALL)
        if nav_match:
            nav_html = nav_match.group(0)
            print(f"=== {fname} ===")
            print(nav_html[:1500])
            print()
