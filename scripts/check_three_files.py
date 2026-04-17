#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

files = ['hash-generator.html', 'jwt-decoder.html', 'uuid-generator.html']
for f in files:
    path = r'd:\网站开发-json\pages\{}'.format(f)
    with open(path, 'r', encoding='utf-8') as fp:
        content = fp.read()
    has_head = '</head>' in content
    has_body = '</body>' in content
    has_manifest = 'manifest' in content
    print(f'{f}: has_head_close={has_head}, has_body_close={has_body}, has_manifest={has_manifest}')
    print(content[:300])
    print('---')
