#!/usr/bin/env python3
"""
检查 script 标签问题
"""
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

# 检查 index.html 的 script 标签
with open(r'd:\网站开发-json\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 找到所有 script 标签
scripts = re.findall(r'<script[^>]*>(.*?)</script>', content, re.DOTALL)

print(f'Found {len(scripts)} script blocks:\n')

for i, script in enumerate(scripts):
    preview = script[:100].replace('\n', ' ').strip()
    if len(script) > 100:
        preview += '...'
    print(f'{i+1}. {preview}')
    print()
