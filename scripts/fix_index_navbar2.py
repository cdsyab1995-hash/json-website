#!/usr/bin/env python3
"""Fix index.html navbar for P0 tools - improved pattern"""

fp = r'd:\网站开发-json\index.html'
with open(fp, 'r', encoding='utf-8') as f:
    content = f.read()

if 'regex-tester.html' in content:
    print('[SKIP] index.html already has P0 tools')
else:
    # Find the Compare link in index.html
    # Pattern: href="pages/compare.html" followed by any content ending with Compare
    search = 'href="pages/compare.html"'
    idx = content.find(search)
    if idx < 0:
        print('[WARN] pages/compare.html not found')
    else:
        # Find the end of this link: </a>
        end_idx = content.find('</a>', idx)
        if end_idx > 0:
            # Find what comes after </a>
            after = content[end_idx:end_idx+50]
            
            # Check if we need to insert P0 tools
            # They should go after Compare and before the closing </div></div>
            # Find the nav-dropdown-menu closing
            close_idx = content.find('</div>', end_idx)
            
            # Insert P0 tools after Compare's </a> and before the closing </div></div>
            insert_point = end_idx + 4  # after </a>
            
            p0_tools = '''
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
                    </a>'''
            
            content = content[:insert_point] + p0_tools + content[insert_point:]
            
            with open(fp, 'w', encoding='utf-8') as f:
                f.write(content)
            print('[OK] index.html updated with P0 tools')
        else:
            print('[WARN] </a> not found after compare.html')
