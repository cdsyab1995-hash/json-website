# -*- coding: utf-8 -*-
import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')

blog_dir = r'd:\网站开发-json\pages\blog'

print('=== blog/index.html ===')
with open(os.path.join(blog_dir, 'index.html'), 'r', encoding='utf-8') as f:
    idx = f.read()
print('Size:', len(idx))
print('Has navbar:', '<nav class="navbar">' in idx)
print('Has dropdown:', 'nav-dropdown-menu' in idx)
print('Has featured:', 'featured-article' in idx)
print('Has article cards:', idx.count('article-card'))
print('Has JSON-LD:', 'application/ld+json' in idx)
print('Canonical:', 'canonical' in idx)

print('\n=== Enhanced articles ===')
for f in sorted(os.listdir(blog_dir)):
    if f.endswith('.html') and f != 'index.html':
        path = os.path.join(blog_dir, f)
        with open(path, 'r', encoding='utf-8') as fp:
            content = fp.read()
        has_nav = '<nav class="navbar">' in content
        has_dropdown = 'nav-dropdown-menu' in content
        has_css = 'styles.css' in content
        has_related = 'related-section' in content
        has_breadcrumb = 'breadcrumb' in content
        has_header = 'article-header' in content
        print(f'  {f}: nav={has_nav} dropdown={has_dropdown} css={has_css} related={has_related} breadcrumb={has_breadcrumb} header={has_header}')

print('\n=== pages/blog.html ===')
with open(r'd:\网站开发-json\pages\blog.html', 'r', encoding='utf-8') as f:
    b = f.read()
print('Links to blog/index.html:', 'blog/index.html' in b)
print('Size:', len(b), 'chars')
