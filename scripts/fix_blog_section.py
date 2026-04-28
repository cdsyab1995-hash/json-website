# -*- coding: utf-8 -*-
"""
重新生成首页文章列表
"""
import os
import re
from datetime import datetime

HOME = r'd:\网站开发-json\index.html'
BLOG_DIR = r'd:\网站开发-json\blog'

# 从博客目录读取文章信息
def get_blog_articles():
    articles = []
    for item in os.listdir(BLOG_DIR):
        path = os.path.join(BLOG_DIR, item)
        if os.path.isdir(path):
            index_file = os.path.join(path, 'index.html')
            if os.path.exists(index_file):
                with open(index_file, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                
                # 提取标题
                title_match = re.search(r'<h1[^>]*class="article-title"[^>]*>([^<]+)</h1>', content)
                if not title_match:
                    title_match = re.search(r'<title>([^|]+)', content)
                
                title = title_match.group(1).strip() if title_match else item
                
                # 提取日期
                date_match = re.search(r'Published:\s*([^<·]+)', content)
                date = date_match.group(1).strip() if date_match else '2026-04-01'
                
                articles.append({
                    'slug': item,
                    'title': title,
                    'date': date,
                    'url': f'/blog/{item}'
                })
    
    # 按日期排序
    articles.sort(key=lambda x: x['date'], reverse=True)
    return articles[:8]  # 最近 8 篇

def generate_article_card(article):
    date_short = article['date'][:10] if len(article['date']) > 10 else article['date']
    return f'''<article class="feature-card" style="text-align: left;">
    <span class="article-date-label">{date_short}</span>
    <h3 class="article-card-title">{article['title']}</h3>
    <p class="article-card-excerpt">Learn more about this topic in our comprehensive guide.</p>
    <a href="{article['url']}" class="article-read-link">Read the full article →</a>
</article>'''

def main():
    # 读取当前首页
    with open(HOME, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 获取文章列表
    articles = get_blog_articles()
    print(f'Found {len(articles)} articles')
    
    # 生成新的文章 HTML
    articles_html = '\n    '.join([generate_article_card(a) for a in articles])
    
    # 替换文章区
    # 找到 Latest Articles section
    pattern = r'(<section class="tool-area mt-lg">\s*<h2 class="section-label[^"]*">Latest Articles</h2>\s*<div class="feature-grid">)([\s\S]*?)(</div>\s*</section>)'
    
    replacement = rf'\1\n    {articles_html}\n    \3'
    
    new_content = re.sub(pattern, replacement, content)
    
    if new_content != content:
        with open(HOME, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print('Updated index.html with new article section')
    else:
        print('No changes made')

if __name__ == '__main__':
    main()
