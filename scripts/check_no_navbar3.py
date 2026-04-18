#!/usr/bin/env python3
"""Check hash-generator and uuid-generator pages - full structure"""
import sys
import re
sys.stdout.reconfigure(encoding='utf-8')

for fname in ['hash-generator.html', 'uuid-generator.html']:
    fpath = rf'd:\网站开发-json\pages\{fname}'
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print(f"=== {fname} ===")
    print(f"Total length: {len(content)} chars")
    
    # Find main
    main_match = re.search(r'<main[^>]*>', content)
    if main_match:
        print(f"Main tag at: {main_match.start()}")
        print(content[main_match.start()-500:main_match.start()+200])
    print("\n")
