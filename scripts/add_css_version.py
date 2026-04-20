# -*- coding: utf-8 -*-
"""Add version to CSS links to force cache refresh"""
import os
import re
from datetime import datetime

css_path = r'd:\网站开发-json\css\styles.css'
mtime = os.path.getmtime(css_path)
version = datetime.fromtimestamp(mtime).strftime('%Y%m%d%H%M')

print(f'CSS Version: {version}')

# Update blog articles
blog_dir = r'd:\网站开发-json\pages\blog'
updated = 0

for f in os.listdir(blog_dir):
    if f.endswith('.html') and f != 'index.html':
        fpath = os.path.join(blog_dir, f)
        with open(fpath, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Check if already has version
        if 'styles.css?v=' in content:
            continue
        
        # Update CSS link
        new_content = re.sub(
            r'href="(../../)?css/styles\.css"',
            f'href="../../css/styles.css?v={version}"',
            content
        )
        
        if new_content != content:
            with open(fpath, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f'Updated: {f}')
            updated += 1

print(f'Total updated: {updated}')
