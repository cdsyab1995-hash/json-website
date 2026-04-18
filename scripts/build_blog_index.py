# -*- coding: utf-8 -*-
"""
Build blog multi-page architecture:
1. Create pages/blog/index.html - the blog homepage (article catalog)
2. Enhance all existing articles with proper nav, breadcrumb, related articles
"""
import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')

BLOG_DIR = r'd:\网站开发-json\pages\blog'
INDEX_FILE = r'd:\网站开发-json\pages\blog\index.html'

# ==================== READ ALL ARTICLES ====================
articles = []
blog_files = [f for f in os.listdir(BLOG_DIR) if f.endswith('.html') and f != 'index.html']

for f in blog_files:
    path = os.path.join(BLOG_DIR, f)
    with open(path, 'r', encoding='utf-8') as fp:
        content = fp.read()

    title = re.search(r'<title>(.*?)</title>', content)
    title = title.group(1) if title else 'Untitled'

    desc = re.search(r'<meta name="description" content="(.*?)"', content)
    desc = desc.group(1) if desc else ''

    category_m = re.search(r'"articleSection"\s*:\s*"([^"]+)"', content)
    category = category_m.group(1) if category_m else 'Development'

    date_m = re.search(r'"datePublished"\s*:\s*"([^"]+)"', content)
    date = date_m.group(1) if date_m else '2026-04-01'
    date_disp = re.search(r'(\d{4})-(\d{2})-(\d{2})', date)
    date_display = date_disp.group(0) if date_disp else date[:10]

    # Reading time
    text = re.sub(r'<[^>]+>', '', content)
    words = len(text)
    read_time = f'{max(1, words // 200)}-{min(10, (words // 200) + 2)} min'

    # Extract first heading from article body
    h_m = re.search(r'<h[12][^>]*>(.*?)</h[12]>', content)
    headline = h_m.group(1) if h_m else title

    articles.append({
        'file': f,
        'title': title,
        'desc': desc,
        'category': category,
        'date': date_display,
        'read_time': read_time,
        'headline': headline,
    })

# Sort by date descending
articles.sort(key=lambda x: x['date'], reverse=True)
print(f'Loaded {len(articles)} articles')

# ==================== BUILD BLOG/INDEX.HTML ====================
featured = articles[0]
rest = articles[1:]

article_cards_html = ''
for i, a in enumerate(rest):
    cat_class = a['category'].lower().replace(' ', '-')
    article_cards_html += f'''                <article class="article-card">
                    <div class="article-category cat-{cat_class}">{a['category']}</div>
                    <h3><a href="{a['file']}">{a['headline']}</a></h3>
                    <p class="article-excerpt">{a['desc'][:150]}...</p>
                    <div class="article-meta">
                        <span>{a['date']}</span> |
                        <span>{a['read_time']} read</span>
                    </div>
                    <a href="{a['file']}" class="read-more">Read article →</a>
                </article>
'''

featured_cat = featured['category'].lower().replace(' ', '-')
featured_html = f'''<article class="article-card featured-article">
                    <div class="article-category cat-{featured_cat}">{featured['category']}</div>
                    <h2><a href="{featured['file']}">{featured['headline']}</a></h2>
                    <p class="article-excerpt">{featured['desc'][:200]}...</p>
                    <div class="article-meta">
                        <span>{featured['date']}</span> |
                        <span>{featured['read_time']} read</span>
                    </div>
                    <a href="{featured['file']}" class="read-more">Read full article →</a>
                </article>'''

