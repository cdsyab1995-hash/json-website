#!/usr/bin/env python3
"""
更准确地检查 script 标签
"""
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'd:\网站开发-json\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 找所有 script 标签的开始位置
script_starts = [(m.start(), m.group()) for m in re.finditer(r'<script[^>]*>', content)]
script_ends = [(m.start(), m.group()) for m in re.finditer(r'</script>', content)]

print('Script tags found:\n')
for pos, tag in script_starts:
    line_num = content[:pos].count('\n') + 1
    print(f'Line {line_num}: {tag}')

print(f'\nScript end tags found: {len(script_ends)}')
for pos, tag in script_ends:
    line_num = content[:pos].count('\n') + 1
    print(f'Line {line_num}: {tag}')

print(f'\nSummary: {len(script_starts)} open, {len(script_ends)} close')

# 检查是否有转义的 script 结束标签
escaped = re.findall(r'<\\/script>', content)
if escaped:
    print(f'\nFound {len(escaped)} escaped </script> tags (this is OK in JS strings)')
