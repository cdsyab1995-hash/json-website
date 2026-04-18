#!/usr/bin/env python3
"""
Fix blog/news pages - remove "US Developers" exclusive targeting
Tools are universal, content should be too
"""
import os
import glob

base_dir = "d:/网站开发-json"
files_changed = []

# Find all blog and news HTML files
for html_file in glob.glob(os.path.join(base_dir, "pages/blog*.html"), recursive=True):
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # 1. Remove "Target: US & Canada Developers" from articles
    content = content.replace('| <strong>Target:</strong> US & Canada Developers', '')
    content = content.replace('| <strong>Target:</strong> Global Developers', '')
    
    # 2. Fix meta description - remove "for US developers"
    content = content.replace(
        'Learn AI workflows, API development patterns, and structured data techniques. Expert guides on JSON tips and modern web development practices.',
        'Learn AI workflows, API development patterns, and structured data techniques. Expert guides on JSON tips and modern web development.'
    )
    
    # 3. Fix meta author
    content = content.replace(
        'AI JSON - JSON Tools for US Developers',
        'AI JSON - Free JSON Tools for Developers'
    )
    
    # 4. Fix JSON-LD - remove areaServed restriction
    content = content.replace(
        '"areaServed": {"@type": "Country", "name": "United States"}',
        '"audience": {"@type": "Audience", "name": "Software Developers"}'
    )
    
    # 5. Fix Twitter description
    content = content.replace(
        'Expert guides on JSON practices, AI workflows, and API development patterns for US developers.',
        'Expert guides on JSON practices, AI workflows, and API development patterns for developers worldwide.'
    )
    
    # 6. Fix OG description
    content = content.replace(
        'Expert insights on JSON in modern development, AI workflows, and structured data practices for American developers',
        'Expert insights on JSON in modern development, AI workflows, and structured data practices'
    )
    
    if content != original:
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)
        files_changed.append(html_file)
        print(f"Fixed: {html_file}")

# Also fix main blog.html
blog_main = os.path.join(base_dir, "pages/blog.html")
if os.path.exists(blog_main):
    with open(blog_main, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Fix meta description
    content = content.replace(
        'JSON practices for US developers. Learn AI workflows, API development patterns, and structured data techniques. Expert guides on JSON tips and modern web development practices.',
        'JSON practices for developers. Learn AI workflows, API development patterns, and structured data techniques. Expert guides on JSON tips and modern web development.'
    )
    
    content = content.replace(
        'AI JSON - JSON Tools for US Developers',
        'AI JSON - Free JSON Tools for Developers'
    )
    
    # Remove geo meta tags from blog
    content = content.replace('<meta name="geo.region" content="US">\n    ', '')
    content = content.replace('<meta name="geo.placename" content="United States">\n    ', '')
    
    # Fix JSON-LD
    content = content.replace(
        '"headline": "AI JSON Tech Blog - For US Developers"',
        '"headline": "AI JSON Tech Blog"'
    )
    content = content.replace(
        '"description": "Expert insights on JSON in modern development, AI workflows, and structured data practices for American developers"',
        '"description": "Expert insights on JSON in modern development, AI workflows, and structured data practices"'
    )
    
    if content != original:
        with open(blog_main, 'w', encoding='utf-8') as f:
            f.write(content)
        files_changed.append(blog_main)
        print(f"Fixed: {blog_main}")

# Fix news.html
news_main = os.path.join(base_dir, "pages/news.html")
if os.path.exists(news_main):
    with open(news_main, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    content = content.replace(
        'Developer trending news for US developers. Daily API trends, JSON utilities updates, and web development industry news. Stay ahead with the latest developer tools and tech updates.',
        'Developer trending news. Daily API trends, JSON utilities updates, and web development industry news. Stay ahead with the latest developer tools and tech updates.'
    )
    
    content = content.replace(
        'AI JSON - JSON Tools for US Developers',
        'AI JSON - Free JSON Tools for Developers'
    )
    
    if content != original:
        with open(news_main, 'w', encoding='utf-8') as f:
            f.write(content)
        files_changed.append(news_main)
        print(f"Fixed: {news_main}")

print(f"\nTotal files changed: {len(files_changed)}")
