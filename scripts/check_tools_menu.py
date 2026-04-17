# -*- coding: utf-8 -*-
import os
import re

BASE_DIR = r'd:\网站开发-json\pages'

# 完整的工具列表（按类别）
ALL_TOOLS = [
    # JSON 工具
    'Format', 'Escape', 'Extract', 'Sort', 'Clean', 'XML', 'YAML', 'Viewer', 'Compare',
    # CSV/Excel 工具
    'CSV', 'Excel', 'Remove Duplicates', 'Merge CSV', 'Batch Rename',
    # 开发者工具
    'Regex', 'Base64', 'URL Encoder', 'UUID Generator', 'Hash Generator', 'JWT',
    # Utilities
    'PDF Split'
]

def check_tools_menu(filepath):
    """检查 Tools 下拉菜单中的工具"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    filename = os.path.basename(filepath)
    
    # 找到 nav-dropdown-menu
    idx = content.find('nav-dropdown-menu')
    if idx < 0:
        return None, "No dropdown menu"
    
    # 提取菜单内容
    menu_start = content.find('>', idx) + 1
    # 找到匹配的 </div>
    depth = 1
    pos = menu_start
    while depth > 0 and pos < len(content):
        if content[pos:pos+5] == '<div ':
            depth += 1
            pos += 5
        elif content[pos:pos+6] == '</div>':
            depth -= 1
            if depth == 0:
                break
            pos += 6
        else:
            pos += 1
    
    menu_content = content[menu_start:pos]
    
    # 检查每个工具
    found_tools = []
    missing_tools = []
    
    for tool in ALL_TOOLS:
        # 处理多词工具名
        tool_pattern = tool.replace(' ', r'\s*')
        if re.search(tool_pattern, menu_content, re.IGNORECASE):
            found_tools.append(tool)
        else:
            missing_tools.append(tool)
    
    return len(found_tools), missing_tools

# 检查所有页面
print('=== Tools 下拉菜单检查 ===')
print()

issues = []
for fname in sorted(os.listdir(BASE_DIR)):
    if not fname.endswith('.html'):
        continue
    
    fp = os.path.join(BASE_DIR, fname)
    count, missing = check_tools_menu(fp)
    
    if count is None:
        print(f'{fname}: {missing}')
    elif missing:
        issues.append((fname, missing))
        print(f'{fname}: {count}/21 tools, MISSING: {", ".join(missing)}')
    else:
        print(f'{fname}: OK (21/21)')

print()
print('=' * 60)
if issues:
    print(f'发现 {len(issues)} 个页面工具不完整')
else:
    print('所有页面工具完整！')
