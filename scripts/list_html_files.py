#!/usr/bin/env python3
"""List all HTML files in the project."""
from pathlib import Path

BASE = Path('d:/网站开发-json')
html_files = []

# Root level .html files
for f in BASE.glob('*.html'):
    html_files.append(f)

# index.html in subdirectories
for f in BASE.glob('*/index.html'):
    html_files.append(f)

# index.html in deeper subdirectories
for f in BASE.glob('*/*/index.html'):
    html_files.append(f)

# .html files in tools/
for f in BASE.glob('tools/*.html'):
    html_files.append(f)

# .html files in pages/
for f in BASE.glob('pages/*.html'):
    html_files.append(f)

html_files.sort()
for f in html_files:
    rel = f.relative_to(BASE)
    print(str(rel))
