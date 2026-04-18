import sys, re
sys.stdout.reconfigure(encoding='utf-8')

# DECISION: Use pages/blog.html as canonical (landing page)
# Keep pages/blog/ for individual articles (multi-page architecture)
# pages/blog/index.html is an alias - delete it to avoid confusion

import os

# 1. Update sitemap: use blog.html as the main blog URL
sitemap_path = r'd:\网站开发-json\sitemap.xml'
with open(sitemap_path, 'r', encoding='utf-8') as f:
    sitemap = f.read()

# Replace all blog-related URLs to use blog.html
# pages/blog/ -> pages/blog.html
sitemap = sitemap.replace(
    'https://www.aijsons.com/pages/blog/',
    'https://www.aijsons.com/pages/blog.html'
)
sitemap = sitemap.replace(
    'https://www.aijsons.com/pages/blog/index.html',
    'https://www.aijsons.com/pages/blog.html'
)

with open(sitemap_path, 'w', encoding='utf-8') as f:
    f.write(sitemap)
print('Sitemap updated')

# Verify sitemap
with open(sitemap_path, 'r', encoding='utf-8') as f:
    s = f.read()
blog_urls = re.findall(r'<loc>([^<]*blog[^<]*)</loc>', s)
print(f'Sitemap blog URLs ({len(blog_urls)}):')
for u in blog_urls:
    print(' ', u)

# 2. Delete pages/blog/index.html to avoid confusion
blog_index = r'd:\网站开发-json\pages\blog\index.html'
if os.path.exists(blog_index):
    os.remove(blog_index)
    print(f'\nDeleted {blog_index} (not needed, pages/blog.html is canonical)')

# 3. Verify pages/blog.html has correct paths
with open(r'd:\网站开发-json\pages\blog.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update the canonical in blog.html itself
content = re.sub(
    r'<link rel="canonical" href="[^"]*"',
    '<link rel="canonical" href="https://www.aijsons.com/pages/blog.html"',
    content
)
content = re.sub(
    r'<meta property="og:url" content="[^"]*"',
    '<meta property="og:url" content="https://www.aijsons.com/pages/blog.html"',
    content
)
content = re.sub(
    r'"url":\s*"https://[^"]+"',
    '"url": "https://www.aijsons.com/pages/blog.html"',
    content
)

with open(r'd:\网站开发-json\pages\blog.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('\nUpdated blog.html canonical URLs')

# Final check
with open(r'd:\网站开发-json\pages\blog.html', 'r', encoding='utf-8') as f:
    final = f.read()
canonical = re.search(r'rel="canonical" href="([^"]+)"', final)
og_url = re.search(r'og:url" content="([^"]+)"', final)
ld_url = re.search(r'"url":\s*"([^"]+)"', final)
print(f'canonical: {canonical.group(1) if canonical else "NOT FOUND"}')
print(f'og:url: {og_url.group(1) if og_url else "NOT FOUND"}')
print(f'JSON-LD url: {ld_url.group(1) if ld_url else "NOT FOUND"}')
print(f'\nTotal size: {len(final)} chars')
print(f'Article cards: {final.count("article-card")}')
print(f'datasets-list: {"OK" if "datasets-list" in final else "MISSING"}')
print(f'templates-grid: {"OK" if "templates-grid" in final else "MISSING"}')
