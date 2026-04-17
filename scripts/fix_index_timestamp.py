#!/usr/bin/env python3
"""Fix index.html to add Timestamp tool"""
import os
import re

fp = r'd:\网站开发-json\index.html'
with open(fp, 'r', encoding='utf-8') as f:
    content = f.read()

# Check if already has Timestamp
if 'timestamp-converter.html' in content:
    print('index.html already has Timestamp link')
    exit(0)

# Find PDF Split closing tag and add Timestamp after
pattern = r'(<a href="pages/pdf-split\.html"[^>]*>.*?</a>\s*</div>\s*</div>\s*<a href="pages/blog\.html")'

replacement = '''<a href="pages/pdf-split.html" class="nav-link">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                            <polyline points="14 2 14 8 20 8"></polyline>
                            <line x1="12" y1="18" x2="12" y2="12"></line>
                            <line x1="9" y1="15" x2="15" y2="15"></line>
                        </svg>
                        PDF Split
                    </a>
                    <a href="pages/timestamp-converter.html" class="nav-link">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <circle cx="12" cy="12" r="10"></circle>
                            <polyline points="12 6 12 12 16 14"></polyline>
                        </svg>
                        Timestamp
                    </a>
                </div>
            </div>
            <a href="pages/blog.html"'''

new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

if new_content != content:
    with open(fp, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('index.html updated with Timestamp link')
else:
    print('Pattern not matched, trying alternative...')
    # Try simpler pattern
    pattern2 = r'(PDF Split\s*</a>\s*</div>\s*</div>\s*<a href="pages/blog\.html")'
    replacement2 = '''PDF Split
                    </a>
                    <a href="pages/timestamp-converter.html" class="nav-link">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <circle cx="12" cy="12" r="10"></circle>
                            <polyline points="12 6 12 12 16 14"></polyline>
                        </svg>
                        Timestamp
                    </a>
                </div>
            </div>
            <a href="pages/blog.html"'''
    new_content = re.sub(pattern2, replacement2, content)
    if new_content != content:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print('index.html updated (alternative pattern)')
    else:
        print('Could not find pattern')
