# -*- coding: utf-8 -*-
import sys, re
sys.stdout.reconfigure(encoding='utf-8')

path = r'd:\网站开发-json\pages\blog\json-schema-complete-guide-2026.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# CSS loading
css_links = re.findall(r'<link[^>]*>', content)
for c in css_links:
    if 'stylesheet' in c or 'css' in c:
        print('CSS:', c[:150])

# Check canonical
canon = re.search(r'<link rel="canonical"[^>]*>', content)
print('Canonical:', canon.group() if canon else 'MISSING')

# Check JSON-LD
ld = re.search(r'<script type="application/ld\+json">(.*?)</script>', content, re.DOTALL)
if ld:
    print('JSON-LD found:', ld.group(1)[:100])
else:
    print('JSON-LD: MISSING')

# Check article body structure
article_m = re.search(r'<article[^>]*>(.*?)</article>', content, re.DOTALL)
if article_m:
    print('Article body found, length:', len(article_m.group(1)))
else:
    print('Article body: MISSING')

# Show nav structure
nav_m = re.search(r'<nav[^>]*>(.*?)</nav>', content, re.DOTALL)
if nav_m:
    nav = nav_m.group(1)
    print('Nav has blog links:', 'blog' in nav)
    print('Nav has dropdown:', 'nav-dropdown' in nav)
