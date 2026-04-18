#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, re
sys.stdout.reconfigure(encoding='utf-8')

INDEX_FILE = r'd:\网站开发-json\index.html'
with open(INDEX_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

print('File size:', len(content))
print('Chars around position 8030-8250:')
print(repr(content[8030:8250]))

# Use regex to replace the async block
pattern = r'<link rel="preload" href="css/styles\.css" as="style"> <link rel="stylesheet" href="css/styles\.css" media="print" onload="this\.media=\'all\'"> <noscript><link rel="stylesheet" href="css/styles\.css"></noscript>'
replacement = '<link rel="stylesheet" href="css/styles.css">'

m = re.search(pattern, content)
if m:
    content = re.sub(pattern, replacement, content)
    print('FIXED: async CSS -> sync CSS')
else:
    # Try without the noscript
    pattern2 = r'<link rel="preload" href="css/styles\.css" as="style">'
    m2 = re.search(pattern2, content)
    if m2:
        # Find the end of the noscript block
        start = m2.start()
        end_marker = '</noscript>'
        end_pos = content.find(end_marker, start)
        if end_pos > 0:
            block = content[start:end_pos + len(end_marker)]
            print('Found block to replace:')
            print(repr(block))
            content = content[:start] + replacement + content[end_pos + len(end_marker):]
            print('FIXED: replaced block')
        else:
            print('ERROR: noscript end not found')
    else:
        print('ERROR: preload link not found')

with open(INDEX_FILE, 'w', encoding='utf-8') as f:
    f.write(content)
print('Written. Size:', len(content))

# Verify - check links
import re as re2
links = re2.findall(r'<link[^>]*styles\.css[^>]*>', content)
print('Remaining styles.css links:')
for l in links:
    print(' ', l)
