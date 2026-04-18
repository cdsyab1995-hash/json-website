import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')

# Check if old single-page blog.html still exists
old = r'd:\网站开发-json\pages\blog.html'
if os.path.exists(old):
    with open(old, 'r', encoding='utf-8') as f:
        c = f.read()
    articles = len(re.findall('<article', c))
    print(f'OLD pages/blog.html EXISTS: {articles} articles, {len(c)} chars')
else:
    print('OLD pages/blog.html DOES NOT EXIST')

# Check new multi-page index.html
new = r'd:\网站开发-json\pages\blog\index.html'
if os.path.exists(new):
    with open(new, 'r', encoding='utf-8') as f:
        c = f.read()
    links = len(re.findall('article-card', c))
    print(f'NEW pages/blog/index.html EXISTS: {links} article cards, {len(c)} chars')
    # Show first article link
    m = re.search(r'href="([^"]+\.html)"[^>]*article-card', c)
    if m:
        print('First article link:', m.group(1))
    # Show nav links
    nav_m = re.findall(r'href="([^"]+)"[^>]*>.*?(?:Blog|blog|Articles)', c)
    print('Blog nav links:', nav_m[:5])
else:
    print('NEW pages/blog/index.html DOES NOT EXIST')

# Check sitemap for blog entries
sitemap = r'd:\网站开发-json\sitemap.xml'
if os.path.exists(sitemap):
    with open(sitemap, 'r', encoding='utf-8') as f:
        s = f.read()
    blog_urls = re.findall(r'<loc>([^<]*blog[^<]*)</loc>', s)
    print(f'\nSitemap blog URLs ({len(blog_urls)}):')
    for u in blog_urls:
        print(' ', u)