blog_index_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="google-site-verification" content="Bq7rq6iKPPDtIQCMjYquCng3eeVG_Ni0tf1bqUQsQ2w" />
    <meta name="description" content="JSON Tech Blog - Expert articles on JSON in AI workflows, API design, JSON Schema, parsing performance, and modern development practices.">
    <meta name="author" content="AI JSON - Free JSON Tools for Developers">
    <meta name="robots" content="index, follow">

    <title>JSON Tech Blog - API Design, AI Workflows & Best Practices | AI JSON</title>
    <link rel="canonical" href="https://www.aijsons.com/pages/blog/index.html">

    <!-- Open Graph -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://www.aijsons.com/pages/blog/index.html">
    <meta property="og:title" content="JSON Tech Blog - API Design, AI Workflows & Best Practices">
    <meta property="og:description" content="Expert articles on JSON in AI workflows, API design, JSON Schema, parsing performance, and modern development.">

    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&display=swap">

    <!-- Styles -->
    <link rel="stylesheet" href="../../css/styles.css">

    <!-- JSON-LD -->
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "Blog",
        "name": "AI JSON Tech Blog",
        "url": "https://www.aijsons.com/pages/blog/index.html",
        "description": "Expert articles on JSON in AI workflows, API design, and modern development",
        "publisher": {{
            "@type": "Organization",
            "name": "AI JSON",
            "url": "https://www.aijsons.com"
        }}
    }}
    </script>
</head>
<body>
    <!-- NAVBAR -->
    <nav class="navbar">
        <a href="../../index.html" class="navbar-brand">
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
            <a href="../../index.html" class="nav-link">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path>
                    <polyline points="9 22 9 12 15 12 15 22"></polyline>
                </svg>
                Home
            </a>
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
                    <a href="../format.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="4 7 4 4 20 4 20 7"></polyline><line x1="9" y1="20" x2="15" y2="20"></line><line x1="12" y1="4" x2="12" y2="20"></line></svg> Format</a>
                    <a href="../escape.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg> Escape</a>
                    <a href="../extract.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg> Extract</a>
                    <a href="../sort.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="5" x2="12" y2="19"></line><polyline points="19 12 12 19 5 12"></polyline></svg> Sort</a>
                    <a href="../clean.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"></path></svg> Clean</a>
                    <a href="../xml.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline></svg> XML</a>
                    <a href="../yaml.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4l4 16 4-16"></path><path d="M12 4l4 16"></path></svg> YAML</a>
                    <a href="../viewer.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path><circle cx="12" cy="12" r="3"></circle></svg> Viewer</a>
                    <a href="../json2csv.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="8" y1="13" x2="16" y2="13"></line><line x1="8" y1="17" x2="16" y2="17"></line></svg> CSV</a>
                    <a href="../compare.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 3h5v5"></path><path d="M8 3H3v5"></path><path d="M21 3l-7 7"></path><path d="M3 3l7 7"></path><path d="M16 21h5v-5"></path><path d="M8 21H3v-5"></path><path d="M21 21l-7-7"></path><path d="M3 21l7-7"></path></svg> Compare</a>
                    <a href="../regex-tester.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v4M12 18v4M4.93 4.93l2.83 2.83M16.24 16.24l2.83 2.83M2 12h4M18 12h4M4.93 19.07l2.83-2.83M16.24 7.76l2.83-2.83"></path></svg> Regex</a>
                    <a href="../base64.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="8" y1="12" x2="16" y2="12"></line></svg> Base64</a>
                    <a href="../url-encoder.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path></svg> URL Encoder</a>
                    <a href="../csv-to-excel.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="3" y1="9" x2="21" y2="9"></line><line x1="9" y1="21" x2="9" y2="9"></line></svg> Excel</a>
                    <a href="../excel-remove-duplicates.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg> Remove Duplicates</a>
                    <a href="../merge-csv.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 16v4a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h2"></path><path d="M8 12v4a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2v-4a2 2 0 0 0-2-2H10a2 2 0 0 0-2 2"></path></svg> Merge CSV</a>
                    <a href="../batch-file-renamer.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path></svg> Batch Rename</a>
                    <a href="../pdf-split.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="12" y1="18" x2="12" y2="12"></line><line x1="9" y1="15" x2="15" y2="15"></line></svg> PDF Split</a>
                    <a href="../timestamp-converter.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg> Timestamp</a>
                    <a href="../css-minifier.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="4 17 10 11 4 5"></polyline><line x1="12" y1="19" x2="20" y2="19"></line></svg> CSS Minifier</a>
                    <a href="../html-encoder.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg> HTML Encoder</a>
                </div>
