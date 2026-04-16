#!/usr/bin/env python3
import os
import re

BASE_DIR = r'd:\网站开发-json\pages'
P1_TOOLS = ['regex-tester.html', 'base64.html', 'url-encoder.html', 'jwt-decoder.html', 'hash-generator.html', 'uuid-generator.html']

# Check tool pages specifically
tool_pages = ['hash-generator.html', 'jwt-decoder.html', 'uuid-generator.html']

print('Checking tool pages for all P1 tool links:')
print('=' * 60)

for tool_page in tool_pages:
    fp = os.path.join(BASE_DIR, tool_page)
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print(f'\n{tool_page}:')
    for tool in P1_TOOLS:
        # Check in nav-dropdown-menu section
        idx = content.find('nav-dropdown-menu')
        if idx >= 0:
            menu = content[idx:idx+5000]
            if f'href="{tool}"' in menu:
                print(f'  [OK] {tool}')
            else:
                print(f'  [MISSING] {tool}')
        else:
            print(f'  [ERROR] No nav-dropdown-menu found')
            break
