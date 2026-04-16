#!/usr/bin/env python3
"""检查所有页面的导航栏一致性"""
import os
import re
from pathlib import Path

def get_navbar_links(html_file):
    """从HTML文件内容中提取导航栏链接"""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    links = []
    hrefs = re.findall(r'<a href="([^"#]+)"', content)
    
    for href in hrefs:
        if href.startswith('javascript:') or href.startswith('#'):
            continue
        filename = href.split('/')[-1]
        if filename:
            links.append(filename)
    
    return links, content

def main():
    pages_dir = Path('d:/网站开发-json/pages')
    
    issues = []
    all_pages = []
    
    all_page_names = [
        'index.html', 'format.html', 'escape.html', 'extract.html',
        'sort.html', 'clean.html', 'xml.html', 'yaml.html',
        'viewer.html', 'json2csv.html', 'compare.html',
        'blog.html', 'best-practices.html', 'news.html',
        'changelog.html', 'about.html'
    ]
    
    for html_file in sorted(pages_dir.rglob('*.html')):
        rel_path = str(html_file.relative_to(pages_dir.parent))
        links, content = get_navbar_links(html_file)
        
        nav_count = len(links)
        has_dropdown = 'nav-dropdown' in content
        
        missing = []
        for page in all_page_names:
            if page not in links:
                missing.append(page)
        
        all_pages.append((rel_path, nav_count, has_dropdown, missing))
        if missing:
            issues.append((rel_path, missing))
    
    print("=" * 80)
    print("Navigation Bar Consistency Report")
    print("=" * 80)
    
    print(f"\nTotal pages: {len(all_pages)}")
    print(f"Pages with missing links: {len(issues)}")
    
    if issues:
        print("\n" + "-" * 80)
        print("Pages with MISSING links:")
        print("-" * 80)
        for page, missing in sorted(issues):
            print(f"\n  {page}:")
            for link in missing:
                print(f"    - {link}")
    else:
        print("\n[OK] All pages have complete navigation!")
    
    print("\n" + "-" * 80)
    print("All pages summary:")
    print("-" * 80)
    for page, count, dropdown, missing in sorted(all_pages):
        status = "[MISSING: " + ",".join(missing) + "]" if missing else "[OK]"
        dropdown_str = "[dropdown]" if dropdown else ""
        print(f"  {count:3d} links {dropdown_str:10s} {status:50s} {page}")

if __name__ == '__main__':
    main()
