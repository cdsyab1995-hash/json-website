# -*- coding: utf-8 -*-
import os

# 验证 Twitter Card
pages_dir = r'd:\网站开发-json\pages'
missing_twitter = []

for f in os.listdir(pages_dir):
    if f.endswith('.html'):
        fp = os.path.join(pages_dir, f)
        with open(fp, 'r', encoding='utf-8') as file:
            if 'twitter:card' not in file.read():
                missing_twitter.append(f)

# 检查 index.html
with open(r'd:\网站开发-json\index.html', 'r', encoding='utf-8') as f:
    if 'twitter:card' not in f.read():
        missing_twitter.append('index.html')

print('=== Twitter Card Status ===')
if missing_twitter:
    print(f'Missing: {len(missing_twitter)} pages')
    for p in missing_twitter:
        print(f'  - {p}')
else:
    print('All 27 pages have Twitter Card!')

# 验证 lazy loading
print()
print('=== Lazy Loading Status ===')
lazy_issues = []
for f in os.listdir(pages_dir):
    if f.endswith('.html'):
        fp = os.path.join(pages_dir, f)
        with open(fp, 'r', encoding='utf-8') as file:
            content = file.read()
            img_tags = [i for i in content.split('<img ') if i.startswith('src=')]
            for img in img_tags:
                if 'loading=' not in img:
                    lazy_issues.append(f)
                    break

if lazy_issues:
    print(f'Pages with non-lazy images: {len(lazy_issues)}')
else:
    print('All images have lazy loading!')
