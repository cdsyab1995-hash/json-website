# -*- coding: utf-8 -*-
"""
修复剩余页面的 Twitter Card
"""
import os
import re

BASE_DIR = r'd:\网站开发-json'

def fix_page(filepath):
    """修复单个页面的 Twitter Card"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 检查是否已有 Twitter Card
    if re.search(r'<meta name="twitter:', content):
        return True
    
    # 检查是否有 </head>
    if '</head>' not in content:
        print(f'{os.path.basename(filepath)}: No </head> found')
        return False
    
    # 提取 og:title, og:description, og:image
    og_title_match = re.search(r'<meta property="og:title" content="([^"]+)"', content)
    og_desc_match = re.search(r'<meta property="og:description" content="([^"]+)"', content)
    og_image_match = re.search(r'<meta property="og:image" content="([^"]+)"', content)
    
    og_title = og_title_match.group(1) if og_title_match else 'AI JSON Tools'
    og_desc = og_desc_match.group(1) if og_desc_match else 'Free JSON formatting, validation, and conversion tools'
    og_image = og_image_match.group(1) if og_image_match else 'https://aijsons.com/og-image.png'
    
    # Twitter Card 标签
    twitter_card = f'''    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{og_title}">
    <meta name="twitter:description" content="{og_desc}">
    <meta name="twitter:image" content="{og_image}">
'''
    
    # 在 </head> 前插入
    head_end = content.find('</head>')
    content = content[:head_end] + twitter_card + content[head_end:]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

# 修复失败的页面
failed_pages = [
    r'd:\网站开发-json\pages\hash-generator.html',
    r'd:\网站开发-json\pages\jwt-decoder.html',
    r'd:\网站开发-json\pages\uuid-generator.html',
]

for fp in failed_pages:
    if fix_page(fp):
        print(f'{os.path.basename(fp)}: Fixed')
    else:
        print(f'{os.path.basename(fp)}: Failed')
