# -*- coding: utf-8 -*-
"""Replace inline styles in index.html article cards with CSS classes."""
from pathlib import Path

idx = Path(r'd:\网站开发-json\index.html')
c = idx.read_text(encoding='utf-8')

replacements = [
    # date spans
    (' style="font-size: 0.8rem; color: var(--text-secondary);"', ' class="article-date-label"'),
    # article h3 inline styles
    (' style="font-size: 1.125rem; margin-bottom: 0.5rem; color: var(--primary);"', ' class="article-card-title"'),
    # article p inline styles
    (' style="color: var(--text-secondary); font-size: 0.95rem;"', ' class="article-card-excerpt"'),
    # article a inline styles
    (' style="display: inline-block; margin-top: 0.75rem; color: var(--primary); font-weight: 500;"', ' class="article-read-link"'),
]

count = 0
for old, new in replacements:
    times = c.count(old)
    c = c.replace(old, new)
    count += times
    print(f'Replaced {times}x: {old[:50]}...')

idx.write_text(c, encoding='utf-8')
print(f'\nTotal: {count} inline styles replaced with CSS classes')
