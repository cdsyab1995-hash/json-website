#!/usr/bin/env python3
"""Debug Google Fonts URL format"""
import os
import re

fp = r'd:\网站开发-json\index.html'
with open(fp, 'r', encoding='utf-8') as f:
    content = f.read()

# Find all font-related links
print('=== Font-related content in index.html ===\n')

# Find preconnect
preconnects = re.findall(r'<link[^>]+preconnect[^>]+>', content)
print('Preconnects:')
for p in preconnects:
    print(f'  {p}')

# Find Google Fonts
fonts = re.findall(r'<link[^>]+googleapis[^>]+>', content)
print('\nGoogle Fonts links:')
for f in fonts:
    print(f'  {f}')

# Find stylesheet
stylesheets = re.findall(r'<link[^>]+stylesheet[^>]+>', content)
print('\nStylesheets:')
for s in stylesheets:
    print(f'  {s}')
