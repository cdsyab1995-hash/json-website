import sys, re
sys.stdout.reconfigure(encoding='utf-8')

path = r'd:\网站开发-json\sitemap.xml'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Current state: sitemap has both blog.html and blog/index.html
# We want: blog.html as canonical, keep individual articles as-is

# Remove duplicate /blog/ and /blog/index.html entries
# Keep the article files (they're in pages/blog/ directory)
# Fix: blog.html should be the landing page URL

# Current sitemap entries for blog:
# https://www.aijsons.com/pages/blog.html  <- WRONG (file was replaced)
# https://www.aijsons.com/pages/blog/     <- this dir doesn't exist as a route
# https://www.aijsons.com/pages/blog/index.html  <- this is inside blog/ dir

# Replace blog.html -> blog/index.html (since blog/index.html IS the actual file)
content = content.replace(
    'https://www.aijsons.com/pages/blog.html',
    'https://www.aijsons.com/pages/blog/'
)

# Verify
blog_urls = re.findall(r'<loc>([^<]*blog[^<]*)</loc>', content)
print(f'Sitemap blog URLs ({len(blog_urls)}):')
for u in blog_urls:
    print(' ', u)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print('\nSitemap updated.')
