#!/usr/bin/env python3
"""Replace old single-page blog.html with redirect to new multi-page blog."""
import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')

old_path = r'd:\网站开发-json\pages\blog.html'
new_path = r'd:\网站开发-json\pages\blog\index.html'

# Read new index.html
with open(new_path, 'r', encoding='utf-8') as f:
    new_content = f.read()

print(f'Read new blog/index.html: {len(new_content)} chars, {new_content.count("article-card")} article cards')

# Fix relative paths: new index uses "../../" for root, but old blog.html is in pages/
fixed = new_content.replace('../../index.html', '../index.html')
fixed = fixed.replace('../../pages/', '../')
fixed = fixed.replace('../../css/', '../css/')
fixed = fixed.replace('../../js/', '../js/')
fixed = fixed.replace('../../images/', '../images/')
fixed = fixed.replace('../../docs/', '../docs/')

# Fix sitemap link
fixed = fixed.replace('sitemap.html', '../sitemap.xml')

# Update title
fixed = fixed.replace(
    '<title>JSON Blog & Insights</title>',
    '<title>JSON Blog & Insights | Free JSON Tools for Developers</title>'
)

# Fix canonical/og:url from /pages/blog/ to /pages/blog.html
fixed = fixed.replace(
    'https://www.aijsons.com/pages/blog/',
    'https://www.aijsons.com/pages/blog.html'
)

# Fix JSON-LD url
fixed = fixed.replace(
    '"url": "https://www.aijsons.com/pages/blog/"',
    '"url": "https://www.aijsons.com/pages/blog.html"'
)

# Remove breadcrumb "Blog >" since this IS the blog page (no parent to go to)
fixed = re.sub(
    r'<div class="breadcrumb">.*?<a href="index\.html">Blog</a>.*?</div>\s*',
    '',
    fixed,
    flags=re.DOTALL
)

# Write to old path
with open(old_path, 'w', encoding='utf-8') as f:
    f.write(fixed)

print(f'Updated old blog.html with multi-page content: {len(fixed)} chars')
print(f'Article cards: {fixed.count("article-card")}')

# Update sitemap: blog.html should be the canonical URL
sitemap_path = r'd:\网站开发-json\sitemap.xml'
with open(sitemap_path, 'r', encoding='utf-8') as f:
    sitemap = f.read()

# Point blog.html URL to blog/index.html
sitemap = sitemap.replace(
    'https://www.aijsons.com/pages/blog.html',
    'https://www.aijsons.com/pages/blog/'
)

with open(sitemap_path, 'w', encoding='utf-8') as f:
    f.write(sitemap)

# Verify
with open(sitemap_path, 'r', encoding='utf-8') as f:
    s = f.read()
blog_urls = re.findall(r'<loc>([^<]*blog[^<]*)</loc>', s)
print(f'\nSitemap blog URLs ({len(blog_urls)}):')
for u in blog_urls:
    print(' ', u)
