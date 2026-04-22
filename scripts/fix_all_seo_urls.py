#!/usr/bin/env python3
"""Fix all remaining SEO issues: canonical/og:url/twitter:url + missing canonicals"""
import re
import io
import sys
from pathlib import Path

for stream in [sys.stdout, sys.stderr]:
    if stream.encoding != 'utf-8':
        stream.reconfigure(encoding='utf-8', errors='replace')

BASE = Path('d:/网站开发-json')
BASE_URL = 'https://www.aijsons.com'

# old_path -> new_path (for URL replacement)
OLD_TO_NEW = {
    '/pages/about.html': '/about',
    '/pages/blog.html': '/blog',
    '/pages/news.html': '/news',
    '/pages/best-practices.html': '/best-practices',
    '/pages/changelog.html': '/changelog',
    '/pages/format.html': '/tools/json-formatter',
    '/pages/escape.html': '/tools/json-escape',
    '/pages/extract.html': '/tools/json-extract',
    '/pages/sort.html': '/tools/json-sort',
    '/pages/clean.html': '/tools/json-clean',
    '/pages/xml.html': '/tools/json-to-xml',
    '/pages/yaml.html': '/tools/json-to-yaml',
    '/pages/viewer.html': '/tools/json-viewer',
    '/pages/json2csv.html': '/tools/json-to-csv',
    '/pages/compare.html': '/tools/json-compare',
    '/pages/base64.html': '/tools/base64',
    '/pages/batch-file-renamer.html': '/tools/batch-renamer',
    '/pages/css-minifier.html': '/tools/css-minifier',
    '/pages/csv-to-excel.html': '/tools/csv-to-excel',
    '/pages/excel-remove-duplicates.html': '/tools/excel-remove-duplicates',
    '/pages/hash-generator.html': '/tools/hash-generator',
    '/pages/html-encoder.html': '/tools/html-encoder',
    '/pages/jwt-decoder.html': '/tools/jwt-decoder',
    '/pages/merge-csv.html': '/tools/merge-csv',
    '/pages/pdf-split.html': '/tools/pdf-split',
    '/pages/regex-tester.html': '/tools/regex-tester',
    '/pages/timestamp-converter.html': '/tools/timestamp-converter',
    '/pages/url-encoder.html': '/tools/url-encoder',
    '/pages/uuid-generator.html': '/tools/uuid-generator',
}

# Blog slugs -> new URL
pb = BASE / 'pages' / 'blog'
if pb.exists():
    for f in pb.glob('*.html'):
        if f.name != 'index.html':
            slug = f.stem
            OLD_TO_NEW[f'/pages/blog/{f.name}'] = f'/blog/{slug}'

# News slugs -> new URL
pn = BASE / 'pages' / 'news'
if pn.exists():
    for f in pn.glob('*.html'):
        slug = f.stem
        OLD_TO_NEW[f'/pages/news/{f.name}'] = f'/news/{slug}'

# Root files
for fname in ['about.html', 'blog.html', 'news.html', 'best-practices.html', 'changelog.html']:
    if fname == 'about.html':
        OLD_TO_NEW[f'/{fname}'] = '/about'
    elif fname == 'blog.html':
        OLD_TO_NEW[f'/{fname}'] = '/blog'
    elif fname == 'news.html':
        OLD_TO_NEW[f'/{fname}'] = '/news'
    elif fname == 'best-practices.html':
        OLD_TO_NEW[f'/{fname}'] = '/best-practices'
    elif fname == 'changelog.html':
        OLD_TO_NEW[f'/{fname}'] = '/changelog'

# Pages that need canonical tag added
NEEDS_CANONICAL = {
    'about/index.html': '/about',
    'blog/index.html': '/blog',
    'news/index.html': '/news',
    'best-practices/index.html': '/best-practices',
    'changelog/index.html': '/changelog',
}

total_changes = 0
files_updated = 0

for pattern in ['**/*.html']:
    for f in BASE.glob(pattern):
        if any(x in str(f) for x in ['node_modules', '.git', '__pycache__', '.workbuddy']):
            continue
        try:
            text = f.read_text(encoding='utf-8')
        except:
            continue
        
        original = text
        changes = 0
        rel = str(f.relative_to(BASE)).replace('\\', '/')
        
        # 1. Replace old URL references
        for old_path, new_path in OLD_TO_NEW.items():
            old_url = BASE_URL + old_path
            new_url = BASE_URL + new_path
            if old_url in text:
                text = text.replace(old_url, new_url)
                changes += 1
        
        # 2. Add missing canonical tag
        if rel in NEEDS_CANONICAL:
            if not re.search(r'<link[^>]+rel=["\']canonical["\']', text):
                new_url = BASE_URL + NEEDS_CANONICAL[rel]
                head_end = text.find('</head>')
                if head_end > 0:
                    canon_tag = f'<link rel="canonical" href="{new_url}">\n'
                    text = text[:head_end] + canon_tag + text[head_end:]
                    changes += 1
                    print(f'  ADDED canonical to {rel}: {new_url}')
        
        if text != original:
            f.write_text(text, encoding='utf-8')
            if changes > 0:
                print(f'  FIXED {rel}: {changes} changes')
            total_changes += changes
            files_updated += 1

print(f'\nDone: {files_updated} files, {total_changes} total changes')
