#!/usr/bin/env python3
"""
移除/注释掉 console.log 语句
"""
import os
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

root_dir = r'd:\网站开发-json'

def remove_console_logs(filepath):
    """移除单个文件中的 console 语句"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    changes = 0
    
    # 匹配 console.log(...)
    content = re.sub(r'console\.log\([^)]+\);?', '// console.log removed', content)
    content = re.sub(r'console\.debug\([^)]+\);?', '// console.debug removed', content)
    content = re.sub(r'console\.info\([^)]+\);?', '// console.info removed', content)
    
    # 匹配单行注释的 console
    content = re.sub(r'//\s*console\.[^\n]+', '// console statement removed', content)
    
    changes = original.count('console.log') + original.count('console.debug') + original.count('console.info')
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
    
    return changes

# 扫描所有文件
print('Removing console statements...\n')

total_changes = 0
files_changed = 0

for root, dirs, files in os.walk(root_dir):
    for filename in files:
        if not filename.endswith(('.html', '.js')):
            continue
        
        filepath = os.path.join(root, filename)
        rel_path = os.path.relpath(filepath, root_dir)
        
        changes = remove_console_logs(filepath)
        if changes > 0:
            files_changed += 1
            total_changes += changes
            print(f'{rel_path}: {changes} removed')

print(f'\nTotal: {total_changes} statements removed from {files_changed} files')
