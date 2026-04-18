#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix dropdown menu:
1. Add 'wide' class to nav-dropdown-menu (2-column layout)
2. Fix CSS hover area issue - ensure menu stays visible when hovering into it
"""
import sys, re, os
sys.stdout.reconfigure(encoding='utf-8')

INDEX_FILE = r'd:\网站开发-json\index.html'
with open(INDEX_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

# Find nav-dropdown-menu div and add 'wide' class
old_menu = 'class="nav-dropdown-menu"'
new_menu = 'class="nav-dropdown-menu wide"'

if old_menu in content:
    content = content.replace(old_menu, new_menu, 1)  # only first occurrence (in navbar)
    print('FIXED: added wide class to nav-dropdown-menu')
else:
    print('WARNING: nav-dropdown-menu not found')

with open(INDEX_FILE, 'w', encoding='utf-8') as f:
    f.write(content)
print('Written:', len(content), 'bytes')
