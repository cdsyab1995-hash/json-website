#!/usr/bin/env python3
"""Update sitemap.xml with missing URLs and correct dates"""

sitemap_path = r"d:\网站开发-json\sitemap.xml"
today = "2026-04-20"

# Missing blog articles to add
missing_articles = [
    ("json-edge-computing-cloudflare-workers.html", "0.8"),
    ("jwt-security-best-practices-2026.html", "0.8"),
    ("postgresql-jsonb-vs-mongodb-document-store.html", "0.8"),
]

# Read current sitemap
with open(sitemap_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Check for missing articles
for article, priority in missing_articles:
    url = f"https://www.aijsons.com/pages/blog/{article}"
    if url not in content:
        print(f"Adding: {article}")
        # Find insertion point (before </urlset>)
        insert_point = content.find("</urlset>")
        new_entry = f"""
  <url>
    <loc>{url}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>{priority}</priority>
  </url>
"""
        content = content[:insert_point] + new_entry + content[insert_point:]
    else:
        print(f"Already exists: {article}")

# Update all lastmod dates to today
import re
content = re.sub(r'<lastmod>\d{4}-\d{2}-\d{2}</lastmod>', f'<lastmod>{today}</lastmod>', content)

# Write back
with open(sitemap_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\nUpdated sitemap.xml with {today} dates")
print("Added missing articles and updated all lastmod values")
