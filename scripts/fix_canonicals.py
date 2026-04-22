#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""修复所有工具页损坏的 canonical URL"""
import re
import sys
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BASE = Path('d:/网站开发-json')

# 从旧 canonical 格式到新 slug 的映射
# 损坏的格式: /tools/https://www.aijsons.com/pages/xxx.html>
old_canonical_patterns = {
    'tools/base64/index.html': '/tools/https://www.aijsons.com/pages/base64.html>',
    'tools/batch-renamer/index.html': '/tools/https://www.aijsons.com/pages/batch-file-renamer.html>',
    'tools/css-minifier/index.html': '/tools/https://aijsons.com/pages/css-minifier.html>',
    'tools/csv-to-excel/index.html': '/tools/https://www.aijsons.com/pages/csv-to-excel.html>',
    'tools/excel-remove-duplicates/index.html': '/tools/https://www.aijsons.com/pages/excel-remove-duplicates.html>',
    'tools/hash-generator/index.html': '/tools/https://www.aijsons.com/pages/hash-generator.html>',
    'tools/html-encoder/index.html': '/tools/https://aijsons.com/pages/html-encoder.html>',
    'tools/json-clean/index.html': '/tools/https://www.aijsons.com/pages/clean.html>',
    'tools/json-compare/index.html': '/tools/https://www.aijsons.com/pages/compare.html>',
    'tools/json-escape/index.html': '/tools/https://www.aijsons.com/pages/escape.html>',
    'tools/json-extract/index.html': '/tools/https://www.aijsons.com/pages/extract.html>',
    'tools/json-formatter/index.html': '/tools/https://www.aijsons.com/pages/format.html>',
    'tools/json-sort/index.html': '/tools/https://www.aijsons.com/pages/sort.html>',
    'tools/json-to-csv/index.html': '/tools/https://www.aijsons.com/pages/json2csv.html>',
    'tools/json-to-xml/index.html': '/tools/https://www.aijsons.com/pages/xml.html>',
    'tools/json-to-yaml/index.html': '/tools/https://www.aijsons.com/pages/yaml.html>',
    'tools/json-viewer/index.html': '/tools/https://www.aijsons.com/pages/viewer.html>',
    'tools/jwt-decoder/index.html': '/tools/https://www.aijsons.com/pages/jwt-decoder.html>',
    'tools/merge-csv/index.html': '/tools/https://www.aijsons.com/pages/merge-csv.html>',
    'tools/pdf-split/index.html': '/tools/https://www.aijsons.com/pages/pdf-split.html>',
    'tools/regex-tester/index.html': '/tools/https://www.aijsons.com/pages/regex-tester.html>',
    'tools/timestamp-converter/index.html': '/tools/https://www.aijsons.com/pages/timestamp-converter.html>',
    'tools/url-encoder/index.html': '/tools/https://www.aijsons.com/pages/url-encoder.html>',
    'tools/uuid-generator/index.html': '/tools/https://www.aijsons.com/pages/uuid-generator.html>',
}

# 正确的 slug -> canonical
correct = {
    'tools/base64/index.html': 'https://www.aijsons.com/tools/base64',
    'tools/batch-renamer/index.html': 'https://www.aijsons.com/tools/batch-renamer',
    'tools/css-minifier/index.html': 'https://www.aijsons.com/tools/css-minifier',
    'tools/csv-to-excel/index.html': 'https://www.aijsons.com/tools/csv-to-excel',
    'tools/excel-remove-duplicates/index.html': 'https://www.aijsons.com/tools/excel-remove-duplicates',
    'tools/hash-generator/index.html': 'https://www.aijsons.com/tools/hash-generator',
    'tools/html-encoder/index.html': 'https://www.aijsons.com/tools/html-encoder',
    'tools/json-clean/index.html': 'https://www.aijsons.com/tools/json-clean',
    'tools/json-compare/index.html': 'https://www.aijsons.com/tools/json-compare',
    'tools/json-escape/index.html': 'https://www.aijsons.com/tools/json-escape',
    'tools/json-extract/index.html': 'https://www.aijsons.com/tools/json-extract',
    'tools/json-formatter/index.html': 'https://www.aijsons.com/tools/json-formatter',
    'tools/json-sort/index.html': 'https://www.aijsons.com/tools/json-sort',
    'tools/json-to-csv/index.html': 'https://www.aijsons.com/tools/json-to-csv',
    'tools/json-to-xml/index.html': 'https://www.aijsons.com/tools/json-to-xml',
    'tools/json-to-yaml/index.html': 'https://www.aijsons.com/tools/json-to-yaml',
    'tools/json-viewer/index.html': 'https://www.aijsons.com/tools/json-viewer',
    'tools/jwt-decoder/index.html': 'https://www.aijsons.com/tools/jwt-decoder',
    'tools/merge-csv/index.html': 'https://www.aijsons.com/tools/merge-csv',
    'tools/pdf-split/index.html': 'https://www.aijsons.com/tools/pdf-split',
    'tools/regex-tester/index.html': 'https://www.aijsons.com/tools/regex-tester',
    'tools/timestamp-converter/index.html': 'https://www.aijsons.com/tools/timestamp-converter',
    'tools/url-encoder/index.html': 'https://www.aijsons.com/tools/url-encoder',
    'tools/uuid-generator/index.html': 'https://www.aijsons.com/tools/uuid-generator',
}

# 同时修复 og:url (如果有的话)
og_url_patterns = {
    'tools/json-formatter/index.html': 'https://www.aijsons.com/tools/format',
    'tools/json-escape/index.html': 'https://www.aijsons.com/tools/escape',
    'tools/json-extract/index.html': 'https://www.aijsons.com/tools/extract',
    'tools/json-sort/index.html': 'https://www.aijsons.com/tools/sort',
    'tools/json-clean/index.html': 'https://www.aijsons.com/tools/clean',
    'tools/json-to-xml/index.html': 'https://www.aijsons.com/tools/xml',
    'tools/json-to-yaml/index.html': 'https://www.aijsons.com/tools/yaml',
    'tools/json-viewer/index.html': 'https://www.aijsons.com/tools/viewer',
    'tools/json-to-csv/index.html': 'https://www.aijsons.com/tools/json2csv',
    'tools/json-compare/index.html': 'https://www.aijsons.com/tools/compare',
}

count = 0
for rel_path, broken in old_canonical_patterns.items():
    f = BASE / rel_path
    if not f.exists():
        print(f'MISSING: {rel_path}')
        continue
    text = f.read_text(encoding='utf-8')
    original = text

    # 修复 canonical
    text = text.replace(broken, f'<link rel="canonical" href="{correct[rel_path]}">')

    # 修复 og:url
    correct_slug = rel_path.split('/')[1]
    if rel_path in og_url_patterns:
        text = text.replace(
            f'content="{og_url_patterns[rel_path]}">',
            f'content="{correct[rel_path]}">'
        )

    if text != original:
        f.write_text(text, encoding='utf-8')
        count += 1
        print(f'Fixed canonical: {rel_path}')

print(f'\nTotal fixed: {count}')
print('Done.')
