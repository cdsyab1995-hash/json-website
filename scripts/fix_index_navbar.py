#!/usr/bin/env python3
"""Fix index.html navbar for P0 tools"""

import re

fp = r'd:\网站开发-json\index.html'
with open(fp, 'r', encoding='utf-8') as f:
    content = f.read()

if 'regex-tester.html' in content:
    print('[SKIP] index.html already has P0 tools')
else:
    # Find Compare link pattern for index.html
    # In index.html, href is "pages/compare.html"
    pattern = r'(<a href="pages/compare\.html"[^>]*>.*?</svg>\s*Compare\s*</a>\s*)(</div>\s*</div>)'
    match = re.search(pattern, content, re.DOTALL)
    
    if match:
        replacement = r'''\1
                    <a href="pages/regex-tester.html" class="nav-link">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M12 2v4M12 18v4M4.93 4.93l2.83 2.83M16.24 16.24l2.83 2.83M2 12h4M18 12h4M4.93 19.07l2.83-2.83M16.24 7.76l2.83-2.83"></path>
                        </svg>
                        Regex
                    </a>
                    <a href="pages/base64.html" class="nav-link">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
                            <line x1="8" y1="12" x2="16" y2="12"></line>
                        </svg>
                        Base64
                    </a>
                    <a href="pages/url-encoder.html" class="nav-link">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path>
                            <path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path>
                        </svg>
                        URL Encoder
                    </a>
                \2'''
        
        content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(content)
        print('[OK] index.html updated with P0 tools')
    else:
        print('[WARN] Compare link pattern not found in index.html')
        # Debug: find what patterns exist
        idx = content.find('pages/compare.html')
        if idx >= 0:
            print(f'  Found compare at index {idx}')
            print(f'  Context: {repr(content[max(0,idx-50):idx+200])}')
