#!/usr/bin/env python3
"""检查所有页面 Tools 下拉菜单是否一致"""
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

print('=== Tools Dropdown Menu Consistency Check ===\n')

results = {}
for f in sorted(os.listdir(pages_dir)):
    if not f.endswith('.html'):
        continue
    fp = os.path.join(pages_dir, f)
    with open(fp, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 查找 nav-dropdown-menu
    idx_start = content.find('nav-dropdown-menu')
    if idx_start == -1:
        results[f] = {'status': 'NO_DROPDOWN', 'tools': [], 'missing': standard_tools}
        continue
    
    idx_end = content.find('</div>\n            </div>', idx_start)
    if idx_end == -1:
        idx_end = content.find('</div>\n        </div>', idx_start)
    if idx_end == -1:
        results[f] = {'status': 'PARSE_ERROR', 'tools': [], 'missing': standard_tools}
        continue
    
    menu = content[idx_start:idx_end]
    
    # 提取工具名称
    tools = []
    # 匹配工具链接（排除 Tutorial/Practices/News 等非工具链接）
    tool_links = re.findall(r'<a href="((?:format|escape|extract|sort|clean|xml|yaml|viewer|json2csv|csv-to-excel|excel-remove-duplicates|merge-csv|batch-file-renamer|pdf-split|compare)\.html)"[^>]*>.*?</svg>\s*([^<]+)', menu, re.DOTALL)
    for href, text in tool_links:
        tools.append(text.strip())
    
    # 检查缺失
    missing = [t for t in standard_tools if t not in tools]
    
    results[f] = {
        'status': 'OK' if not missing else 'MISSING',
        'tools': tools,
        'missing': missing
    }

# 统计
ok_count = sum(1 for v in results.values() if v['status'] == 'OK')
missing_count = sum(1 for v in results.values() if v['status'] == 'MISSING')

# 输出详情
for f, data in results.items():
    status_icon = 'OK' if data['status'] == 'OK' else '!'
    print(f'{status_icon} {f}: {len(data["tools"])} tools')
    if data['missing']:
        print(f'   Missing: {data["missing"]}')
    print()

print('=== Summary ===')
print(f'OK: {ok_count}')
print(f'Missing tools: {missing_count}')
