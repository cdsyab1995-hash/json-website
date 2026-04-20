# -*- coding: utf-8 -*-
"""Fix blog.html article read time formatting errors."""
import re

path = r'd:\网站开发-json\pages\blog.html'

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix malformed read times like "52-10 min read" -> "5-7 min read"
replacements = [
    ('52-10 min read', '5-7 min read'),
    ('41-10 min read', '6-8 min read'),
    ('50-10 min read', '5-7 min read'),
    ('37-10 min read', '7-9 min read'),
    ('35-10 min read', '8-10 min read'),
]

count = 0
for old, new in replacements:
    if old in content:
        content = content.replace(old, new)
        count += 1
        print(f"  Fixed: '{old}' -> '{new}'")

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\n[OK] Fixed {count} read time entries in blog.html")
