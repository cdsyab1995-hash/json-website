# -*- coding: utf-8 -*-
import os
import re

BASE_DIR = r'd:\网站开发-json\pages'

# 检查每个页面的导航栏中是否有 Blog 和 News 链接
print('=== 检查导航栏中的 Blog/News 链接 ===')
print()

for fname in sorted(os.listdir(BASE_DIR)):
    if not fname.endswith('.html'):
        continue
    
    fp = os.path.join(BASE_DIR, fname)
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 检查是否有 blog.html 和 news.html 链接
    has_blog = 'href="blog.html"' in content or "href='blog.html'" in content
    has_news = 'href="news.html"' in content or "href='news.html'" in content
    
    if not has_blog or not has_news:
        status = []
        if not has_blog: status.append('NO-BLOG')
        if not has_news: status.append('NO-NEWS')
        print(f'{fname}: {" | ".join(status)}')
