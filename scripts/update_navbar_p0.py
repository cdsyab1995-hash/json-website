#!/usr/bin/env python3
"""Update all pages to add P0 tools to navbar"""

import os
import re

P0_TOOLS_HTML = '''
                    <a href="regex-tester.html" class="nav-link">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M12 2v4M12 18v4M4.93 4.93l2.83 2.83M16.24 16.24l2.83 2.83M2 12h4M18 12h4M4.93 19.07l2.83-2.83M16.24 7.76l2.83-2.83"></path>
                        </svg>
                        Regex
                    </a>
                    <a href="base64.html" class="nav-link">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
                            <line x1="8" y1="12" x2="16" y2="12"></line>
                        </svg>
                        Base64
                    </a>
                    <a href="url-encoder.html" class="nav-link">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path>
                            <path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path>
                        </svg>
                        URL Encoder
                    </a>'''

def update_page(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Check if P0 tools already exist
    if 'regex-tester.html' in content:
        return False, 'already has P0 tools'
    
    # Find the closing </div> of nav-dropdown-menu after Compare link
    # Pattern: after Compare link's </a>, find </div></div>
    compare_pattern = r'(<a href="compare\.html"[^>]*>.*?</svg>\s*Compare\s*</a>\s*)(</div>\s*</div>)'
    
    match = re.search(compare_pattern, content, re.DOTALL)
    if match:
        content = content[:match.end(1)] + P0_TOOLS_HTML + '\n' + match.group(2) + content[match.end(2):]
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, 'updated'
    return False, 'no match found'

# Update pages directory
pages_dir = r'd:\网站开发-json\pages'
updated = []
for f in os.listdir(pages_dir):
    if not f.endswith('.html'):
        continue
    fp = os.path.join(pages_dir, f)
    changed, status = update_page(fp)
    if changed:
        updated.append(f)
        print(f'[OK] {f}: {status}')
    else:
        if 'no match' not in status and 'already' not in status:
            print(f'[SKIP] {f}: {status}')

print(f'\nTotal updated: {len(updated)} pages')

# Update index.html (root)
index_path = r'd:\网站开发-json\index.html'
with open(index_path, 'r', encoding='utf-8') as f:
    content = f.read()

if 'regex-tester.html' not in content:
    # Find Compare link in index.html
    compare_pattern = r'(<a href="pages/compare\.html"[^>]*>.*?</svg>\s*Compare\s*</a>\s*)(</div>\s*</div>)'
    match = re.search(compare_pattern, content, re.DOTALL)
    if match:
        content = content[:match.end(1)] + '''
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
                    </a>''' + '\n' + match.group(2) + content[match.end(2):]
        
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'[OK] index.html: updated')
    else:
        print(f'[SKIP] index.html: Compare link pattern not found')
else:
    print(f'[SKIP] index.html: already has P0 tools')
