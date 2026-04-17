# -*- coding: utf-8 -*-
"""
检查各种资源的 lazy loading
"""
import os
import re

BASE_DIR = r'd:\网站开发-json'

def check_resources(filepath):
    """检查页面中的各种资源"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    filename = os.path.basename(filepath)
    issues = []
    
    # 检查 <img> 标签
    img_tags = re.findall(r'<img[^>]+>', content)
    for img in img_tags:
        if 'loading=' not in img:
            issues.append(f'img: {img[:80]}...')
        elif 'loading="lazy"' not in img and "loading='lazy'" not in img:
            issues.append(f'img (no lazy): {img[:80]}')
    
    # 检查 <iframe> 标签
    iframe_tags = re.findall(r'<iframe[^>]+>', content)
    for iframe in iframe_tags:
        if 'loading=' not in iframe:
            issues.append(f'iframe: {iframe[:80]}...')
    
    # 检查 <script> 标签 (外部 JS)
    script_tags = re.findall(r'<script src="[^"]+">', content)
    for script in script_tags:
        if 'defer' not in script and 'async' not in script:
            issues.append(f'script (blocking): {script[:60]}...')
    
    if issues:
        print(f'{filename}: {len(issues)} issues')
        for issue in issues[:3]:
            print(f'  - {issue[:100]}')
        return len(issues)
    else:
        print(f'{filename}: OK')
        return 0

# 检查 index.html
print('=== Resource Loading 检查 ===\n')

index_path = os.path.join(BASE_DIR, 'index.html')
check_resources(index_path)

print()

# 检查 pages 目录
pages_dir = os.path.join(BASE_DIR, 'pages')
pages = [f for f in os.listdir(pages_dir) if f.endswith('.html')]

total_issues = 0
for page in pages:
    filepath = os.path.join(pages_dir, page)
    total_issues += check_resources(filepath)

print(f'\n=== Summary ===')
print(f'Total resource issues: {total_issues}')