</div>
            </div>
            <a href="index.html" class="nav-link active">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path>
                    <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path>
                </svg>
                Blog
            </a>
            <a href="../best-practices.html" class="nav-link">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
                    <polyline points="22 4 12 14.01 9 11.01"></polyline>
                </svg>
                Practices
            </a>
            <a href="../news.html" class="nav-link">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"></path>
                </svg>
                News
            </a>
            <a href="../about.html" class="nav-link">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <circle cx="12" cy="12" r="10"></circle>
                    <line x1="12" y1="16" x2="12" y2="12"></line>
                    <line x1="12" y1="8" x2="12.01" y2="8"></line>
                </svg>
                About
            </a>
            <a href="../changelog.html" class="nav-link">
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
            <p class="page-description">In-depth articles on JSON in modern development — API design, AI workflows, Schema validation, parsing performance, and more</p>
            <div class="breadcrumb">
                <a href="../../index.html">Home</a> / <span>Blog</span>
            </div>
        </div>

        <!-- Featured Article -->
        <section>
            <h2 class="section-title">Latest Article</h2>
            {featured_html}
        </section>

        <!-- All Articles Grid -->
        <section>
            <h2 class="section-title">All Articles</h2>
            <div class="articles-grid">
{article_cards_html}
            </div>
        </section>

        <!-- JSON Templates -->
        <section>
            <h2 class="section-title">Common JSON Templates</h2>
            <p class="section-description">Ready-to-use JSON structures for common development scenarios.</p>
            <div class="templates-grid">
                <div class="template-card">
                    <h3>API Response</h3>
                    <pre class="code-block"><code>{{
  "success": true,
  "data": {{ "items": [], "total": 100, "page": 1 }},
  "meta": {{ "requestId": "req_abc", "timestamp": "2024-01-15T08:30:00Z" }}
}}</code></pre>
                </div>
                <div class="template-card">
                    <h3>User Profile</h3>
                    <pre class="code-block"><code>{{
  "id": "usr_123",
  "username": "jdoe",
  "email": "jdoe@example.com",
  "profile": {{ "firstName": "John", "lastName": "Doe" }},
  "roles": ["user"],
  "createdAt": "2024-01-15T08:30:00Z"
}}</code></pre>
                </div>
                <div class="template-card">
                    <h3>API Error</h3>
                    <pre class="code-block"><code>{{
  "success": false,
  "error": {{
    "code": "VALIDATION_ERROR",
    "message": "Invalid input",
    "details": [{{"field": "email", "issue": "invalid"}}]
  }}
}}</code></pre>
                </div>
                <div class="template-card">
                    <h3>Webhook Event</h3>
                    <pre class="code-block"><code>{{
  "event": "user.created",
  "timestamp": "2024-01-15T08:30:00Z",
  "data": {{ "userId": "usr_123" }},
  "signature": "sha256=..."
}}</code></pre>
                </div>
            </div>
        </section>
    </main>

    <!-- Footer -->
    <footer class="footer">
        <p>AI JSON - Free JSON Tools for Developers</p>
        <p style="margin-top: 0.5rem; font-size: 0.875rem;">
            <a href="../about.html">About</a> | <a href="../changelog.html">Changelog</a> | <a href="../../index.html">Home</a>
        </p>
    </footer>
