#!/usr/bin/env python3
"""Fix Google Fonts without font-display in all pages"""
import os
import re

def fix_font_display(fp):
    """Add font-display:swap to Google Fonts URL"""
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if Google Fonts exists without font-display
    if 'fonts.googleapis.com' not in content:
        return False, 'No Google Fonts'

    if 'font-display=swap' in content or 'font-display: swap' in content:
        return False, 'Already has font-display'

    # Pattern to match Google Fonts link
    # https://fonts.googleapis.com/css2?family=XXX&family=YYY&display=swap
    pattern = r'(https://fonts\.googleapis\.com/css2\?[^"&]+)(&family=[^"&]+)?"'
    replacement = r'\1&family=\2&display=swap'

    new_content = content

    # Find all Google Fonts URLs
    google_fonts_pattern = r'https://fonts\.googleapis\.com/css2\?[^"<&\s]+'

    if re.search(google_fonts_pattern, content):
        # Check if already has display=swap
        if 'display=swap' not in content:
            # Add &display=swap to the URL
            def add_display(m):
                url = m.group(0)
                if 'display=' in url:
                    return url
                sep = '&' if '?' in url else '?'
                return url + f'{sep}display=swap'

            new_content = re.sub(google_fonts_pattern, add_display, content)

            if new_content != content:
                with open(fp, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                return True, 'Added font-display=swap'

    return False, 'No change needed'

def main():
    pages_dir = r'd:\网站开发-json\pages'
    root_files = [r'd:\网站开发-json\index.html']

    all_pages = [(fp, os.path.basename(fp)) for fp in root_files]
    for f in os.listdir(pages_dir):
        if f.endswith('.html'):
            all_pages.append((os.path.join(pages_dir, f), f))

    fixed = []
    for fp, name in sorted(all_pages):
        changed, msg = fix_font_display(fp)
        if changed:
            fixed.append((name, msg))
            print(f'[FIXED] {name}: {msg}')
        elif 'Already has' in msg:
            print(f'[OK] {name}: Already has font-display')
        else:
            print(f'[SKIP] {name}: {msg}')

    print(f'\nFixed {len(fixed)} pages')

if __name__ == '__main__':
    main()
