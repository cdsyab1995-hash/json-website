#!/usr/bin/env python3
import os
import re

BASE_DIR = r'd:\网站开发-json\pages'
P1_TOOLS = ['regex-tester.html', 'base64.html', 'url-encoder.html', 'jwt-decoder.html', 'hash-generator.html', 'uuid-generator.html']

# Get all HTML files
files = []
for f in os.listdir(BASE_DIR):
    if f.endswith('.html'):
        files.append(os.path.join(BASE_DIR, f))

files.sort()

print('Verifying P1 tools in all pages:')
print('=' * 60)

for fp in files:
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Count P1 tools
    count = 0
    for tool in P1_TOOLS:
        if f'href="{tool}"' in content:
            count += 1
    
    fname = os.path.basename(fp)
    status = 'OK' if count == 6 else f'MISSING ({6-count})'
    print(f'{fname:35} {status}')
