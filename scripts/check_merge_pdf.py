# -*- coding: utf-8 -*-
import os

# 检查 merge-csv.html 和 pdf-split.html 的导航栏
for fname in ['merge-csv.html', 'pdf-split.html']:
    fp = rf'd:\网站开发-json\pages\{fname}'
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print(f'\n=== {fname} ===')
    
    # 找到 nav-dropdown-menu
    idx = content.find('nav-dropdown-menu')
    if idx >= 0:
        menu_start = content.find('>', idx) + 1
        menu_end = content.find('</div>', menu_start)
        menu = content[menu_start:menu_end]
        
        # 检查是否有 http:// 链接
        if 'href="http' in menu:
            print('WARNING: Found http:// link in nav menu')
            # 找到并显示
            import re
            http_links = re.findall(r'href="(http[^"]+)"', menu)
            for link in http_links:
                print(f'  {link}')
        else:
            print('No http:// links found')
        
        # 检查是否有完整的工具链接
        tools = ['UUID Generator', 'Hash Generator', 'JWT', 'Regex', 'Base64', 'URL Encoder']
        for tool in tools:
            if tool in menu:
                print(f'  Has {tool}')
            else:
                print(f'  MISSING: {tool}')
