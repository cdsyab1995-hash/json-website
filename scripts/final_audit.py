#!/usr/bin/env python3
"""
最终代码审计 - 检查优化效果
"""
import os
import re
import sys
from collections import Counter
sys.stdout.reconfigure(encoding='utf-8')

root_dir = r'd:\网站开发-json'

print('=' * 60)
print('最终代码审计报告')
print('=' * 60)

# 1. 统计文件数量
html_files = []
css_files = []
js_files = []

for root, dirs, files in os.walk(root_dir):
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))
        elif f.endswith('.css'):
            css_files.append(os.path.join(root, f))
        elif f.endswith('.js'):
            js_files.append(os.path.join(root, f))

print(f'\n文件统计:')
print(f'  HTML 文件: {len(html_files)}')
print(f'  CSS 文件: {len(css_files)}')
print(f'  JS 文件: {len(js_files)}')

# 2. 统计代码体积
total_html_size = 0
total_css_size = 0
total_js_size = 0

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        total_html_size += len(file.read().encode('utf-8'))

for f in css_files:
    with open(f, 'r', encoding='utf-8') as file:
        total_css_size += len(file.read().encode('utf-8'))

for f in js_files:
    with open(f, 'r', encoding='utf-8') as file:
        total_js_size += len(file.read().encode('utf-8'))

print(f'\n代码体积:')
print(f'  HTML: {total_html_size:,} bytes ({total_html_size/1024:.1f} KB)')
print(f'  CSS: {total_css_size:,} bytes ({total_css_size/1024:.1f} KB)')
print(f'  JS: {total_js_size:,} bytes ({total_js_size/1024:.1f} KB)')
print(f'  总计: {(total_html_size+total_css_size+total_js_size)/1024:.1f} KB')

# 3. 统计内联样式和脚本
inline_styles = 0
inline_scripts = 0

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    inline_styles += len(re.findall(r'style="[^"]*"', content))
    inline_scripts += len(re.findall(r'<script[^>]*>(?!.*</script>)', content))

print(f'\n内联代码统计:')
print(f'  内联样式: {inline_styles} (优化前: ~824)')
print(f'  内联脚本: {inline_scripts} (优化前: ~114)')

# 4. 检查 console 语句
console_count = 0
for filepath in html_files + js_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    console_count += len(re.findall(r'console\.(log|debug|info|warn)', content))

print(f'\n调试代码:')
print(f'  console 语句: {console_count} (优化前: 40+)')

# 5. 检查重复 ID
duplicate_ids = {}
for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    ids = re.findall(r'\sid="([^"]+)"', content)
    for id_name in ids:
        if id_name not in duplicate_ids:
            duplicate_ids[id_name] = []
        duplicate_ids[id_name].append(os.path.relpath(filepath, root_dir))

duplicate_ids = {k: v for k, v in duplicate_ids.items() if len(v) > 1}
print(f'\n重复 ID:')
print(f'  数量: {len(duplicate_ids)}')

# 6. 检查未闭合标签
unclosed_issues = 0
for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    # 检查 meta 标签
    if 'content="..." <meta' in content or 'content=\\"...\\" <meta' in content:
        unclosed_issues += 1

print(f'\nHTML 语法问题:')
print(f'  未闭合 meta 标签: {unclosed_issues} (优化前: 2)')

print('\n' + '=' * 60)
print('审计完成')
print('=' * 60)
