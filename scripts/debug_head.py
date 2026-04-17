# -*- coding: utf-8 -*-
import os

fname = 'hash-generator.html'
fp = rf'd:\网站开发-json\pages\{fname}'
with open(fp, 'r', encoding='utf-8') as f:
    content = f.read()

print('=== hash-generator.html HEAD SECTION ===')
print()

# 找到 head 区域
head_start = content.find('<head')
if head_start >= 0:
    # 提取 head 内容（到第一个 </style> 或 </style>）
    # 查找所有的 </xxx> 标签
    import re
    
    # 找到 <title> 标签
    title_match = re.search(r'<title>([^<]+)</title>', content)
    title = title_match.group(1) if title_match else 'Unknown'
    print(f'Title: {title}')
    
    # 查找 meta 标签
    meta_tags = re.findall(r'<meta[^>]+>', content[:2000])
    print(f'Meta tags found: {len(meta_tags)}')
    for tag in meta_tags[:5]:
        print(f'  {tag}')
    
    # 查找是否有 og: tags
    og_tags = re.findall(r'<meta property="og:[^>]+>', content)
    print(f'\nOG tags found: {len(og_tags)}')
    for tag in og_tags[:3]:
        print(f'  {tag}')
    
    # 查找 twitter tags
    twitter_tags = re.findall(r'<meta name="twitter:[^>]+>', content)
    print(f'\nTwitter tags found: {len(twitter_tags)}')
    
    # 显示 head 区域末尾
    print('\n--- Head section end (chars 1500-1800) ---')
    print(content[1500:1800])
