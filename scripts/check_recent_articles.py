# -*- coding: utf-8 -*-
import re

# 检查 index.html 的 Recent Articles 部分
with open(r'd:\网站开发-json\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 找到 Recent Articles 部分
articles_start = content.find('Recent Articles')
if articles_start < 0:
    articles_start = content.find('recent-articles')
if articles_start < 0:
    articles_start = content.find('id="blog"')
if articles_start < 0:
    articles_start = content.find('class="blog"')

if articles_start >= 0:
    articles_end = content.find('<section', articles_start + 100)
    if articles_end < 0:
        articles_end = articles_start + 3000
    articles_content = content[articles_start:articles_end]
    
    print('=== 首页 Recent Articles 部分 ===')
    print()
    print(articles_content[:2000])
else:
    print('未找到 Recent Articles 部分')
    # 搜索 blog 相关内容
    blog_idx = content.find('blog.html')
    if blog_idx >= 0:
        print(f'\n找到 blog.html 引用在位置 {blog_idx}')
        print(content[max(0, blog_idx-200):blog_idx+500])
