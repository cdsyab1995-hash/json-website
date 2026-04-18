import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')

# Check 1: best-practices.html existence
paths_to_check = [
    r'd:\网站开发-json\pages\best-practices.html',
    r'd:\网站开发-json\best-practices.html',
]
print('=== best-practices.html 检查 ===')
for p in paths_to_check:
    exists = os.path.exists(p)
    print(f'  {p}: {"EXISTS" if exists else "NOT FOUND"}')

# Check 2: sitemap and nav links pointing to best-practices
sitemap = open(r'd:\网站开发-json\sitemap.xml', 'r', encoding='utf-8').read()
best_practices = re.findall(r'<loc>([^<]*best-practices[^<]*)</loc>', sitemap)
print(f'\nSitemap entries for best-practices: {best_practices}')

# Check 3: nav links to best-practices in all files
print('\n=== 导航栏 best-practices 链接检查 ===')
for root, dirs, files in os.walk(r'd:\网站开发-json'):
    for f in files:
        if f.endswith('.html'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as fp:
                c = fp.read()
            links = re.findall(r'href="([^"]*best-practices[^"]*)"', c)
            if links:
                rel = os.path.relpath(path, r'd:\网站开发-json')
                print(f'  {rel}: {links}')

# Check 4: news.html nav-dropdown-menu class
print('\n=== news.html dropdown 检查 ===')
news_path = r'd:\网站开发-json\pages\news.html'
if os.path.exists(news_path):
    with open(news_path, 'r', encoding='utf-8') as f:
        c = f.read()
    m = re.search(r'<div[^>]*class="([^"]*nav-dropdown-menu[^"]*)"', c)
    if m:
        print(f'  nav-dropdown-menu classes: {m.group(1)}')
        print(f'  Has "wide": {"wide" in m.group(1)}')
    else:
        print('  NO nav-dropdown-menu found!')
else:
    print('  news.html NOT FOUND')

# Check 5: all pages missing best-practices links
print('\n=== 指向 best-practices 的所有链接 ===')
count = 0
for root, dirs, files in os.walk(r'd:\网站开发-json'):
    for f in files:
        if f.endswith('.html'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as fp:
                c = fp.read()
            links = re.findall(r'href="([^"]*best-practices[^"]*)"', c)
            if links:
                count += len(links)
print(f'Total links to best-practices: {count}')
