#!/usr/bin/env python3
"""Check Google Fonts loading method in pages"""
import os
import re

def check_fonts(fp):
    """Check font loading method"""
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find Google Fonts
    google_fonts = re.findall(r'https://fonts\.googleapis\.com/css2\?[^"<&\s]+', content)

    if google_fonts:
        has_display = 'display=swap' in google_fonts[0]
        return 'Google Fonts', has_display

    # Check for other font loading
    if 'Inter' in content or 'font-family' in content:
        return 'CSS font', False

    return 'No fonts', False

def main():
    pages_dir = r'd:\网站开发-json\pages'
    root_files = [r'd:\网站开发-json\index.html']

    all_pages = [(fp, os.path.basename(fp)) for fp in root_files]
    for f in os.listdir(pages_dir):
        if f.endswith('.html'):
            all_pages.append((os.path.join(pages_dir, f), f))

    print('Font Loading Status:')
    print('-' * 60)

    font_types = {}
    for fp, name in sorted(all_pages):
        font_type, has_display = check_fonts(fp)
        if font_type not in font_types:
            font_types[font_type] = {'total': 0, 'with_display': 0}
        font_types[font_type]['total'] += 1
        if has_display:
            font_types[font_type]['with_display'] += 1

        status = '[OK]' if has_display else '[MISSING]'
        print(f'{status} {name:40} {font_type}')

    print('-' * 60)
    print('\nSummary:')
    for font_type, stats in font_types.items():
        print(f'  {font_type}: {stats["with_display"]}/{stats["total"]} with display=swap')

if __name__ == '__main__':
    main()
