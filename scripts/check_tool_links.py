# -*- coding: utf-8 -*-
import os
import re

for fname in ['hash-generator.html', 'jwt-decoder.html', 'uuid-generator.html']:
    fp = rf'd:\网站开发-json\pages\{fname}'
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 找到 nav-dropdown-menu
    idx = content.find('nav-dropdown-menu')
    if idx >= 0:
        # 提取菜单内容
        menu_start = content.find('>', idx) + 1
        menu_end = content.find('</div>', menu_start)
        menu = content[menu_start:menu_end]
        
        # 提取所有链接
        links = re.findall(r'<a href="([^"]+)"[^>]*>([^<]+)', menu)
        
        print(f'\n=== {fname} ===')
        for href, text in links:
            if 'generator' in href or 'jwt' in href or 'uuid' in href or 'regex' in href:
                print(f'  {text} -> {href}')
