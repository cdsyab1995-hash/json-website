# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
with open(r'd:\网站开发-json\pages\blog.html', 'r', encoding='utf-8') as f:
    content = f.read()

checks = [
    ('Google Fonts sync', 'fonts.googleapis.com/css2?family=DM+Sans'),
    ('styles.css link', '../css/styles.css'),
    ('Featured article', 'ai-daily-20260418'),
    ('Preview cards', 'article-card'),
    ('Templates grid', 'templates-grid'),
    ('JSON Datasets', 'datasets-list'),
    ('No async fonts', 'media="print"'),
    ('Section title', 'section-title'),
    ('Code blocks', 'code-block'),
    ('Dataset cards', 'dataset-card'),
]

all_ok = True
for name, pattern in checks:
    found = pattern in content
    status = 'OK' if found else 'MISSING'
    if not found:
        all_ok = False
    print(f'{status}: {name}')

print(f'\nTotal size: {len(content)} chars')
print('Overall:', 'PASS' if all_ok else 'FAIL')
