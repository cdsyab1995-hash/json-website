#!/usr/bin/env python3
"""
批量替换内联样式为 CSS 类
"""
import os
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

root_dir = r'd:\网站开发-json'

# 定义替换规则: (内联样式, CSS类)
replacements = [
    # 最常见的样式
    ('color: var(--primary);', 'class="text-primary"'),
    ('color: var(--primary); margin: 0;', 'class="text-primary mb-0"'),
    ('font-size: 0.75rem; color: var(--text-secondary);', 'class="text-small text-secondary"'),
    ('font-size: 0.8rem; color: var(--text-secondary);', 'class="text-small text-secondary"'),
    ('font-size: 0.875rem; color: var(--text-secondary);', 'class="text-sm text-secondary"'),
    ('font-size: 0.875rem; color: var(--text-secondary);', 'class="text-sm text-secondary"'),
    ('font-size: 1rem; color: var(--text-secondary);', 'class="text-secondary"'),
    ('font-size: 1.125rem; margin-bottom: 0.5rem; color: var(--primary);', 'class="text-lg text-primary mb-sm"'),
    ('font-size: 1.125rem; margin-bottom: 0.5rem; color: var(--primary);', 'class="text-lg text-primary mb-sm"'),
    ('font-size: 1.125rem; margin-bottom: 0.5rem;', 'class="text-lg mb-sm"'),
    ('font-size: 1.125rem; margin-bottom: 1rem;', 'class="text-lg mb-md"'),
    ('font-size: 1.125rem; color: var(--primary);', 'class="text-lg text-primary"'),
    ('font-size: 1.5rem; margin-bottom: 1rem;', 'class="text-xl mb-md"'),
    ('font-size: 0.875rem; margin-top: 0.5rem;', 'class="text-sm mt-sm"'),
    ('margin-top: 0.5rem; font-size: 0.875rem;', 'class="text-sm mt-sm"'),
    ('margin-top: 0.5rem; font-size: 0.75rem; color: var(--text-light);', 'class="text-small mt-sm"'),
    ('margin-top: 0.5rem; font-size: 0.875rem; color: var(--primary);', 'class="text-primary text-sm mt-sm"'),
    ('display: inline-block; margin-top: 0.75rem; color: var(--primary); font-weight: 500;', 'class="inline-block mt-sm text-primary" style="font-weight:500"'),
    ('padding: 1rem;', 'class="p-md"'),
    ('padding: 0.5rem;', 'class="p-sm"'),
    ('min-height: 100px; cursor: pointer;', 'class="min-h-100 cursor-pointer"'),
    ('cursor: pointer; min-height: 100px;', 'class="min-h-100 cursor-pointer"'),
]

def replace_inline_styles(filepath):
    """替换单个文件的内联样式"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    changes = 0
    
    for old_style, new_class in replacements:
        # 匹配 style="..." 属性
        pattern = rf'style="{re.escape(old_style)}"'
        new_attr = f'class="{new_class}"'
        
        # 简单替换
        if pattern.replace('\\', '') in content:
            content = re.sub(pattern, new_attr, content)
            changes += 1
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
    
    return changes

# 扫描所有 HTML 文件
print('Replacing inline styles with CSS classes...\n')

total_changes = 0
files_changed = 0

for root, dirs, files in os.walk(root_dir):
    for filename in files:
        if not filename.endswith('.html'):
            continue
        
        filepath = os.path.join(root, filename)
        rel_path = os.path.relpath(filepath, root_dir)
        
        changes = replace_inline_styles(filepath)
        if changes > 0:
            files_changed += 1
            total_changes += changes
            print(f'{rel_path}: {changes} replacements')

print(f'\nTotal: {total_changes} replacements in {files_changed} files')
