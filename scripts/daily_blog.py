# -*- coding: utf-8 -*-
"""
Daily Blog Article Generator
生成 JSON 相关博客文章并推送到 GitHub
"""
import os
import re
import json
from datetime import datetime

BLOG_DIR = r'd:\网站开发-json\blog'
SITE_URL = 'https://www.aijsons.com'
TODAY = datetime.now().strftime('%B %d, %Y')

TOPICS = [
    {
        'slug': 'jsonpath-vs-jsonata-2026',
        'title': 'JSONPath vs JSONata: Choosing the Right Query Language',
        'description': 'Compare JSONPath and JSONata for JSON data querying. Learn syntax differences, use cases, and performance considerations.',
        'keywords': 'JSONPath, JSONata, JSON query, JSONPath vs JSONata',
        'category': 'Development',
        'category_class': 'cat-development',
        'read_time': '8-10 min read',
        'content': '''
<h2>Introduction</h2>
<p>When working with JSON data, you often need to extract specific values or transform data structures. Two popular query languages have emerged: JSONPath and JSONata. But which one should you choose?</p>

<h2>JSONPath: The XPath for JSON</h2>
<p>JSONPath is inspired by XPath and provides a familiar syntax for those who have worked with XML. It uses dot and bracket notation:</p>

<pre><code>$.store.book[0].title
$.store.book[*].author
$..author</code></pre>

<h2>JSONata: More Than Just Querying</h2>
<p>JSONata goes beyond simple querying by offering a complete expression language with transformations, aggregations, and function composition:</p>

<pre><code>$.store.book{"title": title, "price": price} 
| $average(price)</code></pre>

<h2>Key Differences</h2>
<table>
<tr><th>Feature</th><th>JSONPath</th><th>JSONata</th></tr>
<tr><td>Learning Curve</td><td>Easier for XPath users</td><td>Steeper but more powerful</td></tr>
<tr><td>Data Transformation</td><td>Limited</td><td>Full transformation support</td></tr>
<tr><td>Functions</td><td>Basic filtering</td><td>Rich built-in functions</td></tr>
<tr><td>Performance</td><td>Fast for simple queries</td><td>Optimized for complex expressions</td></tr>
</table>

<h2>When to Use Each</h2>
<p><strong>Use JSONPath when:</strong></p>
<ul>
<li>You need simple data extraction</li>
<li>You're already familiar with XPath</li>
<li>Performance is critical for large datasets</li>
</ul>

<p><strong>Use JSONata when:</strong></p>
<ul>
<li>You need data transformation</li>
<li>You want to perform aggregations</li>
<li>You prefer a more expressive syntax</li>
</ul>

<h2>Conclusion</h2>
<p>Both JSONPath and JSONata are powerful tools for working with JSON data. JSONPath excels at simple extraction, while JSONata provides a more complete solution for transformation and aggregation needs. Try both with our free JSON tools!</p>
'''
    },
    {
        'slug': 'jwt-security-best-practices-2026',
        'title': 'JWT Security Best Practices for Modern Applications',
        'description': 'Essential security practices for implementing JWT tokens in your applications. Learn about signing, validation, and common vulnerabilities.',
        'keywords': 'JWT security, JSON Web Token, authentication, token security',
        'category': 'Security',
        'category_class': 'cat-security',
        'read_time': '10-12 min read',
        'content': '''
<h2>Introduction</h2>
<p>JSON Web Tokens (JWT) are widely used for authentication and authorization, but improper implementation can lead to security vulnerabilities. This guide covers essential security best practices.</p>

<h2>1. Always Use HTTPS</h2>
<p>Never transmit tokens over plain HTTP. Always use HTTPS to prevent token interception via man-in-the-middle attacks.</p>

<h2>2. Choose Strong Signing Algorithms</h2>
<p>Use RS256 (RSA Signature with SHA-256) instead of HS256 for most applications. Avoid using 'none' algorithm.</p>

<pre><code>// Good: RS256
{
  "alg": "RS256",
  "typ": "JWT"
}

// Avoid: HS256 in distributed systems
// Avoid: "none" algorithm
</code></pre>

<h2>3. Validate All Claims</h2>
<p>Always validate these claims:</p>
<ul>
<li><code>exp</code> - Expiration time</li>
<li><code>iat</code> - Issued at time</li>
<li><code>iss</code> - Issuer</li>
<li><code>aud</code> - Audience</li>
</ul>

<h2>4. Keep Tokens Short-Lived</h2>
<p>Use short expiration times (15-60 minutes) and implement refresh tokens for extended sessions.</p>

<h2>5. Store Tokens Securely</h2>
<p>Prefer HttpOnly cookies over localStorage to prevent XSS attacks. Never store tokens in URL parameters.</p>

<h2>Conclusion</h2>
<p>Security is critical when implementing JWT authentication. Follow these best practices to protect your applications and users.</p>
'''
    }
]

