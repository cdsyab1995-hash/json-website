#!/usr/bin/env python3
import re

with open(r'd:\网站开发-json\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the broken CTA section
old_cta = '<!-- CTA Button --> <!--'

if old_cta in content:
    print('Found broken CTA, fixing...')
    new_cta = '''<!-- CTA Button -->
            <a href="pages/format.html" class="nav-link cta">Try Formatter</a>'''
    content = content.replace(old_cta, new_cta)
    with open(r'd:\网站开发-json\index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print('Fixed!')
else:
    print('CTA pattern not found')
    # Search for CTA section
    match = re.search(r'<!-- CTA Button -->.{0,100}', content)
    if match:
        print('Found:', match.group(0)[:200])
