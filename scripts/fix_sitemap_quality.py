#!/usr/bin/env python3
"""
Fix sitemap.xml missing lastmod and other issues
"""
import re

sitemap_path = "d:/网站开发-json/sitemap.xml"

with open(sitemap_path, 'r', encoding='utf-8') as f:
    content = f.read()

# URLs that need lastmod added (from 2026-04-17)
urls_missing_lastmod = [
    'regex-tester.html',
    'base64.html',
    'url-encoder.html',
    'jwt-decoder.html',
    'hash-generator.html',
    'uuid-generator.html'
]

# Add lastmod for missing URLs
for url in urls_missing_lastmod:
    # Pattern to find the <url> block containing this URL without lastmod
    pattern = rf'(<url>\s*<loc>https://www\.aijsons\.com/pages/{url}</loc>\s*)(<changefreq>)'
    replacement = rf'\1<lastmod>2026-04-17</lastmod>\n        \2'
    content = re.sub(pattern, replacement, content)

# Also fix any entries with monthly changefreq that are tools (should be weekly)
# Tools should generally be weekly for more frequent crawling
content = content.replace(
    '<changefreq>monthly</changefreq>\n        <priority>0.8</priority>\n    </url>',
    '<changefreq>weekly</changefreq>\n        <priority>0.8</priority>\n    </url>'
)

with open(sitemap_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("sitemap.xml fixed")
