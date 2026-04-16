#!/usr/bin/env python3
"""详细检查 Tools 下拉菜单内容"""
import os
import re

pages_dir = r'd:\网站开发-json\pages'

# 定义标准工具列表
standard_tools = [
    'Format', 'Escape', 'Extract', 'Sort', 'Clean',
    'XML', 'YAML', 'Viewer',
    'CSV', 'Excel', 'Remove Duplicates',
    'Merge CSV', 'Batch Rename', 'PDF Split', 'Compare'
]

# 工具链接的 href 前缀
tool_hrefs = [
    'format', 'escape', 'extract', 'sort', 'clean',
    'xml', 'yaml', 'viewer',
    'json2csv', 'csv-to-excel', 'excel-remove-duplicates',
    'merge-csv', 'batch-file-renamer', 'pdf-split', 'compare'
]

print('=== Detailed Tools Dropdown Check ===\n')

for f in sorted(os.listdir(pages_dir)):
    if not f.endswith('.html'):
        continue
    fp = os.path.join(pages_dir, f)
    with open(fp, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 检查是否有 nav-dropdown-menu
    has_dropdown = 'nav-dropdown-menu' in content
    if not has_dropdown:
        print(f'{f}: NO DROPDOWN')
        continue
    
    # 查找 nav-dropdown-menu 内容
    # 找到 Tools 链接后面的菜单
    idx_tools = content.find('nav-dropdown-toggle')
    if idx_tools == -1:
        print(f'{f}: NO TOOLS TOGGLE')
        continue
    
    # 找到菜单内容
    idx_menu = content.find('nav-dropdown-menu', idx_tools)
    if idx_menu == -1:
        print(f'{f}: NO MENU')
        continue
    
    # 找到菜单结束
    menu_text = content[idx_menu:]
    idx_end = menu_text.find('</div>')
    if idx_end > 0:
        menu_text = menu_text[:idx_end]
    
    # 提取工具
    tools = []
    for href_prefix in tool_hrefs:
        pattern = f'<a href="{href_prefix}\\.html"[^>]*>.*?</svg>\\s*([^<]+)'
        match = re.search(pattern, menu_text, re.DOTALL)
        if match:
            tools.append(match.group(1).strip())
    
    # 检查缺失
    missing = [t for t in standard_tools if t not in tools]
    extra = [t for t in tools if t not in standard_tools]
    
    status = 'OK' if not missing and not extra else 'MISMATCH'
    print(f'{f}: [{status}] {len(tools)} tools')
    if missing:
        print(f'   Missing: {missing}')
    if extra:
        print(f'   Extra: {extra}')

print('\nDone!')
