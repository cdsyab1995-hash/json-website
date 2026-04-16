#!/usr/bin/env python3
"""
更新 sitemap.xml 添加 P1 工具页面
"""
import os

SITEMAP = r'd:\网站开发-json\sitemap.xml'

NEW_URLS = '''    <url>
        <loc>https://www.aijsons.com/pages/jwt-decoder.html</loc>
        <changefreq>monthly</changefreq>
        <priority>0.8</priority>
    </url>
    <url>
        <loc>https://www.aijsons.com/pages/hash-generator.html</loc>
        <changefreq>monthly</changefreq>
        <priority>0.8</priority>
    </url>
    <url>
        <loc>https://www.aijsons.com/pages/uuid-generator.html</loc>
        <changefreq>monthly</changefreq>
        <priority>0.8</priority>
    </url>'''

def update_sitemap():
    with open(SITEMAP, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 检查是否已有这些 URL
    if 'jwt-decoder.html' in content:
        print('[OK] sitemap.xml already has P1 tool URLs')
        return False
    
    # 在 closing </urlset> 前添加新 URL
    new_content = content.replace('</urlset>', NEW_URLS + '\n</urlset>')
    
    with open(SITEMAP, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print('[OK] Updated sitemap.xml with P1 tool URLs')
    return True

if __name__ == '__main__':
    update_sitemap()
