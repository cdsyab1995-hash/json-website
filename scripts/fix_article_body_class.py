#!/usr/bin/env python3
"""Fix article-body -> article-content class in blog posts"""

import os
import re

blog_dir = r"d:\网站开发-json\pages\blog"
count = 0

for filename in os.listdir(blog_dir):
    if not filename.endswith('.html'):
        continue
    filepath = os.path.join(blog_dir, filename)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace article-body with article-content
    new_content = content.replace('class="article-body"', 'class="article-content"')
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1
        print(f"Fixed: {filename}")

print(f"\nTotal fixed: {count} files")
