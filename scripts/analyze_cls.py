#!/usr/bin/env python3
"""Analyze page layout and CLS issues"""
import os

def analyze_page(fp):
    """Analyze single page layout"""
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()

    issues = []

    # 1. Check fixed width/height attributes
    if 'width="' in content or 'height="' in content:
        issues.append('Uses width/height attributes on img')

    # 2. Check font-display
    if 'font-display: swap' not in content and 'font-display:optional' not in content:
        if 'fonts.googleapis.com' in content:
            issues.append('Google Fonts without font-display')

    # 3. Check container
    if 'min-height' not in content and '.container' in content:
        issues.append('Container may shift content')

    return issues

def main():
    pages = [
        (r'd:\网站开发-json\index.html', 'index.html'),
    ]

    # Add all tool pages
    for f in sorted(os.listdir(r'd:\网站开发-json\pages')):
        if f.endswith('.html'):
            pages.append((os.path.join(r'd:\网站开发-json\pages', f), f))

    print('=== CLS Issue Analysis ===\n')

    all_issues = {}
    for fp, name in pages:
        if os.path.exists(fp):
            issues = analyze_page(fp)
            if issues:
                all_issues[name] = issues

    # Count issues
    issue_count = {}
    for issues in all_issues.values():
        for issue in issues:
            issue_count[issue] = issue_count.get(issue, 0) + 1

    print('Issue Summary:')
    for issue, count in sorted(issue_count.items(), key=lambda x: -x[1]):
        print(f'  {count:2d} pages: {issue}')

    print(f'\n{len(all_issues)} pages with issues\n')

    # Detailed index.html analysis
    print('=== index.html Detail Analysis ===\n')
    with open(r'd:\网站开发-json\index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    if 'class="container"' in content:
        print('[OK] Uses container class')
    if 'hero' in content.lower():
        print('[OK] Has hero section')
    if 'min-height' in content:
        print('[OK] Has min-height set')
    if 'font-display' in content:
        print('[OK] Has font-display set')
    else:
        print('[MISSING] No font-display set')

    # Check CSS
    css_fp = r'd:\网站开发-json\css\styles.css'
    if os.path.exists(css_fp):
        # Try different encodings
        for enc in ['utf-8', 'utf-16', 'latin1', 'cp1252']:
            try:
                with open(css_fp, 'r', encoding=enc) as f:
                    css = f.read()
                break
            except:
                continue

        print('\n=== CSS Analysis ===\n')

        if 'font-display' in css:
            print('[OK] CSS has font-display')
        else:
            print('[MISSING] CSS no font-display')

        if 'aspect-ratio' in css:
            print('[OK] CSS has aspect-ratio')
        else:
            print('[MISSING] CSS no aspect-ratio')

        if 'contain:' in css:
            print('[OK] CSS has contain')

        if 'content-visibility' in css:
            print('[OK] CSS has content-visibility')
        else:
            print('[MISSING] CSS no content-visibility')

        # Check img CSS
        if 'img {' in css:
            idx = css.find('img {')
            img_section = css[idx:idx+200]
            print(f'\n  img CSS block:\n  {img_section[:200]}')

        # Check .container CSS
        if '.container' in css:
            idx = css.find('.container')
            container_section = css[idx:idx+300]
            print(f'\n  .container CSS block:\n  {container_section[:300]}')

if __name__ == '__main__':
    main()
