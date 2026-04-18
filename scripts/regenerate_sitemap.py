import sys, re, os
sys.stdout.reconfigure(encoding='utf-8')

# Restore sitemap from git, then do surgical fix
os.system('git -C "d:\\网站开发-json" checkout -- sitemap.xml')

with open(r'd:\网站开发-json\sitemap.xml', 'r', encoding='utf-8') as f:
    sitemap = f.read()

# Strategy: keep article URLs in pages/blog/ as-is
# Replace ONLY the landing page entries (blog.html or blog/ or blog/index.html)
# to point to blog.html

# Find and replace blog landing page entries
landing_patterns = [
    'https://www.aijsons.com/pages/blog.html',
    'https://www.aijsons.com/pages/blog/',
    'https://www.aijsons.com/pages/blog/index.html',
]
for p in landing_patterns:
    sitemap = sitemap.replace(p, 'https://www.aijsons.com/pages/blog.html')

# Verify result
blog_urls = re.findall(r'<loc>([^<]*blog[^<]*)</loc>', sitemap)
print(f'Sitemap blog URLs ({len(blog_urls)}):')
for u in blog_urls:
    print(' ', u)

# Check for any malformed URLs
bad = [u for u in blog_urls if 'blog.html' in u and not u.endswith('.html') or u.endswith('.html') and '/blog/' not in u and 'blog' in u and u.count('/') < 3]
if bad:
    print('\nWARNING - potentially malformed URLs:')
    for b in bad:
        print(' ', b)

with open(r'd:\网站开发-json\sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(sitemap)
print('\nSitemap regenerated.')
