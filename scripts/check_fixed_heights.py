#!/usr/bin/env python3
"""Check navbar and footer heights"""
import os
import re

css_fp = r'd:\网站开发-json\css\styles.css'
with open(css_fp, 'r', encoding='utf-8') as f:
    content = f.read()

print('=== Navbar and Footer CSS ===\n')

# Find navbar
navbar_match = re.search(r'\.navbar\s*{([^}]+)}', content)
if navbar_match:
    print('.navbar {')
    print(navbar_match.group(1))
    print('}\n')

# Find footer
footer_match = re.search(r'(footer|site-footer)\s*{([^}]+)}', content)
if footer_match:
    print(f'.{footer_match.group(1)} {{')
    print(footer_match.group(2))
    print('}\n')

# Find mobile navbar
mobile_match = re.search(r'@media[^}]+navbar[^}]*{[^}]+}', content, re.I)
if mobile_match:
    print('Mobile navbar:')
    print(mobile_match.group(0)[:300])
