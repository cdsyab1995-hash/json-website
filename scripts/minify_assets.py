#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minify CSS and JS files"""

import re
import os

def minify_css(content):
    # Remove block comments /* ... */
    content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
    # Remove line comments (// ... ) — not standard CSS but just in case
    # Collapse whitespace
    content = re.sub(r'\s+', ' ', content)
    # Remove spaces around selectors, properties, braces, colons
    content = re.sub(r'\s*{\s*', '{', content)
    content = re.sub(r'\s*}\s*', '}', content)
    content = re.sub(r'\s*:\s*', ':', content)
    content = re.sub(r'\s*;\s*', ';', content)
    content = re.sub(r'\s*,\s*', ',', content)
    # Remove last semicolon before }
    content = re.sub(r';}', '}', content)
    # Remove leading/trailing whitespace
    content = content.strip()
    return content

def minify_js(content):
    # Remove single-line comments (but not URLs http://)
    content = re.sub(r'(?<![:/])//[^\n]*', '', content)
    # Remove block comments
    content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
    # Collapse whitespace (preserve newlines needed for ASI)
    content = re.sub(r'[ \t]+', ' ', content)
    # Remove blank lines
    content = re.sub(r'\n\s*\n', '\n', content)
    # Remove spaces around operators
    content = re.sub(r' *([{};,=+\-<>!&|]) *', r'\1', content)
    content = content.strip()
    return content

root = r'd:\网站开发-json'

# Process CSS
css_path = os.path.join(root, 'css', 'styles.css')
with open(css_path, 'r', encoding='utf-8') as f:
    css_orig = f.read()

orig_size = len(css_orig.encode('utf-8'))
css_min = minify_css(css_orig)
min_size = len(css_min.encode('utf-8'))

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css_min)

print(f'styles.css: {orig_size} -> {min_size} bytes ({round((1-min_size/orig_size)*100)}% reduction)')

# Process JS
js_path = os.path.join(root, 'js', 'app.js')
with open(js_path, 'r', encoding='utf-8') as f:
    js_orig = f.read()

orig_js_size = len(js_orig.encode('utf-8'))
js_min = minify_js(js_orig)
min_js_size = len(js_min.encode('utf-8'))

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js_min)

print(f'app.js: {orig_js_size} -> {min_js_size} bytes ({round((1-min_js_size/orig_js_size)*100)}% reduction)')
