#!/usr/bin/env python3
"""Check hash-generator and uuid-generator navbars"""
import sys
import re
sys.stdout.reconfigure(encoding='utf-8')

for fname in ['hash-generator.html', 'uuid-generator.html']:
    fpath = rf'd:\网站开发-json\pages\{fname}'
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print(f"=== {fname} ===")
    # Find nav
    nav_match = re.search(r'<nav[^>]*class="[^"]*"[^>]*>.*?</nav>', content, re.DOTALL)
    if nav_match:
        print("Found nav:")
        print(nav_match.group(0)[:1000])
    else:
        # Try without class
        nav_match = re.search(r'<nav[^>]*>.*?</nav>', content, re.DOTALL)
        if nav_match:
            print("Found nav (no class filter):")
            print(nav_match.group(0)[:1000])
        else:
            print("No nav found with either pattern")
    print("\n")
