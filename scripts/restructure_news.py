"""
Restructure news.html to use blog.html structure.
Extracts news items and rebuilds the page with article-card grid layout.
"""
from pathlib import Path
import re

# News items extracted from the original news.html
news_items = [
    # Trending Today
    {
        "category": "AI",
        "title": "MCP Protocol Reaches 10,000+ Public Servers: The AI Tool Standard Takes Off",
        "excerpt": "The Model Context Protocol (MCP) has surpassed 10,000 public server implementations. From database connectors to filesystem tools, MCP is rapidly becoming the universal bridge for AI agents.",
        "date": "2026-04-21",
        "read_time": "4-5 min",
        "featured": True
    },
    {
        "category": "Web Platform",
        "title": "Browser DevTools Now Built-in JSON Schema Validation and Live Error Highlighting",
        "excerpt": "Chrome 122 and Firefox 120 now include native JSON Schema validation directly in DevTools. Developers can paste a schema and instantly see validation errors highlighted.",
        "date": "2026-04-21",
        "read_time": "3-4 min",
    },
    {
        "category": "Performance",
        "title": "Bun 2.0 Ships 5x Faster JSON Serialization: A New Benchmark Record",
        "excerpt": "Bun's latest release sets a new world record for JSON serialization speed, processing 1GB of JSON data in under 200ms.",
        "date": "2026-04-21",
        "read_time": "3-4 min",
    },
    # API Technology Updates
    {
        "category": "API",
        "title": "JSON Streaming API Now Supported in All Major Browsers",
        "excerpt": "The W3C JSON Streaming specification has reached full browser support across Chrome, Firefox, Safari, and Edge. Streaming JSON parsing for real-time AI responses is now a first-class web platform feature.",
        "date": "2026-04-20",
        "read_time": "4-5 min",
    },
    {
        "category": "Tool Updates",
        "title": "Cursor and VS Code Add Real-Time JSON Lint with AI Error Explanations",
        "excerpt": "AI-powered code editors now offer inline JSON linting that not only flags errors but explains them in plain English with suggested fixes.",
        "date": "2026-04-20",
        "read_time": "3-4 min",
    },
    {
        "category": "Dev Trends",
        "title": "Zod v4 Hits 5M Weekly Downloads: Runtime Type Validation for AI Pipelines",
        "excerpt": "Zod continues its explosive growth driven by the AI agent era. Developers are using Zod schemas to validate LLM outputs, MCP tool responses, and RAG pipeline data.",
        "date": "2026-04-20",
        "read_time": "5-6 min",
    },
    # Frontend & JSON
    {
        "category": "Framework",
        "title": "Next.js 16 Introduces Native JSON Streaming and Partial Prerendering",
        "excerpt": "Next.js 16's App Router now natively supports JSON streaming for LLM-powered pages with automatic partial prerendering.",
        "date": "2026-04-19",
        "read_time": "5-6 min",
    },
    {
        "category": "Runtime",
        "title": "Node.js 24 Ships Built-in Native JSON Schema Validation",
        "excerpt": "Node.js 24 includes built-in JSON Schema validation using Ajv integration. No more third-party dependencies for basic schema validation in server-side code.",
        "date": "2026-04-19",
        "read_time": "4-5 min",
    },
    # Developer Resources
    {
        "category": "Open Source",
        "title": "json-schema-to-typescript v6 Released: Generate TypeScript Types from Any JSON Schema",
        "excerpt": "Version 6 adds support for JSON Schema Draft 2020-12, improved recursive schema handling, and a new CLI with watch mode.",
        "date": "2026-04-18",
        "read_time": "4-5 min",
    },
    {
        "category": "Learning",
        "title": "JSONata 2.0 Launches with Native AI Query Support",
        "excerpt": "JSONata 2.0 introduces AI-assisted query generation — describe what you want in plain English and get a working JSONata expression.",
        "date": "2026-04-18",
        "read_time": "5-6 min",
    },
]

# Map news categories to existing blog.css classes
cat_class_map = {
    "AI": "cat-development",
    "Web Platform": "cat-development",
    "Performance": "cat-debugging",
    "API": "cat-development",
    "Tool Updates": "cat-debugging",
    "Dev Trends": "cat-development",
    "Framework": "cat-tutorial",
    "Runtime": "cat-comparison",
    "Open Source": "cat-tutorial",
    "Learning": "cat-tutorial",
}

def get_cat_class(cat):
    return cat_class_map.get(cat, "cat-development")