</body>
</html>'''

with open(INDEX_FILE, 'w', encoding='utf-8') as f:
    f.write(blog_index_html)
print(f'Written: blog/index.html ({len(blog_index_html)} chars)')

# ==================== ENHANCE ALL ARTICLE PAGES ====================
def build_navbar(active_page=''):
    return f'''    <!-- NAVBAR -->
    <nav class="navbar">
        <a href="../../index.html" class="navbar-brand">
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
            <a href="../../index.html" class="nav-link">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path>
                    <polyline points="9 22 9 12 15 12 15 22"></polyline>
                </svg>
                Home
            </a>
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
                    <a href="../format.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="4 7 4 4 20 4 20 7"></polyline><line x1="9" y1="20" x2="15" y2="20"></line><line x1="12" y1="4" x2="12" y2="20"></line></svg> Format</a>
                    <a href="../escape.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg> Escape</a>
                    <a href="../extract.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg> Extract</a>
                    <a href="../sort.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="5" x2="12" y2="19"></line><polyline points="19 12 12 19 5 12"></polyline></svg> Sort</a>
                    <a href="../clean.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"></path></svg> Clean</a>
                    <a href="../xml.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline></svg> XML</a>
                    <a href="../yaml.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4l4 16 4-16"></path><path d="M12 4l4 16"></path></svg> YAML</a>
                    <a href="../viewer.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path><circle cx="12" cy="12" r="3"></circle></svg> Viewer</a>
                    <a href="../json2csv.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="8" y1="13" x2="16" y2="13"></line><line x1="8" y1="17" x2="16" y2="17"></line></svg> CSV</a>
                    <a href="../compare.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 3h5v5"></path><path d="M8 3H3v5"></path><path d="M21 3l-7 7"></path><path d="M3 3l7 7"></path><path d="M16 21h5v-5"></path><path d="M8 21H3v-5"></path><path d="M21 21l-7-7"></path><path d="M3 21l7-7"></path></svg> Compare</a>
                    <a href="../regex-tester.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v4M12 18v4M4.93 4.93l2.83 2.83M16.24 16.24l2.83 2.83M2 12h4M18 12h4M4.93 19.07l2.83-2.83M16.24 7.76l2.83-2.83"></path></svg> Regex</a>
                    <a href="../base64.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="8" y1="12" x2="16" y2="12"></line></svg> Base64</a>
                    <a href="../url-encoder.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path></svg> URL Encoder</a>
                    <a href="../csv-to-excel.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="3" y1="9" x2="21" y2="9"></line><line x1="9" y1="21" x2="9" y2="9"></line></svg> Excel</a>
                    <a href="../excel-remove-duplicates.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg> Remove Duplicates</a>
                    <a href="../merge-csv.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 16v4a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h2"></path><path d="M8 12v4a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2v-4a2 2 0 0 0-2-2H10a2 2 0 0 0-2 2"></path></svg> Merge CSV</a>
                    <a href="../batch-file-renamer.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path></svg> Batch Rename</a>
                    <a href="../pdf-split.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="12" y1="18" x2="12" y2="12"></line><line x1="9" y1="15" x2="15" y2="15"></line></svg> PDF Split</a>
                    <a href="../timestamp-converter.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg> Timestamp</a>
                    <a href="../css-minifier.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="4 17 10 11 4 5"></polyline><line x1="12" y1="19" x2="20" y2="19"></line></svg> CSS Minifier</a>
                    <a href="../html-encoder.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg> HTML Encoder</a>
                </div>
</div>
            </div>
            <a href="index.html" class="nav-link{(' active' if active_page == 'blog' else '')}">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path>
                    <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path>
                </svg>
                Blog
            </a>
            <a href="../best-practices.html" class="nav-link">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
                    <polyline points="22 4 12 14.01 9 11.01"></polyline>
                </svg>
                Practices
            </a>
            <a href="../news.html" class="nav-link">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"></path>
                </svg>
                News
            </a>
            <a href="../about.html" class="nav-link">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <circle cx="12" cy="12" r="10"></circle>
                    <line x1="12" y1="16" x2="12" y2="12"></line>
                    <line x1="12" y1="8" x2="12.01" y2="8"></line>
                </svg>
                About
            </a>
            <a href="../changelog.html" class="nav-link">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <circle cx="12" cy="12" r="10"></circle>
                    <polyline points="12 6 12 12 16 14"></polyline>
                </svg>
                Changelog
            </a>
        </div>
    </nav>'''

def build_related_section(current_file, all_articles):
    """Build related articles section"""
    related = [a for a in all_articles if a['file'] != current_file][:3]
    if not related:
        return ''
    cards = ''
    for a in related:
        cards += f'''                <div class="related-card">
                    <h4><a href="{a['file']}">{a['headline'][:60]}</a></h4>
                    <p>{a['category']} · {a['date']}</p>
                </div>
