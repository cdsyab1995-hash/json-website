#!/usr/bin/env python3
import re

for fname in ['about.html', 'blog.html', 'news.html']:
    fp = f'd:\\网站开发-json\\pages\\{fname}'
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print(f'\n=== {fname} ===')
    
    # Find nav-dropdown-menu
    idx = content.find('nav-dropdown-menu')
    if idx >= 0:
        menu = content[idx:idx+4000]
        links = re.findall(r'href="([^"]+)"', menu)
        print(f'Links in dropdown ({len(links)}):')
        for l in links:
            print(f'  - {l}')
    else:
        print('No nav-dropdown-menu found')
    
    # Check for specific tools
    for tool in ['compare.html', 'pdf-split.html', 'url-encoder.html', 'regex-tester.html']:
        if tool in content:
            print(f'  Found: {tool}')
        else:
            print(f'  Missing: {tool}')
