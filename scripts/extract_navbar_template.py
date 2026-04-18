#!/usr/bin/env python3
"""Extract navbar template from root index.html"""
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'd:\网站开发-json\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the navbar
nav_match = re.search(r'(<nav[^>]*class="navbar[^"]*"[^>]*>)(.*?)(</nav>)', content, re.DOTALL)
if nav_match:
    navbar_start = nav_match.group(1)
    navbar_content = nav_match.group(2)
    navbar_end = nav_match.group(3)
    
    print("=== NAVBAR START ===")
    print(navbar_start)
    print()
    print("=== NAVBAR END ===")
    print(navbar_end)
    print()
    print("=== NAVBAR CONTENT (first 3000 chars) ===")
    print(navbar_content[:3000])
