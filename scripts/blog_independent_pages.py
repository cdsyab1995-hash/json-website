#!/usr/bin/env python3
"""
Blog Independent Pages Structure
Convert blog.html articles to individual pages + blog as index
"""

import os
import re
import shutil
from datetime import datetime

# Article definitions - extract from blog.html
ARTICLES = {
    "20260417-json-parsing-performance": {
        "title": "JSON Parsing Performance: Comparing Native vs Library Implementations",
        "date": "2026-04-17",
        "reading_time": "5-7 minutes",
        "slug": "json-parsing-performance-comparison",
        "category": "Performance",
        "excerpt": "Benchmark results comparing JSON parsing speeds across Python, JavaScript, Rust, and Go.",
        "content": """<p>Benchmark results comparing JSON parsing speeds across Python, JavaScript, Rust, and Go. Learn which libraries offer the best performance for high-throughput API services.</p>

<p>In the rapidly evolving landscape of modern web development, performance benchmark has become an essential skill for developers building production-grade applications. This article explores key concepts, best practices, and practical implementation strategies.</p>

<h4>Understanding the Fundamentals</h4>
<p>When working with JSON in production environments, developers face common challenges that require thoughtful solutions. Whether you're building REST APIs, processing webhook payloads, or handling real-time data streams, understanding performance benchmark is crucial for maintaining clean, maintainable code.</p>

<h4>Practical Implementation</h4>
<p>Modern development workflows benefit from tools that handle JSON processing efficiently. AI JSON provides browser-based utilities that work entirely client-side, ensuring your data never leaves your machine while providing the formatting, validation, and conversion capabilities you need.</p>

<pre><code>{
  "example": "structured_data",
  "tools": ["formatter", "validator", "converter"],
  "benefits": {
    "speed": "instant_processing",
    "privacy": "client_side_only",
    "compatibility": "all_browsers"
  }
}</code></pre>

<h4>Industry Best Practices</h4>
<p>Leading companies like Stripe, Twilio, and GitHub have established patterns for JSON API design that balance flexibility with predictability. Following these patterns helps teams build APIs that are both developer-friendly and robust against edge cases.</p>

<h4>Key Takeaways</h4>
<ul>
    <li>Structured JSON data enables better API contracts and documentation</li>
    <li>Client-side processing ensures data privacy and reduces server load</li>
    <li>Modern development workflows benefit from JSON's ubiquity and tooling</li>
</ul>"""
    },
    "20260416-zod-json-schema": {
        "title": "Zod v4 + JSON Schema: Runtime Validation for AI Agent Responses",
        "date": "2026-04-16",
        "reading_time": "6-8 minutes",
        "slug": "zod-json-schema-validation-ai",
        "category": "AI Development",
        "excerpt": "TypeScript types only check at compile time — but LLMs respond at runtime. Zod v4 enables runtime validation.",
        "content": """<p>TypeScript types only check at compile time — but LLMs respond at runtime. Zod v4 is 14x faster, ships with built-in <code>.toJSONSchema()</code> for OpenAI Structured Outputs, and enables a retry loop that feeds validation errors back to the model.</p>

<h4>The Problem</h4>
<p>When building AI-powered applications, you can't rely on TypeScript alone to validate LLM outputs. A model might return malformed JSON, missing fields, or unexpected data types. Without validation, your application crashes or worse — silently accepts bad data.</p>

<h4>Solution: Zod + JSON Schema</h4>
<p>Zod v4 solves this with native JSON Schema support. Define your schema once, use it everywhere:</p>

<pre><code>import { z } from 'zod';

const ResponseSchema = z.object({
  status: z.enum(['success', 'error']),
  data: z.object({
    id: z.string().uuid(),
    timestamp: z.number().positive(),
    items: z.array(z.object({
      name: z.string(),
      value: z.number()
    }))
  }).optional()
});

// Convert to JSON Schema for OpenAI
const jsonSchema = ResponseSchema.toJSONSchema();
</code></pre>

<h4>Key Takeaways</h4>
<ul>
    <li>Runtime validation is essential for production AI applications</li>
    <li>Zod v4's JSON Schema export enables OpenAI Structured Outputs</li>
    <li>Validation errors can be fed back to LLMs for self-correction</li>
</ul>"""
    },
    "20260415-mcp-json-standard": {
        "title": "How MCP is Standardizing AI Tool Communication with JSON",
        "date": "2026-04-15",
        "reading_time": "4-6 minutes",
        "slug": "mcp-json-standardizing-ai-tools",
        "category": "AI Development",
        "excerpt": "The Model Context Protocol (MCP) is becoming the universal standard for AI tool interfaces.",
        "content": """<p>AI agents are no longer just generating text — they're executing actions. The Model Context Protocol (MCP) is becoming the universal standard for AI tool interfaces, using JSON Schema as the contract between human intent and AI execution.</p>

<h4>What is MCP?</h4>
<p>MCP (Model Context Protocol) defines how AI models communicate with external tools. It uses JSON Schema to describe tool inputs and outputs, ensuring type safety and clear contracts.</p>

<pre><code>{
  "tool": "format_json",
  "inputSchema": {
    "type": "object",
    "properties": {
      "data": { "type": "string" },
      "indent": { "type": "number", "default": 2 }
    },
    "required": ["data"]
  },
  "outputSchema": {
    "type": "object",
    "properties": {
      "result": { "type": "string" }
    }
  }
}</code></pre>

<h4>Key Takeaways</h4>
<ul>
    <li>MCP standardizes AI tool interfaces with JSON Schema</li>
    <li>Clear contracts enable reliable AI agent workflows</li>
    <li>JSON remains the foundation of structured AI communication</li>
</ul>"""
    }
}

