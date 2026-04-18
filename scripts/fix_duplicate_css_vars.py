#!/usr/bin/env python3
"""
修复 CSS 中的重复变量定义
"""
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

css_path = r'd:\网站开发-json\css\styles.css'

with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# 找出所有变量定义
var_pattern = r'(--[\w-]+):\s*([^;]+);'
vars_found = list(re.finditer(var_pattern, css))

# 找出重复的变量
var_names = [v.group(1) for v in vars_found]
seen = {}
for match in vars_found:
    name = match.group(1)
    if name not in seen:
        seen[name] = []
    seen[name].append(match)

print('Duplicate CSS variables:')
removed = 0
for name, matches in seen.items():
    if len(matches) > 1:
        print(f'  {name}: {len(matches)} definitions')
        # 保留第一个，删除后面的
        for match in matches[1:]:
            # 尝试删除整行
            line_start = css.rfind('\n', 0, match.start()) + 1
            line_end = css.find('\n', match.end())
            if line_end == -1:
                line_end = len(css)
            old_line = css[line_start:line_end]
            # 删除这一行
            css = css[:line_start] + css[line_end:]
            removed += 1
            print(f'    Removed duplicate at position {match.start()}')

print(f'\nTotal removed: {removed} duplicate definitions')

# 保存修复后的 CSS
with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print('CSS file updated!')

# 验证
with open(css_path, 'r', encoding='utf-8') as f:
    new_css = f.read()

vars_found = list(re.finditer(var_pattern, new_css))
var_names = [v.group(1) for v in vars_found]
from collections import Counter
duplicates = {k: v for k, v in Counter(var_names).items() if v > 1}
if duplicates:
    print(f'WARNING: Still have duplicates: {duplicates}')
else:
    print('SUCCESS: All duplicates removed!')
