# -*- coding: utf-8 -*-
"""
Daily News Generator
生成 JSON 相关新闻并推送到 GitHub
"""
import os
import re
from datetime import datetime

NEWS_DIR = r'd:\网站开发-json\news'
TODAY = datetime.now().strftime('%B %d, %Y')

NEWS_TEMPLATES = [
    {
        'slug': 'json-schema-evolution-{date}',
        'title': 'JSON Schema Evolution: What Changed in 2025',
        'description': 'Explore the latest updates to JSON Schema specifications and how they impact API development.',
        'category': 'API Technology',
        'read_time': '5-7 min read',
        'content': '''
<h2>The JSON Schema Landscape</h2>
<p>JSON Schema continues to evolve as the standard for defining and validating JSON data structures. Recent updates have brought significant improvements in expressiveness and developer experience.</p>

<h2>Key Updates</h2>
<ul>
<li>Improved handling of conditional schemas</li>
<li>Enhanced reference resolution mechanisms</li>
<li>Better support for OpenAPI integration</li>
<li>Performance optimizations in validators</li>
</ul>

<h2>Impact on API Development</h2>
<p>These changes make it easier to define complex validation rules and improve interoperability between different JSON Schema implementations.</p>

<h2>Getting Started</h2>
<p>Try our JSON Schema Validator to test your schemas against the latest specification.</p>
'''
    },
    {
        'slug': 'streaming-json-parser-{date}',
        'title': 'Streaming JSON Parsing: Handle Large Files Efficiently',
        'description': 'Learn how to parse large JSON files without loading them entirely into memory using streaming techniques.',
        'category': 'Performance',
        'read_time': '6-8 min read',
        'content': '''
<h2>The Challenge of Large JSON Files</h2>
<p>Traditional JSON parsers load entire files into memory, which becomes problematic with multi-gigabyte datasets. Streaming parsers solve this by processing data incrementally.</p>

<h2>Streaming Approaches</h2>
<h3>1. ndjson (Newline Delimited JSON)</h3>
<p>Each line is a valid JSON object, making it easy to process with simple line-by-line reading.</p>

<h3>2. JSON Lines</h3>
<p>A practical format for storing structured data that may be processed one record at a time.</p>

<h3>3. Partial Parsing</h3>
<p>Parse only what you need, ignoring the rest of the document.</p>

<h2>Use Cases</h2>
<ul>
<li>Log processing and analysis</li>
<li>Data pipeline ETL operations</li>
<li>Real-time data streaming</li>
<li>Memory-constrained environments</li>
</ul>
'''
    }
]

def generate_news(article):
    """Generate news article HTML"""
    slug = article['slug'].format(date=datetime.now().strftime('%Y-%m-%d'))
    
    article_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="google-site-verification" content="Bq7rq6iKPPDtIQCMjYquCng3eeVG_Ni0tf1bqUQsQ2w" />
    <meta name="description" content="{article['description']}">
    <meta name="author" content="AI JSON - Free JSON Tools for Developers">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://www.aijsons.com/news/{slug}">

    <title>{article['title']} | AI JSON</title>

    <!-- Open Graph -->
    <meta property="og:type" content="article">
    <meta property="og:url" content="https://www.aijsons.com/news/{slug}">
    <meta property="og:title" content="{article['title']}">
    <meta property="og:description" content="{article['description']}">
    <meta property="og:image" content="https://www.aijsons.com/og-image.png">

    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{article['title']}">
    <meta name="twitter:description" content="{article['description']}">
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
        "headline": "{article['title']}",
        "description": "{article['description']}",
        "datePublished": "{TODAY}",
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
                    <a href="/">Home</a> / <a href="/news">News</a> / <span>Article</span>
                </div>
                <div class="article-category cat-development">News</div>
                <h1 class="article-title">{article['title']}</h1>
                <div class="article-meta">
                    <span>Published: {TODAY}</span> · <span>{article['read_time']}</span>
                </div>
            </div>

            <div class="article-body">
                {article['content']}
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
    return slug, article_html

def main():
    print('=' * 50)
    print('Daily News Generator')
    print('=' * 50)
    
    for template in NEWS_TEMPLATES:
        slug, html = generate_news(template)
        article_dir = os.path.join(NEWS_DIR, slug)
        
        if not os.path.exists(article_dir):
            print(f'\\nGenerating: {template["title"]}')
            
            os.makedirs(article_dir, exist_ok=True)
            with open(os.path.join(article_dir, 'index.html'), 'w', encoding='utf-8') as f:
                f.write(html)
            
            print(f'✓ Created: {slug}/index.html')
    
    print('\\n✓ News generated! Run push_to_github.py to publish.')

if __name__ == '__main__':
    main()
