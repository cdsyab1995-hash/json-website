# -*- coding: utf-8 -*-
import os
import re

BASE_DIR = r'd:\网站开发-json\pages'

# 正确的检查方法：找到 nav-dropdown-menu 的 div 容器
P1_TOOLS = ['uuid-generator.html', 'hash-generator.html', 'jwt-decoder.html', 
            'regex-tester.html', 'base64.html', 'url-encoder.html']

def check_navbar(filepath):
    """检查导航栏是否包含所有 P1 工具"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    filename = os.path.basename(filepath)
    
    # 检查是否包含所有 6 个 P1 工具页面链接
    missing = []
    for tool in P1_TOOLS:
        # 检查链接是否存在
        pattern = f'href="{tool}"'
        if pattern not in content:
            missing.append(tool)
    
    return missing

# 检查所有页面
print('Checking all pages for P1 tool links...')
print('=' * 60)

issues = []
for fname in sorted(os.listdir(BASE_DIR)):
    if not fname.endswith('.html'):
        continue
    
    fp = os.path.join(BASE_DIR, fname)
    missing = check_navbar(fp)
    
    if missing:
        issues.append((fname, missing))
        print(f'{fname}: MISSING -> {", ".join(missing)}')
    else:
        print(f'{fname}: OK')

print('=' * 60)
if issues:
    print(f'Found issues in {len(issues)} pages')
else:
    print('All pages are OK!')