# Build featured article
featured = next((n for n in news_items if n.get("featured")), news_items[0])
featured_card = f'''            <article class="article-card featured-article">
                <div class="article-category {get_cat_class(featured['category'])}">{featured['category']}</div>
                <h2><a href="#">{featured['title']}</a></h2>
                <p class="article-excerpt">{featured['excerpt']}</p>
                <div class="article-meta">
                    <span>{featured['date']}</span> |
                    <span>{featured['read_time']} read</span>
                </div>
                <a href="#" class="read-more">Read the latest trending news \u2192</a>
            </article>'''

# Build article grid
articles_html = []
for n in news_items:
    articles_html.append(f'''                <article class="article-card">
                    <div class="article-category {get_cat_class(n['category'])}">{n['category']}</div>
                    <h3><a href="#">{n['title']}</a></h3>
                    <p class="article-excerpt">{n['excerpt']}</p>
                    <div class="article-meta">
                        <span>{n['date']}</span> |
                        <span>{n['read_time']} read</span>
                    </div>
                    <a href="#" class="read-more">Read more \u2192</a>
                </article>''')

articles_grid = '\n'.join(articles_html)

# New page body
new_body = '''</nav>

    <main class="main-container">
        <!-- Page Header / Hero -->
        <header class="page-hero">
            <div class="page-header text-center">
                <h1 class="page-title">Developer Trending News</h1>
                <p class="page-description">Daily API trends, JSON tools updates, and web development insights — curated for developers worldwide</p>
                <div class="breadcrumb">
                    <a href="../index.html">Home</a> / <span>News</span>
                </div>
            </div>
        </header>

        <!-- Featured News -->
        <section class="featured-section">
            <h2 class="section-title">Latest News</h2>
''' + featured_card + '''
        </section>

        <!-- All News Grid -->
        <section>
            <h2 class="section-title">All News</h2>
            <div class="articles-grid">
''' + articles_grid + '''
            </div>
        </section>

        <!-- Tips -->
        <div class="tip-box" style="margin-top: 2rem;">
            <strong>Stay Updated</strong><br>
            Follow this page for the latest JSON and API tech updates. Combined with our <a href="format.html">JSON Formatter</a> and <a href="escape.html">JSON Escape tools</a>, you can boost your development efficiency by several times!
        </div>
    </main>

    <!-- Footer -->
    <footer class="footer">
        <p>AI JSON - Instant client-side JSON processing. Your data stays private.</p>
        <p class="text-sm mt-sm">
            <a href="../privacy.html" class="text-primary">Privacy Policy</a> |
            <a href="../terms.html" class="text-primary">Terms of Service</a> |
            <a href="../cookie.html" class="text-primary">Cookie Policy</a>
        </p>
        <p class="text-small mt-sm">
            &copy; 2026 AI JSON. All rights reserved.
        </p>
    </footer>

    <script src="../js/app.js" defer></script>
    <script>
    // Theme Toggle
    (function() {
        var toggle = document.getElementById('themeToggle');
        if (!toggle) return;

        function applyTheme(theme) {
            if (theme === 'light') {
                document.documentElement.setAttribute('data-theme', 'light');
            } else {
                document.documentElement.removeAttribute('data-theme');
            }
        }

        function initTheme() {
            var saved = localStorage.getItem('theme');
            if (saved) {
                applyTheme(saved);
            } else if (window.matchMedia && window.matchMedia('(prefers-color-scheme: light)').matches) {
                applyTheme('light');
            }
        }

        toggle.addEventListener('click', function() {
            var current = document.documentElement.getAttribute('data-theme');
            var next = current === 'light' ? 'dark' : 'light';
            applyTheme(next);
            localStorage.setItem('theme', next);
        });

        initTheme();
    })();
    </script>
    <!-- PWA Service Worker -->
    <script>
    if ('serviceWorker' in navigator) {
        window.addEventListener('load', function() {
            navigator.serviceWorker.register('/sw.js').then(function(reg) {
            }).catch(function(err) {
                console.warn('[PWA] SW registration failed:', err);
            });
        });
    }
    </script>
</body>
</html>
'''

# Build the complete new news.html
old_news = Path(r'd:\网站开发-json\pages\news.html').read_text(encoding='utf-8')

# Extract head section (everything from <head> to </head>)
head_start = old_news.find('<head>')
head_end = old_news.find('</head>') + len('</head>')
head_section = old_news[head_start:head_end]

# Extract navbar (from <body> to </nav>)
# The body starts right after </head>
body_content = old_news[head_end:]
nav_start = body_content.find('<nav')
nav_end = body_content.find('</nav>') + len('</nav>')
navbar = body_content[nav_start:nav_end]

# Build new page
new_news = head_section + '\n<body>\n' + navbar + new_body

# Write
out_path = Path(r'd:\网站开发-json\pages\news.html')
out_path.write_text(new_news, encoding='utf-8')
print(f'news.html restructured successfully')
print(f'Featured: {featured["title"][:60]}...')
print(f'Total articles: {len(news_items)}')
