#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Batch fix all HTML files - remove US location restrictions
"""
import os
import glob
import re

base_dir = "d:/网站开发-json"
files_fixed = []

def fix_html_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    changes = []
    
    # 1. Replace areaServed: United States with audience
    if '"areaServed": {"@type": "Country", "name": "United States"}' in content:
        content = content.replace(
            '"areaServed": {"@type": "Country", "name": "United States"}',
            '"audience": {"@type": "Audience", "name": "Software Developers"}'
        )
        changes.append("areaServed -> audience")
    
    # 2. Remove geo.region meta tag
    content = re.sub(r'<meta name="geo\.region" content="US">\s*\n?\s*', '', content)
    content = re.sub(r'\s*<meta name="geo\.region" content="US">', '', content)
    
    # 3. Remove geo.placename meta tag
    content = re.sub(r'<meta name="geo\.placename" content="United States">\s*\n?\s*', '', content)
    content = re.sub(r'\s*<meta name="geo\.placename" content="United States">', '', content)
    
    # 4. Remove "for US Developers" variants
    replacements = [
        ('for US Developers', 'for Developers'),
        ('for US developers', 'for developers'),
        ('US Developers', 'Developers'),
        ('US developers', 'developers'),
        ('US & Canada Developers', 'Developers'),
        ('JSON Tools for US Developers', 'JSON Tools for Developers'),
    ]
    for old, new in replacements:
        if old in content:
            content = content.replace(old, new)
            changes.append(f'"{old}" -> "{new}"')
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return changes
    return []

# Fix all HTML files
for html_file in glob.glob(os.path.join(base_dir, "**/*.html"), recursive=True):
    changes = fix_html_file(html_file)
    if changes:
        rel_path = os.path.relpath(html_file, base_dir)
        files_fixed.append((rel_path, changes))

print(f"Fixed {len(files_fixed)} files:")
for filepath, changes in files_fixed:
    print(f"\n{filepath}:")
    for c in changes:
        print(f"  - {c}")
