#!/usr/bin/env python3
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'd:\网站开发-json\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove duplicate CTA button
old_text = '<a href="format.html" class="nav-link navbar-cta"> Try Formatter </a>'

if old_text in content:
    print('Found duplicate CTA, removing...')
    content = content.replace(old_text, '')
    with open(r'd:\网站开发-json\index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print('Removed!')
else:
    print('Pattern not found')
