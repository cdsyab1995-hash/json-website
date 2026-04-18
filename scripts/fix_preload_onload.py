#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, re, os
sys.stdout.reconfigure(encoding='utf-8')

warn_files = [
    r'd:\网站开发-json\pages\batch-file-renamer.html',
    r'd:\网站开发-json\pages\css-minifier.html',
    r'd:\网站开发-json\pages\csv-to-excel.html',
    r'd:\网站开发-json\pages\excel-remove-duplicates.html',
    r'd:\网站开发-json\pages\html-encoder.html',
    r'd:\网站开发-json\pages\merge-csv.html',
    r'd:\网站开发-json\pages\pdf-split.html',
]

for filepath in warn_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove the preload with onload pattern (the rel=preload + as=style + onload variant)
    # Pattern: <link rel="preload" href="../css/styles.css" as="style" onload="this.onload=null;this.rel='stylesheet'">
    pattern = r"""<link rel="preload" href="[^"]*styles\.css" as="style" onload="[^"]*">\s*"""
    content = re.sub(pattern, '', content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    remaining = re.findall(r'<link[^>]*styles\.css[^>]*>', content)
    print(os.path.basename(filepath) + ': ' + str(len(remaining)) + ' links')
    for l in remaining:
        print('  ' + l[:100])
