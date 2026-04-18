import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')

sitemap = open(r'd:\网站开发-json\sitemap.xml', 'r', encoding='utf-8').read()

# Get all actual HTML files
actual_pages = set()
for root, dirs, files in os.walk(r'd:\网站开发-json'):
    for f in files:
        if f.endswith('.html'):
            rel = os.path.relpath(os.path.join(root, f), r'd:\网站开发-json').replace('\\', '/')
            actual_pages.add(rel)

# Root-level pages (these don't need /pages/)
root_pages = {'index.html', 'cookie.html', 'privacy.html', 'terms.html'}

# Check sitemap URLs
sitemap_urls = re.findall(r'<loc>([^<]+)</loc>', sitemap)
print(f'Sitemap URLs: {len(sitemap_urls)}')
print()

broken = []
for url in sitemap_urls:
    # Extract the path part
    path = url.replace('https://www.aijsons.com', '')
    
    # Check if this URL is correct
    # Root pages: no /pages/
    # Pages directory: has /pages/
    
    is_broken = False
    for root_page in root_pages:
        if path == '/' + root_page:
            # This is a root page - should be correct
            if root_page not in actual_pages:
                is_broken = True
            break
    else:
        # This should be in pages/ directory
        expected = 'pages/' + path.lstrip('/')
        if expected not in actual_pages and path.lstrip('/') not in actual_pages:
            # Check if the URL itself (without /pages/) exists
            file_path = path.lstrip('/')
            if file_path not in actual_pages:
                is_broken = True
    
    if is_broken:
        broken.append((url, path))

print(f'Broken sitemap entries: {len(broken)}')
for url, path in broken:
    print(f'  {url}')

# Fix sitemap: all non-root pages need /pages/ prefix
def fix_url(url):
    for rp in root_pages:
        if url.endswith(f'https://www.aijsons.com/{rp}'):
            return url
    # Add /pages/ prefix
    path = url.replace('https://www.aijsons.com/', '')
    if not path.startswith('pages/'):
        return f'https://www.aijsons.com/pages/{path}'
    return url

fixed_sitemap = sitemap
for url in sitemap_urls:
    new_url = fix_url(url)
    if new_url != url:
        fixed_sitemap = fixed_sitemap.replace(f'<loc>{url}</loc>', f'<loc>{new_url}</loc>')

with open(r'd:\网站开发-json\sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(fixed_sitemap)

print('\nSitemap fixed!')

# Show updated sitemap URLs
sitemap2 = open(r'd:\网站开发-json\sitemap.xml', 'r', encoding='utf-8').read()
urls2 = re.findall(r'<loc>([^<]+)</loc>', sitemap2)
print(f'Total sitemap URLs: {len(urls2)}')
print('Sample URLs:')
for u in urls2[:10]:
    print(f'  {u}')
