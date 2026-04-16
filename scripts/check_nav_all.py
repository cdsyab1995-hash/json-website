# -*- coding: utf-8 -*-
import os
import re

BASE_DIR = r'd:\网站开发-json\pages'

P1_TOOLS = ['UUID Generator', 'Hash Generator', 'JWT Decoder', 'Regex Tester', 'Base64 Encoder', 'URL Encoder']

# 检查每个页面的导航栏
for fname in sorted(os.listdir(BASE_DIR)):
    if not fname.endswith('.html'):
        continue
    
    fp = os.path.join(BASE_DIR, fname)
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 查找 nav-dropdown-menu
    idx = content.find('nav-dropdown-menu')
    if idx < 0:
        print(f'{fname}: NO dropdown menu')
        continue
    
    # 提取菜单内容
    menu_start = content.find('>', idx) + 1
    menu_end = content.find('</div>', menu_start)
    menu_content = content[menu_start:menu_end]
    
    # 检查关键工具
    has_uuid = 'UUID Generator' in menu_content
    has_hash = 'Hash Generator' in menu_content
    has_jwt = 'JWT' in menu_content
    has_regex = 'Regex' in menu_content
    has_base64 = 'Base64' in menu_content
    has_url = 'URL Encoder' in menu_content
    
    status = []
    if not has_uuid: status.append('NO-UUID')
    if not has_hash: status.append('NO-Hash')
    if not has_jwt: status.append('NO-JWT')
    if not has_regex: status.append('NO-Regex')
    if not has_base64: status.append('NO-Base64')
    if not has_url: status.append('NO-URL')
    
    # 检查是否有错误的 HTML 显示
    if 'href="' in menu_content and 'href="http' in menu_content:
        status.append('BAD-HREF')
    
    if status:
        print(f'{fname}: {" | ".join(status)}')
    else:
        print(f'{fname}: OK')