def create_article_template(article_data, article_id):
    """Generate individual article page HTML"""
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="google-site-verification" content="Bq7rq6iKPPDtIQCMjYquCng3eeVG_Ni0tf1bqUQsQ2w" />
    <meta name="description" content="{article_data["excerpt"]} | AI JSON Blog">
    <meta name="author" content="AI JSON - Free JSON Tools for Developers">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://www.aijsons.com/pages/blog/{article_data["slug"]}.html">
    
    <!-- Open Graph -->
    <meta property="og:type" content="article">
    <meta property="og:url" content="https://www.aijsons.com/pages/blog/{article_data["slug"]}.html">
    <meta property="og:title" content="{article_data["title"]} | AI JSON Blog">
    <meta property="og:description" content="{article_data["excerpt"]}">
    
    <!-- Article JSON-LD -->
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": "{article_data["title"]}",
        "description": "{article_data["excerpt"]}",
        "datePublished": "{article_data["date"]}",
        "author": {{"@type": "Organization", "name": "AI JSON"}},
        "publisher": {{"@type": "Organization", "name": "AI JSON", "url": "https://www.aijsons.com"}},
        "audience": {{"@type": "Audience", "name": "Software Developers"}}
    }}
    </script>
    
    <title>{article_data["title"]} | AI JSON Blog</title>
    
    <!-- Styles (same as other pages) -->
    <style>
        *,*::before,*::after{{margin:0;padding:0;box-sizing:border-box}}
        :root{{--bg-main:#131c2e;--bg-dark:#0a0f1a;--bg-card:#1f2940;--bg-secondary:#2a3654;--text-primary:#F8FAFC;--text-secondary:#94A3B8;--primary:#22C55E;--space-sm:0.5rem;--space-md:1rem;--space-xl:2rem;--radius-md:8px;--radius-lg:12px}}
        body{{font-family:'DM Sans','Segoe UI',-apple-system,BlinkMacSystemFont,sans-serif;background:var(--bg-main);color:var(--text-primary);line-height:1.6;min-height:100vh;display:flex;flex-direction:column}}
        .navbar{{background:var(--bg-dark);height:64px;display:flex;align-items:center;justify-content:space-between;padding:0 var(--space-xl);border-bottom:1px solid var(--bg-secondary);position:sticky;top:0;z-index:100}}
        .navbar-brand{{font-size:1.25rem;font-weight:700;color:var(--text-primary);text-decoration:none;display:flex;align-items:center;gap:var(--space-sm)}}
        .main-container{{flex:1;max-width:800px;margin:0 auto;padding:var(--space-xl);width:100%}}
        .article-header{{margin-bottom:2rem;padding-bottom:1rem;border-bottom:1px solid var(--bg-secondary)}}
        .article-title{{font-size:2rem;margin-bottom:1rem;color:var(--primary)}}
        .article-meta{{color:var(--text-secondary);font-size:0.9rem;margin-bottom:1rem}}
        .article-content{{line-height:1.8}}
        .article-content h4{{color:var(--primary);margin:1.5rem 0 0.75rem;font-size:1.25rem}}
        .article-content p{{margin-bottom:1rem}}
        .article-content ul{{margin:1rem 0 1rem 1.5rem}}
        .article-content li{{margin-bottom:0.5rem}}
        .article-content pre{{background:var(--bg-dark);padding:1rem;border-radius:var(--radius-md);overflow-x:auto;margin:1rem 0}}
        .article-content code{{font-family:'Consolas','Monaco',monospace;background:var(--bg-secondary);padding:0.2rem 0.4rem;border-radius:4px}}
        .breadcrumb{{margin-bottom:1rem}}
        .breadcrumb a{{color:var(--primary);text-decoration:none}}
        .related-articles{{margin-top:3rem;padding-top:2rem;border-top:1px solid var(--bg-secondary)}}
        .related-articles h3{{color:var(--primary);margin-bottom:1rem}}
        .back-link{{display:inline-block;margin-top:2rem;color:var(--primary)}}
        .footer{{background:var(--bg-dark);color:var(--text-secondary);text-align:center;padding:var(--space-xl);margin-top:auto;border-top:1px solid var(--bg-secondary)}}
        .footer a{{color:var(--primary);text-decoration:none}}
    </style>
    <link rel="preconnect" href="https://fonts.googleapis.com" crossorigin>
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&display=swap&display=swap" media="print" onload="this.media='all'">
    <noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&display=swap"></noscript>
</head>
<body>
    <nav class="navbar">
        <a href="../../index.html" class="navbar-brand">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                <polyline points="14 2 14 8 20 8"></polyline>
            </svg>
            AI JSON
        </a>
        <a href="../blog.html" class="nav-link" style="color:var(--primary)">← Back to Blog</a>
    </nav>
    
    <main class="main-container">
        <div class="breadcrumb">
            <a href="../../index.html">Home</a> / <a href="../blog.html">Blog</a> / <span>{article_data["category"]}</span>
        </div>
        
        <article>
            <header class="article-header">
                <h1 class="article-title">{article_data["title"]}</h1>
                <div class="article-meta">
                    <span><strong>Published:</strong> {article_data["date"]}</span> | 
                    <span><strong>Reading time:</strong> {article_data["reading_time"]}</span> | 
                    <span><strong>Category:</strong> {article_data["category"]}</span>
                </div>
            </header>
            
            <div class="article-content">
                {article_data["content"]}
            </div>
            
            <a href="../blog.html" class="back-link">← Back to all articles</a>
        </article>
        
        <section class="related-articles">
            <h3>More Articles</h3>
            <div style="display:flex;flex-wrap:wrap;gap:0.5rem;">
                <a href="20260416-zod-json-schema.html" class="nav-link" style="background:var(--bg-secondary)">Zod v4 + JSON Schema</a>
                <a href="20260415-mcp-json-standard.html" class="nav-link" style="background:var(--bg-secondary)">MCP JSON Standard</a>
                <a href="../format.html" class="nav-link" style="background:var(--bg-secondary)">JSON Formatter</a>
                <a href="../json2csv.html" class="nav-link" style="background:var(--bg-secondary)">JSON to CSV</a>
            </div>
        </section>
    </main>
    
    <footer class="footer">
        <p>AI JSON - Free JSON Tools for Developers</p>
        <p style="margin-top:0.5rem;font-size:0.875rem;">
            <a href="../about.html">About</a> | <a href="../changelog.html">Changelog</a> | <a href="../../index.html">Home</a>
        </p>
    </footer>
</body>
</html>'''

def create_blog_index(articles):
    """Create updated blog.html as article index"""
    articles_html = ""
    for article_id, data in articles.items():
        articles_html += f'''
            <article class="article-card">
                <div class="article-category">{data["category"]}</div>
                <h3><a href="blog/{data["slug"]}.html">{data["title"]}</a></h3>
                <p class="article-excerpt">{data["excerpt"]}</p>
                <div class="article-meta">
                    <span>{data["date"]}</span> | 
                    <span>{data["reading_time"]}</span>
                </div>
                <a href="blog/{data["slug"]}.html" class="read-more">Read more →</a>
            </article>'''
    
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="google-site-verification" content="Bq7rq6iKPPDtIQCMjYquCng3eeVG_Ni0tf1bqUQsQ2w" />
    <meta name="description" content="JSON practices for developers. Learn AI workflows, API development patterns, and structured data techniques. Expert guides on JSON tips and modern web development.">
    <meta name="author" content="AI JSON - Free JSON Tools for Developers">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://www.aijsons.com/pages/blog.html">
    
    <!-- Open Graph -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://www.aijsons.com/pages/blog.html">
    <meta property="og:title" content="JSON Practices Blog - API Development & AI Workflows | AI JSON">
    <meta property="og:description" content="Expert guides on JSON practices, AI workflows, and API development patterns for developers worldwide.">
    
    <title>JSON Practices Blog - API Development & AI Workflows | AI JSON</title>
    
    <style>
        *,*::before,*::after{{margin:0;padding:0;box-sizing:border-box}}
        :root{{--bg-main:#131c2e;--bg-dark:#0a0f1a;--bg-card:#1f2940;--bg-secondary:#2a3654;--text-primary:#F8FAFC;--text-secondary:#94A3B8;--primary:#22C55E;--space-sm:0.5rem;--space-md:1rem;--space-xl:2rem;--radius-md:8px;--radius-lg:12px}}
        body{{font-family:'DM Sans','Segoe UI',-apple-system,BlinkMacSystemFont,sans-serif;background:var(--bg-main);color:var(--text-primary);line-height:1.6;min-height:100vh;display:flex;flex-direction:column}}
        .navbar{{background:var(--bg-dark);height:64px;display:flex;align-items:center;justify-content:space-between;padding:0 var(--space-xl);border-bottom:1px solid var(--bg-secondary);position:sticky;top:0;z-index:100}}
        .navbar-brand{{font-size:1.25rem;font-weight:700;color:var(--text-primary);text-decoration:none;display:flex;align-items:center;gap:var(--space-sm)}}
        .nav-link{{color:var(--text-secondary);text-decoration:none;padding:var(--space-sm) var(--space-md);border-radius:var(--radius-md);font-size:.875rem;font-weight:500;height:36px;display:inline-flex;align-items:center}}
        .nav-link:hover,.nav-link.active{{color:var(--primary);background:rgba(34,197,94,.1)}}
        .main-container{{flex:1;max-width:1000px;margin:0 auto;padding:var(--space-xl);width:100%}}
        .page-header{{text-align:center;margin-bottom:3rem}}
        .page-title{{font-size:2.5rem;margin-bottom:0.5rem;color:var(--primary)}}
        .page-description{{color:var(--text-secondary);font-size:1.1rem}}
        .breadcrumb{{margin-bottom:1rem;color:var(--text-secondary)}}
        .breadcrumb a{{color:var(--primary);text-decoration:none}}
        .articles-grid{{display:grid;gap:1.5rem}}
        .article-card{{background:var(--bg-card);border-radius:var(--radius-lg);padding:1.5rem;border:1px solid var(--bg-secondary)}}
        .article-category{{display:inline-block;background:var(--primary);color:var(--bg-dark);padding:0.25rem 0.75rem;border-radius:20px;font-size:0.75rem;font-weight:600;margin-bottom:0.75rem}}
        .article-card h3{{font-size:1.25rem;margin-bottom:0.75rem;color:var(--text-primary)}}
        .article-card h3 a{{color:inherit;text-decoration:none}}
        .article-card h3 a:hover{{color:var(--primary)}}
        .article-excerpt{{color:var(--text-secondary);margin-bottom:1rem;line-height:1.6}}
        .article-meta{{color:var(--text-secondary);font-size:0.85rem;margin-bottom:1rem}}
        .read-more{{color:var(--primary);text-decoration:none;font-weight:500}}
        .read-more:hover{{text-decoration:underline}}
        .footer{{background:var(--bg-dark);color:var(--text-secondary);text-align:center;padding:var(--space-xl);margin-top:auto;border-top:1px solid var(--bg-secondary)}}
        .footer a{{color:var(--primary);text-decoration:none}}
    </style>
    <link rel="preconnect" href="https://fonts.googleapis.com" crossorigin>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&display=swap&display=swap" media="print" onload="this.media='all'">
    <noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&display=swap"></noscript>
</head>
<body>
    <nav class="navbar">
        <a href="../index.html" class="navbar-brand">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                <polyline points="14 2 14 8 20 8"></polyline>
            </svg>
            AI JSON
        </a>
        <a href="blog.html" class="nav-link active">Blog</a>
    </nav>
    
    <main class="main-container">
        <div class="page-header">
            <h1 class="page-title">JSON Tech Blog</h1>
            <p class="page-description">Expert insights on JSON in modern development, AI workflows, and structured data</p>
            <div class="breadcrumb">
                <a href="../index.html">Home</a> / <span>Blog</span>
            </div>
        </div>
        
        <section class="articles-grid">
            {articles_html}
        </section>
    </main>
    
    <footer class="footer">
        <p>AI JSON - Free JSON Tools for Developers</p>
        <p style="margin-top:0.5rem;font-size:0.875rem;">
            <a href="about.html">About</a> | <a href="changelog.html">Changelog</a> | <a href="../index.html">Home</a>
        </p>
    </footer>
</body>
</html>'''

def main():
    pages_dir = r"d:\网站开发-json\pages"
    blog_dir = os.path.join(pages_dir, "blog")
    
    # Create blog directory
    if not os.path.exists(blog_dir):
        os.makedirs(blog_dir)
        print(f"[OK] Created: {blog_dir}")
    
    # Generate article pages
    print("\n[1/2] Creating article pages...")
    for article_id, article_data in ARTICLES.items():
        filename = f"{article_data['slug']}.html"
        filepath = os.path.join(blog_dir, filename)
        
        html = create_article_template(article_data, article_id)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"[OK] Created: blog/{filename}")
    
    # Generate blog index
    print("\n[2/2] Creating blog index page...")
    blog_index_path = os.path.join(pages_dir, "blog.html")
    blog_index_html = create_blog_index(ARTICLES)
    with open(blog_index_path, 'w', encoding='utf-8') as f:
        f.write(blog_index_html)
    print(f"[OK] Updated: blog.html")
    
    print("\n[Summary]")
    print(f"  - Created {len(ARTICLES)} article pages in blog/")
    print(f"  - Updated blog.html as article index")
    print("\n[Next Steps]")
    print("  1. Update sitemap.xml with new blog URLs")
    print("  2. Add navigation links from other pages")
    print("  3. Continue adding more articles")

if __name__ == "__main__":
    main()
