# -*- coding: utf-8 -*-
import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'd:\网站开发-json\pages\blog.html', 'r', encoding='utf-8') as f:
    content = f.read()

print('Total size:', len(content), 'chars')

# Find article blocks
articles = re.findall(r'<article[^>]*>', content)
print('Article blocks found:', len(articles))
for a in articles[:10]:
    print(' -', a[:120])

# Find all class= patterns
all_classes = re.findall(r'class="([^"]+)"', content)
unique_classes = sorted(set(all_classes))
print('\nAll unique classes:')
for c in unique_classes:
    print(' ', c)

# Find main sections
main_sections = re.findall(r'<div[^>]*class="([^"]*)"[^>]*>', content)
print('\nMain div classes:')
for c in sorted(set(main_sections)):
    print(' ', c)
