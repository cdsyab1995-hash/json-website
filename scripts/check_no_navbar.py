#!/usr/bin/env python3
"""Check hash-generator and uuid-generator pages"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

for fname in ['hash-generator.html', 'uuid-generator.html']:
    fpath = rf'd:\网站开发-json\pages\{fname}'
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print(f"=== {fname} ===")
    # Find header
    header_match = __import__('re').search(r'<header[^>]*>', content)
    if header_match:
        print(f"Header tag: {header_match.group(0)}")
        # Print content around header
        start = max(0, header_match.start() - 100)
        end = min(len(content), header_match.end() + 500)
        print(content[start:end])
    else:
        # Find body start
        body_match = __import__('re').search(r'<body[^>]*>', content)
        if body_match:
            start = body_match.end()
            print(content[start:start+1000])
