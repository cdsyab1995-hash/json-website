#!/usr/bin/env python3
"""Check index.html navbar structure for PDF Split"""
import os
import re

fp = r'd:\网站开发-json\index.html'
with open(fp, 'r', encoding='utf-8') as f:
    content = f.read()

# Find PDF Split
idx = content.find('pdf-split.html')
if idx >= 0:
    start = max(0, idx - 200)
    end = min(len(content), idx + 500)
    print(content[start:end])
