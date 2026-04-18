import sys, re, os
sys.stdout.reconfigure(encoding='utf-8')

BASE = 'https://www.aijsons.com'
PAGES = r'd:\网站开发-json\pages'
TODAY = '2026-04-18'

# Get all HTML pages
pages_dir_files = []
for root, dirs, files in os.walk(PAGES):
    for f in files:
        if f.endswith('.html'):
            full = os.path.join(root, f)
            rel = os.path.relpath(full, r'd:\网站开发-json')
            # Convert to URL path
            url_path = rel.replace('\\', '/')
            pages_dir_files.append((full, url_path))

# Read each page to get lastmod
def get_lastmod(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            c = f.read()
        m = re.search(r'<time[^>]*datetime="([^"]+)"', c)
        if m:
            return m.group(1)[:10]
        m = re.search(r'class="article-date[^"]*"[^>]*>([^<]+)', c)
        if m:
            d = re.search(r'\d{4}-\d{2}-\d{2}', m.group(1))
            if d:
                return d.group(0)
        return TODAY
    except:
        return TODAY

def get_priority(url):
    if url in [f'{BASE}/index.html']:
        return '1.0'
    if '/blog/' in url and url.endswith('.html'):
        return '0.8'
    if url.endswith(('.html', '-en.html')):
        return '0.7'
    return '0.5'

def get_changefreq(url):
    if '/blog/' in url:
        return 'weekly'
    if 'changelog' in url or 'news' in url:
        return 'weekly'
    if 'blog.html' in url or 'blog-en.html' in url:
        return 'weekly'
    return 'monthly'

# Build sitemap
entries = []
for full, url_path in sorted(pages_dir_files):
    url = BASE + '/' + url_path
    lastmod = get_lastmod(full)
    priority = get_priority(url)
    changefreq = get_changefreq(url)
    entries.append(f'''  <url>
    <loc>{url}</loc>
    <lastmod>{lastmod}</lastmod>
    <changefreq>{changefreq}</changefreq>
    <priority>{priority}</priority>
  </url>''')

sitemap = f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{chr(10).join(entries)}
</urlset>'''

with open(r'd:\网站开发-json\sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(sitemap)

print(f'Sitemap regenerated: {len(entries)} URLs')
# Show blog URLs
blog_urls = [e for e in entries if '/blog/' in e or 'blog.html' in e]
print(f'\nBlog URLs ({len(blog_urls)}):')
for u in blog_urls:
    url_m = re.search(r'<loc>([^<]+)</loc>', u)
    print(' ', url_m.group(1) if url_m else u)