'''
    return f'''
        <!-- Related Articles -->
        <section class="related-section">
            <h2 class="section-title">Related Articles</h2>
            <div class="related-grid">
{cards}            </div>
        </section>'''

def enhance_article(filepath, current_article, all_articles):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Fix CSS link (change ../../css to ../..css, and ensure it's not duplicated)
    content = re.sub(r'<link[^>]*href="[^"]*styles\.css"[^>]*>', '', content)

    # Extract body content between <article> tags
    article_m = re.search(r'(<article[^>]*>)(.*?)(</article>)', content, re.DOTALL)
    if not article_m:
        return False

    article_open = article_m.group(1)
    article_body = article_m.group(2)
    article_close = article_m.group(3)

    # Extract title from JSON-LD or title tag
    ld_title = re.search(r'"headline"\s*:\s*"([^"]+)"', content)
    title_text = ld_title.group(1) if ld_title else current_article['title']

    # Build new article with header
    new_article = f'''{article_open}
                <div class="article-header">
                    <div class="article-category cat-{current_article['category'].lower().replace(' ', '-')}">{current_article['category']}</div>
                    <h1 class="article-title">{title_text}</h1>
                    <div class="article-meta">
                        <span>Published: {current_article['date']}</span>
                        <span>·</span>
                        <span>{current_article['read_time']} read</span>
                    </div>
                </div>
                {article_body}
{article_close}'''

    # Extract main content area (between body open and footer/nav)
    # Find main tag
    main_m = re.search(r'(<main[^>]*>)(.*?)(</main>)', content, re.DOTALL)
    if not main_m:
        return False

    main_open = main_m.group(1)
    main_body = main_m.group(2)
    main_close = main_m.group(3)

    # Remove old article from main
    new_main_body = main_body.replace(article_m.group(0), new_article)
    # Remove old navbar if exists
    new_main_body = re.sub(r'<!-- NAVBAR -->.*?</nav>\s*', '', new_main_body, flags=re.DOTALL)
    # Remove old breadcrumb if exists
    new_main_body = re.sub(r'<div class="breadcrumb">.*?</div>\s*', '', new_main_body)
    # Add related section before </main>
    related = build_related_section(current_article['file'], all_articles)
    new_main_body = new_main_body.rstrip() + related + '\n    '

    new_content = content[:main_m.start()] + main_open + new_main_body + main_close + content[main_m.end():]

    # Fix navbar - replace or insert
    navbar = build_navbar('blog')

    # Try to find existing nav
    if '<nav class="navbar">' in new_content:
        new_content = re.sub(r'<nav class="navbar">.*?</nav>\s*', navbar + '\n\n    ', new_content, flags=re.DOTALL)
    else:
        new_content = new_content.replace('<body>', '<body>\n    ' + navbar)

    # Add styles.css after head
    if '../../css/styles.css' not in new_content:
        new_content = new_content.replace('</head>', '<link rel="stylesheet" href="../../css/styles.css">\n</head>')

    # Fix footer links to point to ../../index.html
    new_content = re.sub(r'href="\.\./(index\.html)"', r'href="../../\1"', new_content)
    new_content = re.sub(r'href="\.\./(about\.html|changelog\.html|best-practices\.html|news\.html|blog\.html)"', r'href="../\1"', new_content)

    # Fix blog.html links in footer
    new_content = new_content.replace('href="../blog.html"', 'href="index.html"')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    return True

# Enhance all articles
enhanced = 0
for a in articles:
    path = os.path.join(BLOG_DIR, a['file'])
    if enhance_article(path, a, articles):
        enhanced += 1
        print(f'Enhanced: {a["file"]}')
    else:
        print(f'FAILED: {a["file"]}')

print(f'\nDone: {enhanced}/{len(articles)} articles enhanced')
print(f'Blog index: {INDEX_FILE}')
