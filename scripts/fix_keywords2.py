import os
import re

# Fix remaining JSON-LD and meta description keywords
fixes = {
    r'd:\网站开发-json\pages\escape.html': [
        ('"Online JSON escape and unescape tool', '"JSON escape and unescape tool'),
        ('"Online JSON', '"JSON'),
    ],
    r'd:\网站开发-json\pages\extract.html': [
        ('"Online JSONPath extractor', '"JSONPath extractor'),
        ('"Online JSON', '"JSON'),
    ],
    r'd:\网站开发-json\pages\sort.html': [
        ('"Online JSON key sorter', '"JSON key sorter'),
        ('"Online JSON', '"JSON'),
    ],
    r'd:\网站开发-json\pages\clean.html': [
        ('"Online JSON cleaner', '"JSON cleaner'),
        ('"Online JSON', '"JSON'),
    ],
    r'd:\网站开发-json\pages\xml.html': [
        ('"The #1 free XML to JSON', '"Professional XML to JSON'),
        ('"Online JSON', '"JSON'),
    ],
    r'd:\网站开发-json\pages\yaml.html': [
        ('"Online JSON YAML converter', '"JSON YAML converter'),
        ('"Online JSON', '"JSON'),
    ],
    r'd:\网站开发-json\pages\json2csv.html': [
        ('100% free.">', ''),
        ('"Online JSON to CSV converter', '"JSON to CSV converter'),
        ('"Online JSON', '"JSON'),
    ],
    r'd:\网站开发-json\terms.html': [
        ('Free online JSON processing', 'JSON processing'),
        ('free online JSON', 'JSON'),
    ],
}

for fp, replacements in fixes.items():
    if os.path.exists(fp):
        with open(fp, 'r', encoding='utf-8') as f:
            content = f.read()
        new_content = content
        for old, new in replacements:
            new_content = new_content.replace(old, new)
        if new_content != content:
            with open(fp, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'Fixed: {fp}')

print('\nDone!')
