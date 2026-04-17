#!/usr/bin/env python3
"""Analyze tool pages for CLS issues"""
import os
import re

def analyze_tool_page(fp):
    """Analyze a tool page"""
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()

    issues = []

    # Check for external scripts without defer/async
    scripts = re.findall(r'<script[^>]+src="[^"]+"[^>]*>', content)
    for script in scripts:
        if 'defer' not in script and 'async' not in script:
            if 'cdn' in script or 'googleapis' in script or 'unpkg' in script:
                issues.append(f'Blocking script: {script[:100]}')

    # Check for fonts
    if 'font-display' not in content and 'display=swap' not in content:
        if 'fonts.googleapis' in content:
            issues.append('Fonts without font-display')

    # Check for iframe
    if '<iframe' in content:
        issues.append('Contains iframe')

    # Check for dynamically sized elements
    if 'clientHeight' in content or 'clientWidth' in content:
        issues.append('Uses client dimension queries')

    # Check container
    if '.editor-container' in content:
        editor = re.search(r'\.editor-container\s*{[^}]+}', content)
        if editor:
            css = editor.group(0)
            if 'height:' not in css and 'min-height' not in css:
                issues.append('Editor container has no height')

    return issues

def main():
    pages_dir = r'd:\网站开发-json\pages'

    tool_pages = [
        'format.html', 'escape.html', 'extract.html', 'sort.html',
        'clean.html', 'xml.html', 'yaml.html', 'viewer.html',
        'json2csv.html', 'compare.html', 'base64.html', 'url-encoder.html',
        'regex-tester.html', 'jwt-decoder.html', 'hash-generator.html',
        'uuid-generator.html', 'merge-csv.html', 'batch-file-renamer.html',
        'pdf-split.html'
    ]

    print('=== Tool Pages Analysis ===\n')

    all_issues = {}
    for name in tool_pages:
        fp = os.path.join(pages_dir, name)
        if os.path.exists(fp):
            issues = analyze_tool_page(fp)
            if issues:
                all_issues[name] = issues

    # Count issue types
    issue_types = {}
    for issues in all_issues.values():
        for issue in issues:
            issue_type = issue.split(':')[0].strip()
            issue_types[issue_type] = issue_types.get(issue_type, 0) + 1

    print('Issue Summary:')
    for issue_type, count in sorted(issue_types.items(), key=lambda x: -x[1]):
        print(f'  {count:2d}x {issue_type}')

    print(f'\n{len(all_issues)} pages with issues\n')

    # Show detail
    for name, issues in sorted(all_issues.items()):
        print(f'{name}:')
        for issue in issues:
            print(f'  - {issue[:120]}')
        print()

if __name__ == '__main__':
    main()
