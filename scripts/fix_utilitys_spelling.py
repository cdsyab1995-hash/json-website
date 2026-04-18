#!/usr/bin/env python3
"""
Fix utilitys -> utilities spelling error across all files
"""
import os
import glob

base_dir = "d:/网站开发-json"
files_changed = []

# Find all HTML files
for html_file in glob.glob(os.path.join(base_dir, "**/*.html"), recursive=True):
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'utilitys' in content.lower():
        new_content = content.replace('utilitys', 'utilities')
        new_content = new_content.replace('Utilitys', 'Utilities')
        new_content = new_content.replace('UTILITIES', 'UTILITIES')
        
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        files_changed.append(html_file)
        print(f"Fixed: {html_file}")

# Also check JS files
for js_file in glob.glob(os.path.join(base_dir, "**/*.js"), recursive=True):
    with open(js_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'utilitys' in content.lower():
        new_content = content.replace('utilitys', 'utilities')
        
        with open(js_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        files_changed.append(js_file)
        print(f"Fixed: {js_file}")

print(f"\nTotal files changed: {len(files_changed)}")
