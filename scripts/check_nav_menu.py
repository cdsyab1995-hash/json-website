#!/usr/bin/env python3
import re

files = ['hash-generator.html', 'jwt-decoder.html', 'uuid-generator.html']
for f in files:
    fp = f'd:\\网站开发-json\\pages\\{f}'
    with open(fp, 'r') as fin:
        content = fin.read()
    
    # Find nav-dropdown-menu
    idx = content.find('nav-dropdown-menu')
    if idx >= 0:
        menu = content[idx:idx+3000]
        # Check for self link
        if f'href="{f}"' in menu:
            print(f'{f}: Found self link in nav-dropdown-menu')
        else:
            print(f'{f}: NO self link in nav-dropdown-menu')
            # Print all links
            links = re.findall(r'href="([^"]+)"', menu)
            print(f'  Links: {links[:15]}...')
    else:
        print(f'{f}: No nav-dropdown-menu found')
