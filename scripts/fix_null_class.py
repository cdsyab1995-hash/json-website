#!/usr/bin/env python3
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Fix clean.html bug
with open(r'd:\网站开发-json\pages\clean.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find class="null"
pattern = r'class="null"'
if pattern in content:
    print('Found class="null" in clean.html')
    # Check context
    idx = content.find(pattern)
    print('Context:', content[max(0,idx-50):idx+100])
    
    # Replace with proper class
    # The element seems to be a checkbox, let's see what it should be
    content = content.replace(pattern, 'class="checkbox-label"')
    
    with open(r'd:\网站开发-json\pages\clean.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print('Fixed!')
else:
    print('Pattern not found')

# Also check for any other pages with this issue
print('\nChecking other pages...')
import os
pages_dir = r'd:\网站开发-json\pages'
for filename in os.listdir(pages_dir):
    if filename.endswith('.html'):
        filepath = os.path.join(pages_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        if 'class="null"' in content:
            print(f'  Found in {filename}')
