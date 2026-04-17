# -*- coding: utf-8 -*-
import os

for fname in ['hash-generator.html', 'jwt-decoder.html', 'uuid-generator.html']:
    fp = rf'd:\网站开发-json\pages\{fname}'
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print(f'=== {fname} ===')
    print(f'Length: {len(content)} chars')
    
    # 查找 head 相关标签
    if '<head>' in content:
        print('Has <head>')
    if '</head>' in content:
        print('Has </head>')
    
    # 查找内联样式开始
    body_idx = content.find('<body')
    if body_idx >= 0:
        print(f'Body starts at: {body_idx}')
    
    # 显示 head 区域
    head_start = content.find('<head')
    if head_start >= 0:
        # 找到 </style> 或 <body>
        head_end = content.find('<body')
        if head_end > head_start:
            print(f'Head content (first 500): {content[head_start:head_start+500]}...')
    
    print()
