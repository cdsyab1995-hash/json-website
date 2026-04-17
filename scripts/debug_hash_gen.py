#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

# Show full content of hash-generator.html to understand structure
path = r'd:\网站开发-json\pages\hash-generator.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

print(f'File length: {len(content)}')
print(f'Has body: {"body" in content.lower()}')
print(f'Has head: {"head" in content.lower()}')

# Find all tags
import re
tags = re.findall(r'<[^>]+>', content[:2000])
print('\nFirst tags found:')
for t in tags[:20]:
    print(f'  {t}')
    
print('\nLast 500 chars:')
print(repr(content[-500:]))
