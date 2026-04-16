#!/usr/bin/env python3
"""检查所有页面 Tools 下拉菜单内容"""
import os
import re

pages_dir = r'd:\网站开发-json\pages'

# 定义标准工具列表（按导航栏顺序）
standard_tools = [
    'Format', 'Escape', 'Extract', 'Sort', 'Clean',
    'XML', 'YAML', 'Viewer',
    'CSV', 'Excel', 'Remove Duplicates',
    'Merge CSV', 'Batch Rename', 'PDF Split', 'Compare'
]

print('=== Tools Dropdown Menu Check ===\n')

results = []

for f in sorted(os.listdir(pages_dir)):
    if not f.endswith('.html'):
        continue
    fp = os.path.join(pages_dir, f)
    with open(fp, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 查找 nav-dropdown-menu
    match = re.search(r'nav-dropdown-menu[^>]*>(.*?)</div>\s*</div>', content, re.DOTALL)
    if match:
        menu_content = match.group(1)
        # 提取所有链接文本
        tools = re.findall(r'<a href="[^"]+\.html"[^>]*>(?:<svg[^>]*>.*?</svg>\s*)?([^<]+)', menu_content)
        tools = [t.strip() for t in tools if t.strip()]
        
        # 检查是否缺少工具
        missing = [t for t in standard_tools if t not in tools]
        extra = [t for t in tools if t not in standard_tools]
        
        if missing or extra:
            status = 'MISMATCH'
            print(f'{f}: {status}')
            print(f'  Found: {tools}')
            if missing:
                print(f'  Missing: {missing}')
            if extra:
                print(f'  Extra: {extra}')
            print()
        else:
            print(f'{f}: OK ({len(tools)} tools)')
            results.append((f, 'OK'))
    
print('\n=== Summary ===')
ok_count = sum(1 for _, s in results if s == 'OK')
mismatch_count = len([f for f in os.listdir(pages_dir) if f.endswith('.html')]) - ok_count
print(f'OK: {ok_count}')
print(f'Mismatch: {mismatch_count}')
