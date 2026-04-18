# -*- coding: utf-8 -*-
"""Fix duplicate article cards inserted by daily_blog.py in index.html"""

import re

INDEX_PATH = r'd:\网站开发-json\index.html'

with open(INDEX_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

original_len = len(content)

# The duplicate block inserted by daily_blog.py - 3 extra cards at lines 108-125
# Pattern: the 3 cards start with 4 spaces before <article
duplicate_block = (
    '    <article class="feature-card" style="text-align: left;">\n'
    '    <span style="font-size: 0.8rem; color: var(--text-secondary);">2026-04-18</span>\n'
    '    <h3 style="font-size: 1.125rem; margin-bottom: 0.5rem; color: var(--primary);">Stream JSON Data Efficiently: Handling Large Payloads Without Memory Issues</h3>\n'
    '    <p style="color: var(--text-secondary); font-size: 0.95rem;">Traditional JSON parsing loads entire documents into memory. Stream parsing allows processing of massive JSON files with minimal memory footprint. Perfect for log processing and data pipelines.</p>\n'
    '    <a href="pages/blog.html#ai-daily-20260418" style="display: inline-block; margin-top: 0.75rem; color: var(--primary); font-weight: 500;">Read more \u2192</a>\n'
    '</article>\n'
    '    <article class="feature-card" style="text-align: left;">\n'
    '    <span style="font-size: 0.8rem; color: var(--text-secondary);">2026-04-18</span>\n'
    '    <h3 style="font-size: 1.125rem; margin-bottom: 0.5rem; color: var(--primary);">Stream JSON Data Efficiently: Handling Large Payloads Without Memory Issues</h3>\n'
    '    <p style="color: var(--text-secondary); font-size: 0.95rem;">Traditional JSON parsing loads entire documents into memory. Stream parsing allows processing of massive JSON files with minimal memory footprint. Perfect for log processing and data pipelines.</p>\n'
    '    <a href="pages/blog.html#ai-daily-20260418" style="display: inline-block; margin-top: 0.75rem; color: var(--primary); font-weight: 500;">Read more \u2192</a>\n'
    '</article>\n'
    '    <article class="feature-card" style="text-align: left;">\n'
    '    <span style="font-size: 0.8rem; color: var(--text-secondary);">2026-04-18</span>\n'
    '    <h3 style="font-size: 1.125rem; margin-bottom: 0.5rem; color: var(--primary);">\U0001f527 JSON Patch (RFC 6902): Partial API Updates That Save Bandwidth</h3>\n'
    '    <p style="color: var(--text-secondary); font-size: 0.95rem;">Stop sending full JSON objects for tiny field changes. JSON Patch lets you describe exactly what changed in a compact, atomic operation array.</p>\n'
    '    <a href="pages/blog.html#ai-daily-20260418" style="display: inline-block; margin-top: 0.75rem; color: var(--primary); font-weight: 500;">Read more \u2192</a>\n'
    '</article> '
)

if duplicate_block in content:
    content = content.replace(duplicate_block, '')
    print(f'[OK] Removed duplicate block. Size: {original_len} -> {len(content)}')
else:
    # Try to count occurrences of the "Stream JSON" card
    count = content.count('Stream JSON Data Efficiently: Handling Large Payloads Without Memory Issues')
    print(f'Pattern not found exactly. Stream article appears {count} times')
    # Let's find the actual content around line 108
    lines = content.split('\n')
    print(f'Total lines: {len(lines)}')
    for i, line in enumerate(lines[105:130], start=106):
        print(f'{i}: {line[:100]}')

with open(INDEX_PATH, 'w', encoding='utf-8') as f:
    f.write(content)
print('File saved')
