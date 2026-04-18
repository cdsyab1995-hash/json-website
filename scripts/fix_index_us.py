#!/usr/bin/env python3
"""
Fix index.html - remove US restrictions without breaking the page
"""
import re

def fix_index():
    file_path = r"d:\网站开发-json\index.html"
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix 1: meta description - remove "for US developers"
    content = content.replace(
        'for US developers',
        'for developers'
    )
    
    # Fix 2: title - remove "for US Developers"
    content = content.replace(
        'for US Developers',
        'for Developers'
    )
    
    # Fix 3: areaServed: United States -> audience: Software Developers
    old_ld = '"areaServed": {"@type": "Country", "name": "United States"}'
    new_ld = '"audience": {"@type": "Audience", "name": "Software Developers"}'
    content = content.replace(old_ld, new_ld)
    
    # Fix 4: Twitter meta
    content = content.replace(
        'Debugger for US Developers',
        'Debugger for Developers'
    )
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("[DONE] Fixed index.html US restrictions")

if __name__ == "__main__":
    fix_index()
