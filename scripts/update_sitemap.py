#!/usr/bin/env python3
"""Update sitemap.xml to add timestamp-converter.html"""
import os

sitemap = r'd:\网站开发-json\sitemap.xml'
with open(sitemap, 'r', encoding='utf-8') as f:
    content = f.read()

# Check if already has timestamp-converter
if 'timestamp-converter' in content:
    print('sitemap.xml already has timestamp-converter')
else:
    # Add after pdf-split.html
    old = '<loc>https://www.aijsons.com/pages/pdf-split.html</loc>'
    new = old + '\n    <loc>https://www.aijsons.com/pages/timestamp-converter.html</loc>'
    content = content.replace(old, new)

    with open(sitemap, 'w', encoding='utf-8') as f:
        f.write(content)
    print('sitemap.xml updated')

# Update URL count
import re
urls = re.findall(r'<loc>.*?</loc>', content)
print(f'Total URLs: {len(urls)}')
