#!/usr/bin/env python3
"""Update sitemap.xml with new blog article URLs"""

import re

sitemap_path = r"d:\网站开发-json\sitemap.xml"

# New blog article URLs
new_urls = '''
    <url>
        <loc>https://www.aijsons.com/pages/blog/json-parsing-performance-comparison.html</loc>
        <lastmod>2026-04-17</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.8</priority>
    </url>
    <url>
        <loc>https://www.aijsons.com/pages/blog/zod-json-schema-validation-ai.html</loc>
        <lastmod>2026-04-16</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.8</priority>
    </url>
    <url>
        <loc>https://www.aijsons.com/pages/blog/mcp-json-standardizing-ai-tools.html</loc>
        <lastmod>2026-04-15</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.8</priority>
    </url>'''

with open(sitemap_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Add new URLs before </urlset>
if 'json-parsing-performance-comparison' not in content:
    content = content.replace('</urlset>', new_urls + '\n</urlset>')
    print("[OK] Added 3 new blog article URLs to sitemap.xml")
else:
    print("[SKIP] Blog URLs already exist in sitemap.xml")

with open(sitemap_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("[OK] sitemap.xml updated")
