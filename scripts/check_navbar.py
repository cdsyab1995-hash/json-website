#!/usr/bin/env python3
"""Check navbar structure in index.html"""
import os
import re

fp = r'd:\网站开发-json\index.html'
with open(fp, 'r', encoding='utf-8') as f:
    content = f.read()

# Find navbar
navbar_match = re.search(r'<nav[^>]*class="navbar"[^>]*>.*?</nav>', content, re.DOTALL)
if navbar_match:
    print(navbar_match.group(0)[:1500])
