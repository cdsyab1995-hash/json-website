# -*- coding: utf-8 -*-
"""
检查并添加图片 lazy loading
"""
import os
import re

BASE_DIR = r'd:\网站开发-json'

def check_images(filepath):
    """检查页面中的图片"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    filename = os.path.basename(filepath)
    
    # 查找所有 <img 标签
    img_tags = re.findall(r'<img[^>]+>', content)
    
    # 查找没有 loading="lazy" 的图片
    non_lazy = []
    for img in img_tags:
        if 'loading=' not in img:
            non_lazy.append(img[:100])
        elif 'loading="lazy"' not in img and "loading='lazy'" not in img:
            non_lazy.append(img[:100])
    
    if non_lazy:
        print(f'{filename}: {len(non_lazy)} images without lazy loading')
        return len(non_lazy)
    else:
        print(f'{filename}: OK ({len(img_tags)} images)')
        return 0

# 检查所有页面
print('=== Lazy Loading 检查 ===\n')

pages_dir = os.path.join(BASE_DIR, 'pages')
pages = [f for f in os.listdir(pages_dir) if f.endswith('.html')]

total_non_lazy = 0
for page in pages:
    filepath = os.path.join(pages_dir, page)
    total_non_lazy += check_images(filepath)

print(f'\n=== Summary ===')
print(f'Total images without lazy loading: {total_non_lazy}')
