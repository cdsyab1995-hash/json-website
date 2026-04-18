# -*- coding: utf-8 -*-
import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')

blog_dir = r'd:\网站开发-json\pages\blog'
missing_breadcrumb = [
    'ai-tool-calling-mcp-2026.html',
    'json-api-error-handling-2026.html',
    'json-schema-complete-guide-2026.html',
]

for f in missing_breadcrumb:
    path = os.path.join(blog_dir, f)
    with open(path, 'r', encoding='utf-8') as fp:
        content = fp.read()

    # Add breadcrumb before the article header
    breadcrumb = '''                <div class="breadcrumb">
                    <a href="index.html">Blog</a> / <span>Article</span>
                </div>
'''
    if 'breadcrumb' not in content:
        # Insert before article-header
        content = content.replace('<div class="article-header">', breadcrumb + '                <div class="article-header">', 1)
        with open(path, 'w', encoding='utf-8') as fp:
            fp.write(content)
        print(f'Added breadcrumb to: {f}')
    else:
        print(f'Already has breadcrumb: {f}')
