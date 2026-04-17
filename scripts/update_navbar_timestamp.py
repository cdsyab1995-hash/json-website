#!/usr/bin/env python3
"""Update all navbar dropdown menus to add Timestamp tool"""
import os
import re

def update_navbar(fp):
    """Add Timestamp tool to navbar dropdown"""
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if already has Timestamp link
    if 'timestamp-converter.html' in content:
        return False, 'Already has Timestamp'

    # Find UUID Generator link and add Timestamp after it
    # Pattern: <a href="uuid-generator.html" class="nav-link">
    uuid_pattern = r'(<a href="uuid-generator\.html" class="nav-link"[^>]*>.*?</a>\s*</div>\s*</div>\s*<a href="blog\.html")'

    timestamp_link = '''<a href="timestamp-converter.html" class="nav-link">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <circle cx="12" cy="12" r="10"></circle>
                            <polyline points="12 6 12 12 16 14"></polyline>
                        </svg>
                        Timestamp
                    </a>
                    </div>
                </div>
                <a href="blog.html"'''

    new_content = re.sub(uuid_pattern, timestamp_link, content, flags=re.DOTALL)

    if new_content != content:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True, 'Added Timestamp link'
    else:
        return False, 'Pattern not matched'

def main():
    pages_dir = r'd:\网站开发-json\pages'

    updated = []
    for fname in sorted(os.listdir(pages_dir)):
        if not fname.endswith('.html'):
            continue
        fp = os.path.join(pages_dir, fname)
        changed, msg = update_navbar(fp)
        if changed:
            updated.append(fname)
            print(f'[UPDATED] {fname}')
        else:
            print(f'[SKIP] {fname}: {msg}')

    print(f'\nUpdated {len(updated)} pages')
    for name in updated:
        print(f'  - {name}')

if __name__ == '__main__':
    main()
