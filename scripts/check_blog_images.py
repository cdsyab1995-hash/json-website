#!/usr/bin/env python3
"""Check blog.html images in detail"""
import os
import re

fp = r'd:\网站开发-json\pages\blog.html'
with open(fp, 'r', encoding='utf-8') as f:
    content = f.read()

images = re.findall(r'<img[^>]+>', content)

print(f'Found {len(images)} images in blog.html\n')

for i, img in enumerate(images):
    print(f'{i+1}. {img[:200]}')
    print()
