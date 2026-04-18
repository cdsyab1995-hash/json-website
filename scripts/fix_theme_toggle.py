#!/usr/bin/env python3
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'd:\网站开发-json\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the broken CTA section
old = '<a href="pages/format.html" class="nav-link cta">Try Formatter</a> Theme Toggle -->'
new = '<a href="pages/format.html" class="nav-link cta">Try Formatter</a>'

if old in content:
    print('Found broken text, fixing...')
    content = content.replace(old, new)
    with open(r'd:\网站开发-json\index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print('Fixed!')
else:
    print('Pattern not found')
