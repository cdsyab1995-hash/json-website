#!/usr/bin/env python3
import re

fp = r'd:\网站开发-json\pages\format.html'
with open(fp, 'r', encoding='utf-8') as f:
    content = f.read()

# 查找 Tools 下拉菜单
idx = content.find('nav-dropdown-menu')
if idx > 0:
    menu = content[idx:idx+8000]
    # 提取所有链接
    links = re.findall(r'<a href="([^"]+)"[^>]*>.*?</svg>\s*([^<]+)', menu, re.DOTALL)
    for href, text in links[:20]:
        print(f'{href}: {text.strip()}')
else:
    print('nav-dropdown-menu not found')
    # 尝试其他方式
    idx = content.find('Tools')
    if idx > 0:
        print(content[idx:idx+2000])