def get_reading_time(content):
    """Calculate reading time based on word count"""
    words = len(re.sub(r'<[^>]+>', '', content).split())
    minutes = max(1, words // 200)
    return f'{minutes}-{minutes + 2} min read'

def generate_article(article):
    """Generate article HTML"""
    read_time = get_reading_time(article['content'])
    
    article_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="google-site-verification" content="Bq7rq6iKPPDtIQCMjYquCng3eeVG_Ni0tf1bqUQsQ2w" />
    <meta name="description" content="{article['description']}">
    <meta name="keywords" content="{article['keywords']}">
    <meta name="author" content="AI JSON - Free JSON Tools for Developers">
    <meta name="robots" content="index, follow">

    <title>{article['title']} | AI JSON</title>
    <link rel="canonical" href="https://www.aijsons.com/blog/{article['slug']}">

    <!-- Open Graph -->
    <meta property="og:type" content="article">
    <meta property="og:url" content="https://www.aijsons.com/blog/{article['slug']}">
    <meta property="og:title" content="{article['title']}">
    <meta property="og:description" content="{article['description']}">
    <meta property="og:image" content="https://www.aijsons.com/og-image.png">

    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{article['title']}">
    <meta name="twitter:description" content="{article['description']}">
    <meta name="twitter:image" content="https://www.aijsons.com/og-image.png">

    <meta property="article:published_time" content="{TODAY}">
    <meta property="article:section" content="{article['category']}">

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
        "url": "https://www.aijsons.com/blog/{article['slug']}",
        "articleSection": "{article['category']}"
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
                    <a href="/">Home</a> / <a href="/blog">Blog</a> / <span>Article</span>
                </div>
                <div class="article-category {article['category_class']}">{article['category']}</div>
                <h1 class="article-title">{article['title']}</h1>
                <div class="article-meta">
                    <span>Published: {TODAY}</span> · <span>{read_time}</span>
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
                    <span>Format and validate JSON</span>
                </a>
                <a href="/tools/json-viewer" class="related-tool-card">
                    <strong>JSON Viewer</strong>
                    <span>Visualize JSON as tree</span>
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
    return article_html

def main():
    print('=' * 50)
    print('Daily Blog Article Generator')
    print('=' * 50)
    
    # Find next topic
    for topic in TOPICS:
        article_dir = os.path.join(BLOG_DIR, topic['slug'])
        if not os.path.exists(article_dir):
            print(f'\\nGenerating: {topic["title"]}')
            
            # Create directory
            os.makedirs(article_dir, exist_ok=True)
            
            # Generate article
            html = generate_article(topic)
            with open(os.path.join(article_dir, 'index.html'), 'w', encoding='utf-8') as f:
                f.write(html)
            
            print(f'✓ Created: {topic["slug"]}/index.html')
            print('\\n✓ Article generated! Run push_to_github.py to publish.')
            return
    
    print('\\nAll topics already exist!')

if __name__ == '__main__':
    main()
