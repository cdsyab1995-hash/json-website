# -*- coding: utf-8 -*-
"""
修复 P1 工具页面的 Twitter Card
"""
import os
import re

def fix_page(filepath):
    """修复单个页面的 Twitter Card"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    filename = os.path.basename(filepath)
    
    # 检查是否已有 Twitter Card
    if '<meta name="twitter:' in content:
        print(f'{filename}: Already has Twitter Card')
        return True
    
    # 提取 og:title, og:description, og:image
    og_title_match = re.search(r'<meta property="og:title" content="([^"]+)"', content)
    og_desc_match = re.search(r'<meta property="og:description" content="([^"]+)"', content)
    og_image_match = re.search(r'<meta property="og:image" content="([^"]+)"', content)
    
    og_title = og_title_match.group(1) if og_title_match else 'AI JSON Tools'
    og_desc = og_desc_match.group(1) if og_desc_match else 'Free JSON formatting, validation, and conversion tools'
    og_image = og_image_match.group(1) if og_image_match else 'https://aijsons.com/og-image.png'
    
    # Twitter Card 标签
    twitter_card = f'<meta name="twitter:card" content="summary_large_image">\n    <meta name="twitter:title" content="{og_title}">\n    <meta name="twitter:description" content="{og_desc}">\n    <meta name="twitter:image" content="{og_image}">\n'
    
    # 在最后一个 meta 标签后插入
    # 找到最后一个 </style> 标签
    style_close = content.rfind('</style>')
    if style_close >= 0:
        insert_pos = style_close + 8  # after </style>
        content = content[:insert_pos] + '\n    ' + twitter_card + content[insert_pos:]
    else:
        # 在 <body 之前插入
        body_pos = content.find('<body')
        if body_pos >= 0:
            content = content[:body_pos] + '    ' + twitter_card + '\n' + content[body_pos:]
        else:
            print(f'{filename}: Cannot find insertion point')
            return False
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'{filename}: Fixed')
    return True

# 修复失败的页面
failed_pages = [
    r'd:\网站开发-json\pages\hash-generator.html',
    r'd:\网站开发-json\pages\jwt-decoder.html',
    r'd:\网站开发-json\pages\uuid-generator.html',
]

for fp in failed_pages:
    fix_page(fp)
