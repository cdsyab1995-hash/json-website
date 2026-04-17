# -*- coding: utf-8 -*-
import os
import re

# 检查 pages 目录
pages_dir = r'd:\网站开发-json\pages'
files = sorted([f for f in os.listdir(pages_dir) if f.endswith('.html')])
print('=== pages/ 目录 ===')
for f in files:
    print(f)

# 检查 blog.html 和 news.html 是否存在
print('\n=== 文件存在性检查 ===')
for f in ['blog.html', 'news.html']:
    path = os.path.join(pages_dir, f)
    print(f'{f}: {"存在" if os.path.exists(path) else "不存在"}')

# 检查 index.html 中的 blog 和 news 链接
print()
print('=== index.html 中的 Blog/News 链接 ===')
with open(r'd:\网站开发-json\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

links = re.findall(r'href="([^"]+)"[^>]*>([^<]+)', content)
for href, text in links:
    if 'blog' in href.lower() or 'news' in href.lower() or 'Blog' in text or 'News' in text:
        print(f'{text} -> {href}')

# 检查 sitemap.xml
print()
print('=== sitemap.xml 中的 Blog/News ===')
with open(r'd:\网站开发-json\sitemap.xml', 'r', encoding='utf-8') as f:
    sitemap = f.read()
    
blog_count = sitemap.count('blog.html')
news_count = sitemap.count('news.html')
print(f'blog.html: {blog_count} 次')
print(f'news.html: {news_count} 次')
