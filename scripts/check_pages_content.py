# -*- coding: utf-8 -*-
import os

# 检查 blog.html 和 news.html 的内容
for fname in ['blog.html', 'news.html']:
    fp = rf'd:\网站开发-json\pages\{fname}'
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print(f'=== {fname} ===')
    print(f'文件大小: {len(content)} 字符')
    
    # 提取 title
    import re
    title_match = re.search(r'<title>([^<]+)</title>', content)
    if title_match:
        print(f'Title: {title_match.group(1)}')
    
    # 检查是否有实际文章内容
    article_count = len(re.findall(r'<article', content))
    h2_count = len(re.findall(r'<h2', content))
    h3_count = len(re.findall(r'<h3', content))
    
    print(f'<article> 标签数: {article_count}')
    print(f'<h2> 标签数: {h2_count}')
    print(f'<h3> 标签数: {h3_count}')
    
    # 检查内容区域
    main_idx = content.find('<main')
    if main_idx < 0:
        main_idx = content.find('class="main')
    
    if main_idx >= 0:
        # 获取 main 内容的前 500 字符
        main_content = content[main_idx:main_idx+500]
        # 移除 HTML 标签
        text = re.sub(r'<[^>]+>', ' ', main_content)
        text = ' '.join(text.split())
        print(f'Main 内容预览: {text[:300]}...')
    
    print()
