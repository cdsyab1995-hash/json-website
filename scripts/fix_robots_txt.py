#!/usr/bin/env python3
"""Fix robots.txt - remove US targeting comments"""

robots_path = r"d:\网站开发-json\robots.txt"

with open(robots_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove US-specific comments and content
new_content = """# robots.txt for AI JSON - Free JSON Tools for Developers
# https://aijsons.com/

User-agent: *
Allow: /

Sitemap: https://aijsons.com/sitemap.xml

Crawl-delay: 1
"""

with open(robots_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("robots.txt cleaned!")
