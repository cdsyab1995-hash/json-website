# -*- coding: utf-8 -*-
"""
SEO Audit Script for aijsons.com
Checks for common Google Search Console issues
"""
import requests
from bs4 import BeautifulSoup
import time
import json

BASE_URL = "https://www.aijsons.com"

def check_page(url):
    """Check a single page for SEO issues"""
    try:
        resp = requests.get(url, timeout=10)
        soup = BeautifulSoup(resp.content, 'html.parser')
        
        issues = []
        
        # Check title
        title = soup.find('title')
        if not title:
            issues.append("MISSING: <title> tag")
        elif len(title.text) < 10:
            issues.append(f"WARNING: Title too short: '{title.text}'")
        elif len(title.text) > 60:
            issues.append(f"WARNING: Title too long ({len(title.text)} chars): '{title.text[:50]}...'")
        
        # Check meta description
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        if not meta_desc:
            issues.append("MISSING: meta description")
        elif len(meta_desc.get('content', '')) < 50:
            issues.append(f"WARNING: Meta description too short")
        elif len(meta_desc.get('content', '')) > 160:
            issues.append(f"WARNING: Meta description too long")
        
        # Check canonical
        canonical = soup.find('link', attrs={'rel': 'canonical'})
        if not canonical:
            issues.append("MISSING: canonical URL")
        else:
            canon_url = canonical.get('href', '')
            if not canon_url.startswith('https://'):
                issues.append(f"WARNING: Canonical URL doesn't use HTTPS: {canon_url}")
        
        # Check H1
        h1 = soup.find('h1')
        if not h1:
            issues.append("MISSING: <h1> tag")
        
        # Check Open Graph
        og_title = soup.find('meta', attrs={'property': 'og:title'})
        og_desc = soup.find('meta', attrs={'property': 'og:description'})
        if not og_title:
            issues.append("MISSING: og:title")
        if not og_desc:
            issues.append("MISSING: og:description")
            
        return issues, resp.status_code
    except Exception as e:
        return [f"ERROR: {str(e)}"], 0

# Pages to check
pages_to_check = [
    "/",
    "/tools/json-formatter",
    "/tools/json-escape",
    "/blog",
    "/news",
    "/about",
    "/privacy",
    "/terms"
]

print("=" * 60)
print("SEO Audit Report for aijsons.com")
print("=" * 60)
print()

all_issues = {}

for page in pages_to_check:
    url = BASE_URL + page
    print(f"Checking: {url}")
    issues, status = check_page(url)
    
    if status != 200:
        print(f"  ❌ HTTP {status} - Page not accessible")
        all_issues[page] = [f"HTTP {status}"]
    elif issues:
        print(f"  ⚠️  Found {len(issues)} issues:")
        for issue in issues:
            print(f"     - {issue}")
        all_issues[page] = issues
    else:
        print(f"  ✅ No major issues found")
    
    print()
    time.sleep(0.5)

# Summary
print("=" * 60)
print("SUMMARY")
print("=" * 60)
if all_issues:
    print(f"Total pages with issues: {len(all_issues)}")
    for page, issues in all_issues.items():
        print(f"\n{page}:")
        for issue in issues:
            print(f"  - {issue}")
else:
    print("✅ All checked pages pass basic SEO checks!")
