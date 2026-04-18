import sys, re, os
sys.stdout.reconfigure(encoding='utf-8')

print('=== 最终验证 ===\n')

# 1. pages/blog.html
with open(r'd:\网站开发-json\pages\blog.html', 'r', encoding='utf-8') as f:
    blog_html = f.read()

print(f'pages/blog.html: {len(blog_html)} chars')
print(f'  Article cards: {blog_html.count("article-card")}')
print(f'  Blog article links (blog/xxx): {blog_html.count("href=\"blog/")}')
print(f'  Root links (../): {blog_html.count("href=\"../")}')
print(f'  Canonical: {re.search(r"canonical.*?content=\"([^\"]+)\"", blog_html).group(1) if re.search(r"canonical.*?content=\"([^\"]+)\"", blog_html) else "MISSING"}')
print(f'  Templates: {"OK" if "templates-grid" in blog_html else "MISSING"}')
print(f'  Datasets: {"OK" if "datasets-list" in blog_html else "MISSING"}')

# 2. Individual article pages
blog_dir = r'd:\网站开发-json\pages\blog'
articles = [f for f in os.listdir(blog_dir) if f.endswith('.html')]
print(f'\nIndividual articles in blog/: {len(articles)}')
for f in sorted(articles):
    path = os.path.join(blog_dir, f)
    with open(path, 'r', encoding='utf-8') as fp:
        c = fp.read()
    has_nav = 'nav-dropdown' in c
    has_related = 'related-articles' in c
    has_breadcrumb = 'breadcrumb' in c
    has_back = 'href="../blog.html"' in c or 'href="index.html"' in c
    print(f'  {f}: nav={has_nav}, related={has_related}, breadcrumb={has_breadcrumb}, back_link={has_back}')

# 3. Sitemap
with open(r'd:\网站开发-json\sitemap.xml', 'r', encoding='utf-8') as f:
    sitemap = f.read()
blog_urls = re.findall(r'<loc>([^<]*blog[^<]*)</loc>', sitemap)
print(f'\nSitemap blog URLs ({len(blog_urls)}):')
for u in blog_urls:
    print(f'  {u}')
