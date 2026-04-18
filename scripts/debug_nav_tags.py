#!/usr/bin/env python3
"""Debug nav tags in hash-generator"""
import sys
import re
sys.stdout.reconfigure(encoding='utf-8')

fpath = r'd:\网站开发-json\pages\hash-generator.html'
with open(fpath, 'r', encoding='utf-8') as f:
    content = f.read()

# Find all nav occurrences
nav_starts = [m.start() for m in re.finditer(r'<nav', content)]
nav_ends = [m.start() for m in re.finditer(r'</nav>', content)]

print(f"Nav starts: {nav_starts}")
print(f"Nav ends: {nav_ends}")

# Find what tags exist in the first 500 chars
first_500 = content[:500]
print("\nFirst 500 chars:")
print(repr(first_500))

# Find what's between <body> and <main>
body_match = re.search(r'<body[^>]*>(.*?)<main', content, re.DOTALL)
if body_match:
    print("\nBetween body and main:")
    print(repr(body_match.group(1)[:2000]))
