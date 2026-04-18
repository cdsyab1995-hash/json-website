#!/usr/bin/env python3
"""Check hash-generator and uuid-generator pages - full structure"""
import sys
import re
sys.stdout.reconfigure(encoding='utf-8')

for fname in ['hash-generator.html', 'uuid-generator.html']:
    fpath = rf'd:\网站开发-json\pages\{fname}'
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print(f"=== {fname} ===")
    # Find header
    header_match = re.search(r'<header[^>]*>(.*?)</header>', content, re.DOTALL)
    if header_match:
        print("HEADER CONTENT:")
        print(header_match.group(0)[:2000])
    else:
        # Look for nav
        nav_match = re.search(r'<nav[^>]*>', content)
        if nav_match:
            print(f"Nav found at: {nav_match.start()}")
            print(content[nav_match.start():nav_match.start()+2000])
        else:
            print("No header, no nav found")
            # Look for any nav-link
            nav_links = re.findall(r'<a[^>]*class="[^"]*nav-link[^"]*"[^>]*>', content)
            print(f"Nav links found: {len(nav_links)}")
            for link in nav_links[:5]:
                print(f"  {link}")
    print("\n")
