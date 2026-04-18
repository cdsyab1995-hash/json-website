import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'd:\网站开发-json\pages\blog.html', 'r', encoding='utf-8') as f:
    content = f.read()

checks = [
    ('Google Fonts sync', 'fonts.googleapis.com/css2?family=DM+Sans'),
    ('styles.css', '../css/styles.css'),
    ('app.js', '../js/app.js'),
    ('og-image', '../og-image.png'),
    ('index.html link', '../index.html'),
    ('8 article cards', 'article-card', 8),
    ('breadcrumb removed', 'breadcrumb', 0),
    ('canonical /pages/blog.html', 'aijsons.com/pages/blog.html'),
    ('JSON-LD /pages/blog.html', '"url": "https://www.aijsons.com/pages/blog.html"'),
    ('Article: curl-json-api-guide', 'curl-json-api-guide'),
    ('Article: json-patch', 'json-patch-vs-merge-patch'),
    ('Templates section', 'templates-grid'),
    ('Datasets section', 'datasets-list'),
]

print('=== blog.html 路径验证 ===')
for name, pattern, *rest in checks:
    count = rest[0] if rest else None
    found = pattern in content
    if count is not None:
        actual = content.count(pattern)
        ok = found and actual == count
        print(f'{"OK" if ok else "FAIL"} ({actual}/{count}): {name}')
    else:
        print(f'{"OK" if found else "FAIL"}: {name}')

print(f'\nTotal size: {len(content)} chars')
print(f'Article links sample:')
links = re.findall(r'href="([^"]+\.html)"[^>]*article-card', content)
for l in links[:5]:
    print(' ', l)
