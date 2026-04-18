import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')

# Check nav links in key pages
pages_to_check = [
    (r'd:\网站开发-json\index.html', 'index.html'),
    (r'd:\网站开发-json\pages\news.html', 'pages/news.html'),
    (r'd:\网站开发-json\pages\format.html', 'pages/format.html'),
    (r'd:\网站开发-json\pages\best-practices.html', 'pages/best-practices.html'),
]

print('=== 导航栏链接检查 ===\n')
for path, name in pages_to_check:
    if not os.path.exists(path):
        print(f'{name}: FILE NOT FOUND')
        continue
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find nav section
    nav_match = re.search(r'<nav[^>]*>(.*?)</nav>', content, re.DOTALL)
    if nav_match:
        nav = nav_match.group(1)
        # Find all hrefs in nav
        hrefs = re.findall(r'href="([^"]+)"', nav)
        print(f'{name}:')
        for h in hrefs[:15]:
            print(f'  {h}')
        print()

# Check if best-practices.html is linked from anywhere with wrong path
print('=== best-practices 链接来源 ===')
for root, dirs, files in os.walk(r'd:\网站开发-json'):
    for f in files:
        if f.endswith('.html'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as fp:
                c = fp.read()
            links = re.findall(r'href="([^"]*best-practices[^"]*)"', c)
            if links:
                rel = os.path.relpath(path, r'd:\网站开发-json')
                # Categorize by link type
                for link in links:
                    if link.startswith('http'):
                        print(f'  {rel} -> ABSOLUTE: {link}')
                    elif link.startswith('/'):
                        print(f'  {rel} -> ROOT: {link}')
                    elif link.startswith('pages/') or link.startswith('../pages/'):
                        print(f'  {rel} -> CORRECT: {link}')
                    else:
                        print(f'  {rel} -> MAYBE_WRONG: {link}')
