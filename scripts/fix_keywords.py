import os
import re

# Fix remaining high-competition keywords
fixes = {
    r'd:\网站开发-json\pages\about.html': [
        ('provides free, fast, and private JSON', 'provides fast, private JSON'),
    ],
    r'd:\网站开发-json\pages\format.html': [
        ('100% free.">', ''),
        ('Online JSON formatter', 'JSON formatter'),
        ('Online JSON', 'JSON'),
    ],
    r'd:\网站开发-json\pages\compare.html': [
        ('Online JSON compare', 'JSON compare'),
        ('Online JSON', 'JSON'),
    ],
    r'd:\网站开发-json\pages\escape.html': [
        ('online JSON', 'JSON'),
    ],
    r'd:\网站开发-json\pages\extract.html': [
        ('online JSON', 'JSON'),
    ],
    r'd:\网站开发-json\pages\sort.html': [
        ('online JSON', 'JSON'),
    ],
    r'd:\网站开发-json\pages\clean.html': [
        ('online JSON', 'JSON'),
    ],
    r'd:\网站开发-json\pages\xml.html': [
        ('online JSON', 'JSON'),
    ],
    r'd:\网站开发-json\pages\yaml.html': [
        ('online JSON', 'JSON'),
    ],
    r'd:\网站开发-json\pages\viewer.html': [
        ('online JSON', 'JSON'),
    ],
    r'd:\网站开发-json\pages\json2csv.html': [
        ('online JSON', 'JSON'),
    ],
    r'd:\网站开发-json\pages\blog.html': [
        ('online JSON', 'JSON'),
    ],
    r'd:\网站开发-json\pages\news.html': [
        ('online JSON', 'JSON'),
    ],
    r'd:\网站开发-json\pages\best-practices.html': [
        ('online JSON', 'JSON'),
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
