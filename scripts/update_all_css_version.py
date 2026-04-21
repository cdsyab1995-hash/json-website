# -*- coding: utf-8 -*-
"""Update CSS version in all blog articles to force cache refresh"""
import os
import re

version = '202604210832'

# Update blog articles
blog_dir = r'd:\网站开发-json\pages\blog'
for f in os.listdir(blog_dir):
    if f.endswith('.html') and f != 'index.html':
        fpath = os.path.join(blog_dir, f)
        with open(fpath, 'r', encoding='utf-8') as file:
            content = file.read()
        
        new_content = re.sub(
            r'styles\.css\?v=\d+',
            f'styles.css?v={version}',
            content
        )
        
        if new_content != content:
            with open(fpath, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f'Updated: {f}')

print(f'Version: {version}')
