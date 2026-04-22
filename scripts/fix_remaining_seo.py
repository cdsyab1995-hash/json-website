#!/usr/bin/env python3
"""Fix remaining SEO issues: canonical/og:url/twitter:url pointing to old /pages/ URLs"""
import re
import io
import sys
from pathlib import Path

for stream in [sys.stdout, sys.stderr]:
    if stream.encoding != 'utf-8':
        stream.reconfigure(encoding='utf-8', errors='replace')

BASE = Path('d:/网站开发-json')

# Old path -> new canonical URL
OLD_TO_NEW = {
    'pages/about.html': 'https://www.aijsons.com/about',
    'pages/blog.html': 'https://www.aijsons.com/blog',
    'pages/news.html': 'https://www.aijsons.com/news',
    'pages/best-practices.html': 'https://www.aijsons.com/best-practices',
    'pages/changelog.html': 'https://www.aijsons.com/changelog',
    'pages/format.html': 'https://www.aijsons.com/tools/json-formatter',
    'pages/escape.html': 'https://www.aijsons.com/tools/json-escape',
    'pages/extract.html': 'https://www.aijsons.com/tools/json-extract',
    'pages/sort.html': 'https://www.aijsons.com/tools/json-sort',
    'pages/clean.html': 'https://www.aijsons.com/tools/json-clean',
    'pages/xml.html': 'https://www.aijsons.com/tools/json-to-xml',
    'pages/yaml.html': 'https://www.aijsons.com/tools/json-to-yaml',
    'pages/viewer.html': 'https://www.aijsons.com/tools/json-viewer',
    'pages/json2csv.html': 'https://www.aijsons.com/tools/json-to-csv',
    'pages/compare.html': 'https://www.aijsons.com/tools/json-compare',
    'pages/base64.html': 'https://www.aijsons.com/tools/base64',
    'pages/batch-file-renamer.html': 'https://www.aijsons.com/tools/batch-renamer',
    'pages/css-minifier.html': 'https://www.aijsons.com/tools/css-minifier',
    'pages/csv-to-excel.html': 'https://www.aijsons.com/tools/csv-to-excel',
    'pages/excel-remove-duplicates.html': 'https://www.aijsons.com/tools/excel-remove-duplicates',
    'pages/hash-generator.html': 'https://www.aijsons.com/tools/hash-generator',
    'pages/html-encoder.html': 'https://www.aijsons.com/tools/html-encoder',
    'pages/jwt-decoder.html': 'https://www.aijsons.com/tools/jwt-decoder',
    'pages/merge-csv.html': 'https://www.aijsons.com/tools/merge-csv',
    'pages/pdf-split.html': 'https://www.aijsons.com/tools/pdf-split',
    'pages/regex-tester.html': 'https://www.aijsons.com/tools/regex-tester',
    'pages/timestamp-converter.html': 'https://www.aijsons.com/tools/timestamp-converter',
    'pages/url-encoder.html': 'https://www.aijsons.com/tools/url-encoder',
    'pages/uuid-generator.html': 'https://www.aijsons.com/tools/uuid-generator',
}

# Blog slugs
pb = BASE / 'pages' / 'blog'
if pb.exists():
    for f in pb.glob('*.html'):
        if f.name != 'index.html':
            slug = f.stem
            OLD_TO_NEW[f'pages/blog/{f.name}'] = f'https://www.aijsons.com/blog/{slug}'

# News slugs
pn = BASE / 'pages' / 'news'
if pn.exists():
    for f in pn.glob('*.html'):
        slug = f.stem
        OLD_TO_NEW[f'pages/news/{f.name}'] = f'https://www.aijsons.com/news/{slug}'

# Root files
for fname in ['about.html', 'blog.html', 'news.html', 'best-practices.html', 'changelog.html']:
    if fname in ['about.html']:
        OLD_TO_NEW[fname] = 'https://www.aijsons.com/about'
    elif fname == 'blog.html':
        OLD_TO_NEW[fname] = 'https://www.aijsons.com/blog'
    elif fname == 'news.html':
        OLD_TO_NEW[fname] = 'https://www.aijsons.com/news'
    elif fname == 'best-practices.html':
        OLD_TO_NEW[fname] = 'https://www.aijsons.com/best-practices'
    elif fname == 'changelog.html':
        OLD_TO_NEW[fname] = 'https://www.aijsons.com/changelog'

def fix_file(filepath):
    try:
        text = filepath.read_text(encoding='utf-8')
    except Exception as e:
        return 0, str(e)
    
    original = text
    changes = 0
    
    rel = str(filepath.relative_to(BASE)).replace('\\', '/')
    
    # Replace all occurrences of old URLs in the file
    for old_path, new_url in OLD_TO_NEW.items():
        old_url = f'https://www.aijsons.com{old_path}'
        if old_url in text:
            text = text.replace(old_url, new_url)
            changes += 1
    
    # For migrated pages (about/index.html etc), also fix any remaining self-refs
    migrated_self_refs = {
        'about/index.html': 'https://www.aijsons.com/about',
        'best-practices/index.html': 'https://www.aijsons.com/best-practices',
        'blog/index.html': 'https://www.aijsons.com/blog',
        'changelog/index.html': 'https://www.aijsons.com/changelog',
        'news/index.html': 'https://www.aijsons.com/news',
    }
    if rel in migrated_self_refs:
        new_url = migrated_self_refs[rel]
        # Find any /pages/xxx.html URL in the file and replace
        for old_path in OLD_TO_NEW.keys():
            old_url = f'https://www.aijsons.com{old_path}'
            if old_url in text:
                text = text.replace(old_url, new_url)
                changes += 1
    
    if text != original:
        filepath.write_text(text, encoding='utf-8')
    
    return changes, None

# Scan all HTML files
print('Scanning for SEO URL issues...')
total_changes = 0
files_updated = 0

for pattern in ['*.html', '**/*.html']:
    for f in BASE.glob(pattern):
        if any(x in str(f) for x in ['node_modules', '.git', '__pycache__', '.workbuddy']):
            continue
        
        rel = str(f.relative_to(BASE)).replace('\\', '/')
        
        # Only process migrated pages + old pages
        should_check = (
            rel.startswith('pages/') or
            rel in ['about.html', 'blog.html', 'news.html', 'best-practices.html', 'changelog.html'] or
            rel in ['about/index.html', 'best-practices/index.html', 'blog/index.html', 
                   'changelog/index.html', 'news/index.html']
        )
        
        if not should_check:
            continue
        
        changes, err = fix_file(f)
        if err:
            print(f'  ERROR {rel}: {err}')
        elif changes > 0:
            print(f'  FIXED {rel}: {changes} changes')
            total_changes += changes
            files_updated += 1

print(f'\nDone: {files_updated} files, {total_changes} SEO URL fixes')
