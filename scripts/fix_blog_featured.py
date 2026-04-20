#!/usr/bin/env python3
"""Fix blog.html: replace expanded article with standard article-card format"""

import re

blog_path = r"d:\网站开发-json\pages\blog.html"

with open(blog_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the entire featured-section (expanded article) with a clean card
old_pattern = r'<!-- Featured Article -->.*?</section>'
new_section = '''<!-- Featured Article -->
        <section class="featured-section">
            <h2 class="section-title">Latest Article</h2>
            <article class="article-card featured-article">
                <div class="article-category cat-performance">Edge Computing</div>
                <h2><a href="blog/json-edge-computing-cloudflare-workers.html">JSON in Edge Computing: Building Sub-10ms API Responses with Cloudflare Workers</a></h2>
                <p class="article-excerpt">Move your JSON processing to Cloudflare Workers and cut API latency by 10x. Transform responses, validate payloads, and cache JSON at the edge — serving users from the nearest of 300+ global data centers.</p>
                <div class="article-meta">
                    <span>2026-04-20</span> |
                    <span>6-8 min read</span>
                </div>
                <a href="blog/json-edge-computing-cloudflare-workers.html" class="read-more">Read full article →</a>
            </article>
        </section>'''

new_content = re.sub(old_pattern, new_section, content, count=1, flags=re.DOTALL)

if new_content == content:
    print("ERROR: Pattern not found!")
else:
    with open(blog_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Fixed blog.html featured article section!")
