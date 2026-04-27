# -*- coding: utf-8 -*-
"""
修复 news 文章格式 - 统一为和 blog 文章一样的结构
"""
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

NEWS_DIR = r'd:\网站开发-json\news'

def fix_news_article(filepath):
    """修复单个 news 文章的格式"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 检查是否已经是新格式
    if 'article-header' in content and 'article-body' in content:
        print(f'  [SKIP] Already fixed: {os.path.basename(os.path.dirname(filepath))}')
        return
    
    # 提取标题
    title_match = re.search(r'<h1 class="page-title">(.*?)</h1>', content)
    title = title_match.group(1) if title_match else 'Article'
    
    # 提取面包屑
    breadcrumb_match = re.search(r'<div class="breadcrumb">(.*?)</div>', content)
    breadcrumb = breadcrumb_match.group(1) if breadcrumb_match else '<a href="/">Home</a> / <a href="/news">News</a> / <span>Article</span>'
    
    # 提取日期 - 更精确的匹配
    date_match = re.search(r'Published:\s*([^<·|]+)', content)
    date = date_match.group(1).strip() if date_match else ''
    
    # 提取阅读时间
    readtime_match = re.search(r'(\d+-\d+\s*min read)', content)
    readtime = readtime_match.group(1) if readtime_match else '5 min read'
    
    # 提取文章正文
    body_match = re.search(r'<article class="blog-content">(.*?)</article>', content, re.DOTALL)
    body = body_match.group(1) if body_match else ''
    
    # 提取 slug
    slug_match = re.search(r'/news/([^"]+)', content)
    slug = slug_match.group(1) if slug_match else 'article'
    
    # 构建新格式
    new_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="google-site-verification" content="Bq7rq6iKPPDtIQCMjYquCng3eeVG_Ni0tf1bqUQsQ2w" />
    <meta name="description" content="Latest JSON news, API updates, and developer tools insights for developers worldwide.">
    <meta name="author" content="AI JSON - Free JSON Tools for Developers">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://www.aijsons.com/news/{slug}">

    <title>{title} | AI JSON</title>

    <!-- Open Graph -->
    <meta property="og:type" content="article">
    <meta property="og:url" content="https://www.aijsons.com/news/{slug}">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="Latest JSON news and developer tools updates.">
    <meta property="og:image" content="https://www.aijsons.com/og-image.png">

    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title}">
    <meta name="twitter:description" content="Latest JSON news and developer tools updates.">
    <meta name="twitter:image" content="https://www.aijsons.com/og-image.png">

    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap">

    <!-- Styles -->
    <link rel="stylesheet" href="/css/styles.css">

    <!-- JSON-LD -->
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": "{title}",
        "description": "Latest JSON news and developer tools updates.",
        "datePublished": "{date}",
        "author": {{"@type": "Organization", "name": "AI JSON"}},
        "publisher": {{"@type": "Organization", "name": "AI JSON", "url": "https://www.aijsons.com"}},
        "url": "https://www.aijsons.com/news/{slug}",
        "articleSection": "News"
    }}
    </script>
<script src="/js/navbar.js"></script>
</head>
<body>
    <div id="navbar-placeholder"></div>

    <main class="main-container">
        <article>
            <div class="article-header">
                <div class="breadcrumb">
                    {breadcrumb}
                </div>
                <div class="article-category cat-development">News</div>
                <h1 class="article-title">{title}</h1>
                <div class="article-meta">
                    <span>Published: {date}</span> · <span>{readtime}</span>
                </div>
            </div>

            <div class="article-body">
                {body}
            </div>
        </article>

        <section class="related-tools-section">
            <h2>Try Our JSON Tools</h2>
            <div class="related-tools-grid">
                <a href="/tools/json-formatter" class="related-tool-card">
                    <strong>JSON Formatter</strong>
                    <span>Format and validate JSON instantly</span>
                </a>
                <a href="/tools/json-validator" class="related-tool-card">
                    <strong>JSON Validator</strong>
                    <span>Validate JSON syntax and structure</span>
                </a>
                <a href="/tools/json-schema-validator" class="related-tool-card">
                    <strong>JSON Schema Validator</strong>
                    <span>Validate JSON against JSON Schema</span>
                </a>
            </div>
        </section>
    </main>

    <!-- Footer -->
    <footer class="footer">
        <p>AI JSON - Free JSON Tools for Developers</p>
        <p class="text-sm mt-sm">
            <a href="/about">About</a> | <a href="/changelog">Changelog</a> | <a href="/">Home</a>
        </p>
    </footer>

    <script src="/js/app.js" defer></script>
</body>
</html>'''

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_html)
    
    print(f'  [FIXED] {os.path.basename(os.path.dirname(filepath))}')

def main():
    print('=' * 50)
    print('Fixing News Article Format')
    print('=' * 50)
    
    fixed_count = 0
    for root, dirs, files in os.walk(NEWS_DIR):
        for file in files:
            if file == 'index.html':
                filepath = os.path.join(root, file)
                # 跳过 news/index.html (主索引页)
                if filepath != os.path.join(NEWS_DIR, 'index.html'):
                    print(f'\nProcessing: {os.path.basename(root)}')
                    fix_news_article(filepath)
                    fixed_count += 1
    
    print('\n' + '=' * 50)
    print(f'Fixed {fixed_count} news articles!')
    print('=' * 50)

if __name__ == '__main__':
    main()
