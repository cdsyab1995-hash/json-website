#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r'd:\网站开发-json\index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f'Total lines: {len(lines)}')
for i, l in enumerate(lines):
    if any(tag in l.lower() for tag in ['<main', '<section', 'feature-section', 'tools-grid', 'hero', 'card-grid', 'feature-card']):
        print(f'{i+1}: {l.rstrip()[:100]}')
