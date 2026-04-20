# -*- coding: utf-8 -*-
"""
Blog Article Structure Validator
Checks that all blog articles have correct HTML structure and CSS classes.
Run as part of automation to ensure consistent styling.
"""
from __future__ import print_function
import os
import sys

BLOG_DIR = r'd:\网站开发-json\pages\blog'

REQUIRED_CLASSES = {
    'article-header': 'Article header container',
    'article-title': 'Article title (h1)',
    'article-content': 'Article body content',
    'article-category': 'Category badge',
}

REQUIRED_PATTERNS = [
    ('../../css/styles.css', 'CSS stylesheet link'),
    ('article-header', 'Article header'),
    ('article-title', 'Article title class'),
    ('article-content', 'Article content class'),
]

def check_article(filepath):
    """Check a single article file for required structure."""
    filename = os.path.basename(filepath)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    issues = []
    
    for pattern, desc in REQUIRED_PATTERNS:
        if pattern not in content:
            issues.append(f"Missing: {desc}")
    
    # Check h1 exists
    if '<h1' not in content:
        issues.append("Missing: <h1> title tag")
    
    # Check category class format
    if 'article-category' in content:
        import re
        categories = re.findall(r'class="article-category ([^"]+)"', content)
        if not categories:
            categories = re.findall(r"class='article-category ([^']+)'", content)
        for cat in categories:
            valid_cats = ['cat-tutorial', 'cat-debugging', 'cat-comparison', 
                         'cat-development', 'cat-security', 'cat-api-design', 
                         'cat-developer-tools']
            if cat not in valid_cats:
                issues.append(f"Unknown category class: {cat}")
    
    return issues


def main():
    print('=' * 60)
    print('Blog Article Structure Validator')
    print('=' * 60)
    
    files = [f for f in os.listdir(BLOG_DIR) 
             if f.endswith('.html') and f != 'index.html']
    
    total_articles = len(files)
    ok_count = 0
    issue_count = 0
    
    all_issues = []
    
    for filename in sorted(files):
        filepath = os.path.join(BLOG_DIR, filename)
        issues = check_article(filepath)
        
        if issues:
            issue_count += 1
            print(f'\n[BAD] {filename}')
            for issue in issues:
                print(f'      - {issue}')
            all_issues.append((filename, issues))
        else:
            ok_count += 1
            print(f'[OK]  {filename}')
    
    print('\n' + '=' * 60)
    print(f'Summary: {ok_count}/{total_articles} OK, {issue_count} need fixing')
    
    if all_issues:
        print('\nIssues found:')
        for filename, issues in all_issues:
            print(f'  {filename}: {len(issues)} issue(s)')
        return 1
    else:
        print('\nAll articles have correct structure!')
        return 0


if __name__ == '__main__':
    sys.exit(main())
