#!/usr/bin/env python3
"""
修复 HTML meta 标签语法错误
"""
import os
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

root_dir = r'd:\网站开发-json'

def fix_meta_tags(filepath):
    """修复单个文件的 meta 标签问题"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    changes = []
    
    # 1. 修复 description meta 标签没有闭合的问题
    # 匹配: <meta name="description" content="..." <meta name="keywords"
    pattern = r'(<meta name="description" content="[^"]+?)\s+(<meta name="keywords")'
    if re.search(pattern, content):
        content = re.sub(pattern, r'\1"> \2', content)
        changes.append('Fixed unclosed description meta tag')
    
    # 2. 修复重复的 author meta 标签
    author_pattern = r'(<meta name="author" content="[^"]+">)\s*(<meta name="author" content="[^"]+">)'
    if re.search(author_pattern, content):
        content = re.sub(author_pattern, r'\1', content)
        changes.append('Removed duplicate author meta tag')
    
    # 3. 检查重复的 robots meta
    robots_count = len(re.findall(r'<meta name="robots"', content))
    if robots_count > 1:
        content = re.sub(r'(<meta name="robots" content="[^"]+">)\s*(?:<meta name="robots"[^>]*>\s*)+', r'\1', content)
        changes.append('Removed duplicate robots meta tag')
    
    # 4. 检查是否有未闭合的 style 标签
    style_open = len(re.findall(r'<style[^>]*>', content))
    style_close = len(re.findall(r'</style>', content))
    if style_open != style_close:
        changes.append(f'Unmatched style tags: {style_open} open, {style_close} close')
    
    # 5. 检查是否有未闭合的 script 标签
    script_open = len(re.findall(r'<script[^>]*>', content))
    script_close = len(re.findall(r'</script>', content))
    if script_open != script_close:
        changes.append(f'Unmatched script tags: {script_open} open, {script_close} close')
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
    
    return changes

# 扫描所有 HTML 文件
print('Scanning HTML files for meta tag issues...\n')

total_changes = 0
files_with_issues = []

for root, dirs, files in os.walk(root_dir):
    for filename in files:
        if not filename.endswith('.html'):
            continue
        
        filepath = os.path.join(root, filename)
        rel_path = os.path.relpath(filepath, root_dir)
        
        changes = fix_meta_tags(filepath)
        if changes:
            files_with_issues.append((rel_path, changes))
            total_changes += len(changes)
            print(f'{rel_path}:')
            for change in changes:
                print(f'  - {change}')
            print()

print(f'\nTotal: {total_changes} changes in {len(files_with_issues)} files')
