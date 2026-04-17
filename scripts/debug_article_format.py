# -*- coding: utf-8 -*-
import re

# 检查 blog.html 中的文章格式
with open(r'd:\网站开发-json\pages\blog.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 找到第一个 ai-daily 文章
article_match = re.search(r'<article id="(ai-daily-\d+[a-z]?)".*?</article>', content, re.DOTALL)
if article_match:
    print("First article sample:")
    print(article_match.group(0)[:3000])
else:
    # 尝试另一种方式
    start = content.find('ai-daily-20260416b')
    if start >= 0:
        # 找到 <article 开始位置
        article_start = content.rfind('<article', 0, start)
        article_end = content.find('</article>', start) + len('</article>')
        if article_end > article_start:
            print("Article from blog.html:")
            print(content[article_start:article_start+4000])
