# -*- coding: utf-8 -*-
import sys, re
sys.stdout.reconfigure(encoding='utf-8')

sitemap = r'd:\网站开发-json\sitemap.xml'
with open(sitemap, 'r', encoding='utf-8') as f:
    content = f.read()

# New blog URLs to add
new_urls = [
    'https://www.aijsons.com/pages/blog/index.html',
    'https://www.aijsons.com/pages/blog/json-schema-complete-guide-2026.html',
    'https://www.aijsons.com/pages/blog/json-api-error-handling-2026.html',
    'https://www.aijsons.com/pages/blog/json-parsing-performance-comparison.html',
    'https://www.aijsons.com/pages/blog/zod-json-schema-validation-ai.html',
    'https://www.aijsons.com/pages/blog/mcp-json-standardizing-ai-tools.html',
    'https://www.aijsons.com/pages/blog/ai-tool-calling-mcp-2026.html',
]

# Check which URLs are already in sitemap
for url in new_urls:
    if url in content:
        print(f'Already in sitemap: {url}')
    else:
        # Find last url entry to insert after
        last_loc = content.rfind('<url>')
        url_entry = f'''  <url>
    <loc>{url}</loc>
    <lastmod>2026-04-18</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
'''
        content = content.replace('</urlset>', url_entry + '</urlset>')
        print(f'Added: {url}')

with open(sitemap, 'w', encoding='utf-8') as f:
    f.write(content)
print('\nSitemap updated')
