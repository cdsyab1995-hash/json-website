# -*- coding: utf-8 -*-
import re, os

BLOG_FILE = r'd:\网站开发-json\pages\blog.html'

with open(BLOG_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Extract the featured article (full content)
start = content.find('<article id="ai-daily-20260418"')
end = content.find('</article>', start) + len('</article>')
featured_article = content[start:end]

# 2. Extract 3 preview article cards
remaining = content[end:]
article_cards = re.findall(r'<article class="article-card">[\s\S]*?</article>', remaining)
print(f'Featured article: {len(featured_article)} chars')
print(f'Preview cards: {len(article_cards)} cards')

# ==================== BUILD NEW BLOG.HTML ====================
new_blog = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="google-site-verification" content="Bq7rq6iKPPDtIQCMjYquCng3eeVG_Ni0tf1bqUQsQ2w" />
    <meta name="description" content="JSON Tech Blog - Expert insights on JSON in modern development, AI workflows, API design, and structured data practices for developers worldwide.">
    <meta name="author" content="AI JSON - Free JSON Tools for Developers">
    <meta name="robots" content="index, follow">

    <title>JSON Tech Blog - API Design, AI Workflows & Best Practices | AI JSON</title>
    <link rel="canonical" href="https://www.aijsons.com/pages/blog.html">

    <!-- Open Graph -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://www.aijsons.com/pages/blog.html">
    <meta property="og:title" content="JSON Tech Blog - API Design, AI Workflows & Best Practices">
    <meta property="og:description" content="Expert insights on JSON in modern development, AI workflows, API design, and structured data practices.">

    <!-- Fonts - sync loading -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&display=swap">

    <!-- Main Stylesheet -->
    <link rel="stylesheet" href="../css/styles.css">
</head>
<body>
    <!-- NAVBAR -->
    <nav class="navbar">
        <a href="../index.html" class="navbar-brand">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                <polyline points="14 2 14 8 20 8"></polyline>
                <line x1="16" y1="13" x2="8" y2="13"></line>
                <line x1="16" y1="17" x2="8" y2="17"></line>
            </svg>
            AI JSON
        </a>
        <button class="menu-toggle" aria-label="Menu">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <line x1="3" y1="12" x2="21" y2="12"></line>
                <line x1="3" y1="6" x2="21" y2="6"></line>
                <line x1="3" y1="18" x2="21" y2="18"></line>
            </svg>
        </button>
        <div class="navbar-links">
            <a href="../index.html" class="nav-link">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path>
                    <polyline points="9 22 9 12 15 12 15 22"></polyline>
                </svg>
                Home
            </a>
            <!-- Tools Dropdown -->
            <div class="nav-dropdown">
                <a href="#" class="nav-link nav-dropdown-toggle">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <rect x="3" y="3" width="7" height="7"></rect>
                        <rect x="14" y="3" width="7" height="7"></rect>
                        <rect x="14" y="14" width="7" height="7"></rect>
                        <rect x="3" y="14" width="7" height="7"></rect>
                    </svg>
                    Tools
                </a>
                <div class="nav-dropdown-menu">
<div class="nav-dropdown-menu-box">
                    <a href="format.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="4 7 4 4 20 4 20 7"></polyline><line x1="9" y1="20" x2="15" y2="20"></line><line x1="12" y1="4" x2="12" y2="20"></line></svg> Format</a>
                    <a href="escape.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg> Escape</a>
                    <a href="extract.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg> Extract</a>
                    <a href="sort.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="5" x2="12" y2="19"></line><polyline points="19 12 12 19 5 12"></polyline></svg> Sort</a>
                    <a href="clean.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"></path></svg> Clean</a>
                    <a href="xml.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline></svg> XML</a>
                    <a href="yaml.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4l4 16 4-16"></path><path d="M12 4l4 16"></path></svg> YAML</a>
                    <a href="viewer.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path><circle cx="12" cy="12" r="3"></circle></svg> Viewer</a>
                    <a href="json2csv.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="8" y1="13" x2="16" y2="13"></line><line x1="8" y1="17" x2="16" y2="17"></line></svg> CSV</a>
                    <a href="compare.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 3h5v5"></path><path d="M8 3H3v5"></path><path d="M21 3l-7 7"></path><path d="M3 3l7 7"></path><path d="M16 21h5v-5"></path><path d="M8 21H3v-5"></path><path d="M21 21l-7-7"></path><path d="M3 21l7-7"></path></svg> Compare</a>
                    <a href="regex-tester.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v4M12 18v4M4.93 4.93l2.83 2.83M16.24 16.24l2.83 2.83M2 12h4M18 12h4M4.93 19.07l2.83-2.83M16.24 7.76l2.83-2.83"></path></svg> Regex</a>
                    <a href="base64.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="8" y1="12" x2="16" y2="12"></line></svg> Base64</a>
                    <a href="url-encoder.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path></svg> URL Encoder</a>
                    <a href="csv-to-excel.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="3" y1="9" x2="21" y2="9"></line><line x1="9" y1="21" x2="9" y2="9"></line></svg> Excel</a>
                    <a href="excel-remove-duplicates.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg> Remove Duplicates</a>
                    <a href="merge-csv.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 16v4a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h2"></path><path d="M8 12v4a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2v-4a2 2 0 0 0-2-2H10a2 2 0 0 0-2 2"></path></svg> Merge CSV</a>
                    <a href="batch-file-renamer.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path></svg> Batch Rename</a>
                    <a href="pdf-split.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="12" y1="18" x2="12" y2="12"></line><line x1="9" y1="15" x2="15" y2="15"></line></svg> PDF Split</a>
                    <a href="timestamp-converter.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg> Timestamp</a>
                    <a href="css-minifier.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="4 17 10 11 4 5"></polyline><line x1="12" y1="19" x2="20" y2="19"></line></svg> CSS Minifier</a>
                    <a href="html-encoder.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg> HTML Encoder</a>
                </div>
</div>
            </div>
            <a href="blog.html" class="nav-link active">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path>
                    <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path>
                </svg>
                Tutorial
            </a>
            <a href="best-practices.html" class="nav-link">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
                    <polyline points="22 4 12 14.01 9 11.01"></polyline>
                </svg>
                Practices
            </a>
            <a href="news.html" class="nav-link">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"></path>
                </svg>
                News
            </a>
            <a href="about.html" class="nav-link">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <circle cx="12" cy="12" r="10"></circle>
                    <line x1="12" y1="16" x2="12" y2="12"></line>
                    <line x1="12" y1="8" x2="12.01" y2="8"></line>
                </svg>
                About
            </a>
            <a href="changelog.html" class="nav-link">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <circle cx="12" cy="12" r="10"></circle>
                    <polyline points="12 6 12 12 16 14"></polyline>
                </svg>
                Changelog
            </a>
        </div>
    </nav>

    <main class="main-container">
        <!-- Page Header -->
        <div class="page-header text-center">
            <h1 class="page-title">JSON Tech Blog</h1>
            <p class="page-description">Expert insights on JSON in modern development, AI workflows, API design, and structured data</p>
            <div class="breadcrumb">
                <a href="../index.html">Home</a> / <span>Blog</span>
            </div>
        </div>

        <!-- Featured Article -->
        <section>
            <h2 class="section-title">Latest Article</h2>
            ''' + featured_article + '''
        </section>

        <!-- More Articles -->
        <section>
            <h2 class="section-title">More Articles</h2>
            <div class="articles-grid">
'''

for card in article_cards:
    new_blog += card + '\n'

new_blog += '''            </div>
        </section>

        <!-- JSON Templates Section -->
        <section>
            <h2 class="section-title">Common JSON Templates</h2>
            <p class="section-description">Ready-to-use JSON structures for common development scenarios. Copy and adapt for your projects.</p>
            <div class="templates-grid">
                <div class="template-card">
                    <h3>User Profile</h3>
                    <pre class="code-block"><code>{
  "id": "usr_12345",
  "username": "jdoe",
  "email": "jdoe@example.com",
  "profile": {
    "firstName": "John",
    "lastName": "Doe",
    "avatar": "https://example.com/avatars/jdoe.jpg",
    "bio": "Software Engineer"
  },
  "roles": ["user", "admin"],
  "createdAt": "2024-01-15T08:30:00Z",
  "verified": true
}</code></pre>
                </div>
                <div class="template-card">
                    <h3>API Response</h3>
                    <pre class="code-block"><code>{
  "success": true,
  "data": {
    "items": [],
    "total": 100,
    "page": 1,
    "perPage": 20
  },
  "meta": {
    "requestId": "req_abc123",
    "timestamp": "2024-01-15T08:30:00Z"
  }
}</code></pre>
                </div>
                <div class="template-card">
                    <h3>API Error</h3>
                    <pre class="code-block"><code>{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input data",
    "details": [
      {"field": "email", "issue": "invalid format"},
      {"field": "age", "issue": "must be positive"}
    ]
  },
  "meta": {
    "requestId": "req_abc123",
    "timestamp": "2024-01-15T08:30:00Z"
  }
}</code></pre>
                </div>
                <div class="template-card">
                    <h3>Configuration</h3>
                    <pre class="code-block"><code>{
  "app": {
    "name": "MyApp",
    "version": "2.0.0",
    "env": "production"
  },
  "features": {
    "darkMode": true,
    "notifications": true,
    "analytics": false
  },
  "limits": {
    "maxFileSize": 10485760,
    "rateLimit": 1000
  }
}</code></pre>
                </div>
                <div class="template-card">
                    <h3>E-commerce Product</h3>
                    <pre class="code-block"><code>{
  "id": "prod_789",
  "name": "Wireless Headphones",
  "price": 79.99,
  "currency": "USD",
  "category": "electronics",
  "tags": ["audio", "wireless", "bluetooth"],
  "inventory": {
    "inStock": true,
    "quantity": 234
  },
  "images": ["https://..."]
}</code></pre>
                </div>
                <div class="template-card">
                    <h3>Webhook Event</h3>
                    <pre class="code-block"><code>{
  "event": "user.created",
  "timestamp": "2024-01-15T08:30:00Z",
  "data": {
    "userId": "usr_12345",
    "email": "jdoe@example.com"
  },
  "signature": "sha256=..."
}</code></pre>
                </div>
            </div>
        </section>

        <!-- JSON Datasets Section -->
        <section>
            <h2 class="section-title">Sample JSON Datasets</h2>
            <p class="section-description">Real-world JSON data samples for testing, development, and learning purposes.</p>
            <div class="datasets-list">
                <div class="dataset-card">
                    <h3>JSONPlaceholder API</h3>
                    <p>Free fake API for testing and prototyping. Provides endpoints for posts, comments, users, photos, and more.</p>
                    <a href="https://jsonplaceholder.typicode.com" target="_blank" rel="noopener" class="dataset-link">jsonplaceholder.typicode.com →</a>
                </div>
                <div class="dataset-card">
                    <h3>REST Countries API</h3>
                    <p>Complete data about countries including names, capitals, currencies, languages, regions, and flags.</p>
                    <a href="https://restcountries.com" target="_blank" rel="noopener" class="dataset-link">restcountries.com →</a>
                </div>
                <div class="dataset-card">
                    <h3>GitHub Gists API</h3>
                    <p>Explore public Gists to see how developers structure their JSON data in real projects.</p>
                    <a href="https://api.github.com/gists/public" target="_blank" rel="noopener" class="dataset-link">api.github.com/gists →</a>
                </div>
            </div>
        </section>
    </main>

    <!-- Footer -->
    <footer class="footer">
        <p>AI JSON - Free JSON Tools for Developers</p>
        <p style="margin-top: 0.5rem; font-size: 0.875rem;">
            <a href="about.html">About</a> | <a href="changelog.html">Changelog</a> | <a href="../index.html">Home</a>
        </p>
    </footer>
</body>
</html>'''

# Write the new blog.html
with open(BLOG_FILE, 'w', encoding='utf-8') as f:
    f.write(new_blog)

print(f'Written: {len(new_blog)} chars')
