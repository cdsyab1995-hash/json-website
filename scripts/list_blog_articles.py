# -*- coding: utf-8 -*-
import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')

blog_dir = r'd:\网站开发-json\pages\blog'
files = sorted(os.listdir(blog_dir))
print('Files in blog/:')
for f in files:
    if f.endswith('.html') and f != 'index.html':
        path = os.path.join(blog_dir, f)
        with open(path, 'r', encoding='utf-8') as fp:
            content = fp.read()
        title_m = re.search(r'<title>(.*?)</title>', content)
        title = title_m.group(1) if title_m else 'NO TITLE'
        desc_m = re.search(r'<meta name="description" content="(.*?)"', content)
        desc = (desc_m.group(1)[:80] + '...') if desc_m else 'NO DESC'
        words = len(re.sub(r'<[^>]+>', '', content))
        print(f'  {f}')
        print(f'    Title: {title[:70]}')
        print(f'    Desc: {desc}')
        print(f'    Words: ~{words//5}')
        print()
