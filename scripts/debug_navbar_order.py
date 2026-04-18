#!/usr/bin/env python3
"""Debug: look at actual navbar structure in format.html"""
import os
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

fpath = r'd:\网站开发-json\pages\format.html'
with open(fpath, 'r', encoding='utf-8') as f:
    content = f.read()

# Find navbar
nav_match = re.search(r'<nav[^>]*class="navbar[^"]*"[^>]*>(.*?)</nav>', content, re.DOTALL)
if nav_match:
    nav_html = nav_match.group(1)
    # Remove dropdown menus
    nav_html_clean = re.sub(r'<div class="nav-dropdown-menu[^"]*"[^>]*>.*?</div>\s*</div>', '[DROPDOWN]', nav_html, flags=re.DOTALL)
    print("Nav HTML (cleaned):")
    print(nav_html_clean[:3000])
