# -*- coding: utf-8 -*-
"""
检查并修复 Twitter Card 标签
"""
import os
import re

BASE_DIR = r'd:\网站开发-json'

def check_twitter_card(filepath):
    """检查是否有 Twitter Card 标签"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    has_twitter_card = bool(re.search(r'<meta name="twitter:', content))
    has_twitter_image = 'twitter:image' in content
    has_twitter_title = 'twitter:title' in content
    has_twitter_desc = 'twitter:description' in content
    
    return {
        'has_twitter_card': has_twitter_card,
        'has_twitter_image': has_twitter_image,
        'has_twitter_title': has_twitter_title,
        'has_twitter_desc': has_twitter_desc,
    }

def add_twitter_card(filepath):
    """添加 Twitter Card 标签"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 检查是否已有 Twitter Card
    if re.search(r'<meta name="twitter:', content):
        return False
    
    # 提取 og:title, og:description, og:image 作为 Twitter Card 的默认值
    og_title_match = re.search(r'<meta property="og:title" content="([^"]+)"', content)
    og_desc_match = re.search(r'<meta property="og:description" content="([^"]+)"', content)
    og_image_match = re.search(r'<meta property="og:image" content="([^"]+)"', content)
    og_url_match = re.search(r'<meta property="og:url" content="([^"]+)"', content)
    
    og_title = og_title_match.group(1) if og_title_match else 'AI JSON Tools'
    og_desc = og_desc_match.group(1) if og_desc_match else 'Free JSON formatting, validation, and conversion tools'
    og_image = og_image_match.group(1) if og_image_match else 'https://aijsons.com/og-image.png'
    og_url = og_url_match.group(1) if og_url_match else 'https://aijsons.com/'
    
    # Twitter Card 标签
    twitter_card = f'''    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{og_title}">
    <meta name="twitter:description" content="{og_desc}">
    <meta name="twitter:image" content="{og_image}">
    <meta name="twitter:url" content="{og_url}">
'''
    
    # 在 </head> 前插入
    head_end = content.find('</head>')
    if head_end >= 0:
        content = content[:head_end] + twitter_card + content[head_end:]
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    
    return False

# 检查所有页面
print('=== Twitter Card 检查 ===\n')

pages_dir = os.path.join(BASE_DIR, 'pages')
pages = [f for f in os.listdir(pages_dir) if f.endswith('.html')]

# 也检查根目录
index_path = os.path.join(BASE_DIR, 'index.html')
if os.path.exists(index_path):
    pages.insert(0, 'index.html')

missing_twitter = []
fixed_count = 0

for page in pages:
    if page == 'index.html':
        filepath = index_path
    else:
        filepath = os.path.join(pages_dir, page)
    
    result = check_twitter_card(filepath)
    
    if not result['has_twitter_card']:
        missing_twitter.append(page)
        # 尝试添加
        if add_twitter_card(filepath):
            print(f'{page}: Added Twitter Card')
            fixed_count += 1
        else:
            print(f'{page}: Failed to add')
    else:
        print(f'{page}: OK')

print(f'\n=== Summary ===')
print(f'Missing: {len(missing_twitter)} pages')
print(f'Fixed: {fixed_count} pages')
