#!/usr/bin/env python3
"""Update sitemap.xml with P0 tools"""

fp = r'd:\网站开发-json\sitemap.xml'
with open(fp, 'r', encoding='utf-8') as f:
    content = f.read()

# Check if already has P0 tools
if 'regex-tester' in content:
    print('[SKIP] sitemap.xml already has P0 tools')
else:
    # Add new URLs before </urlset>
    new_urls = '''  <url>
    <loc>https://www.aijsons.com/pages/regex-tester.html</loc>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://www.aijsons.com/pages/base64.html</loc>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://www.aijsons.com/pages/url-encoder.html</loc>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
'''
    
    content = content.replace('</urlset>', new_urls + '</urlset>')
    
    with open(fp, 'w', encoding='utf-8') as f:
        f.write(content)
    print('[OK] sitemap.xml updated with 3 new URLs')
