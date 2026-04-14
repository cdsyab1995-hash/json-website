#!/usr/bin/env python3
"""Push website changes to GitHub using direct API calls"""
import base64
import json
import os
import time
from urllib.request import urlopen, Request
from urllib.error import HTTPError

# GitHub Token
TOKEN = "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"
REPO = "cdsyab1995-hash/json-website"
BRANCH = "main"

def github_api(method, endpoint, data=None):
    """Make GitHub API request"""
    url = f"https://api.github.com/{endpoint}"
    headers = {
        "Authorization": f"token {TOKEN}",
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "AIJSON-Pusher"
    }
    
    req = Request(url, headers=headers, method=method)
    if data:
        import urllib.parse
        req.data = json.dumps(data).encode('utf-8')
        req.add_header("Content-Type", "application/json")
    
    try:
        with urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode('utf-8'))
    except HTTPError as e:
        error_body = e.read().decode('utf-8') if e.fp else ""
        print(f"[ERROR] GitHub API error {e.code}: {error_body[:200]}")
        raise

def get_file_sha(path):
    """Get file SHA for update"""
    try:
        result = github_api("GET", f"repos/{REPO}/contents/{path}?ref={BRANCH}")
        return result.get('sha')
    except:
        return None

def push_file(path, content, message):
    """Push a single file to GitHub"""
    sha = get_file_sha(path)
    
    data = {
        "message": message,
        "content": base64.b64encode(content.encode('utf-8')).decode('utf-8'),
        "branch": BRANCH
    }
    if sha:
        data["sha"] = sha
    
    try:
        result = github_api("PUT", f"repos/{REPO}/contents/{path}", data)
        print(f"[OK] {path}")
        return True
    except Exception as e:
        print(f"[FAIL] {path}: {e}")
        return False

def main():
    website_dir = r"d:\网站开发-json"
    
    # Files to push
    files_to_push = [
        "index.html",
        "pages/format.html",
        "pages/escape.html",
        "pages/extract.html",
        "pages/sort.html",
        "pages/clean.html",
        "pages/xml.html",
        "pages/yaml.html",
        "pages/viewer.html",
        "pages/json2csv.html",
        "pages/compare.html",
        "pages/blog.html",
        "pages/news.html",
    ]
    
    print("Pushing SEO-optimized pages to GitHub...")
    print("=" * 50)
    
    for file_path in files_to_push:
        full_path = os.path.join(website_dir, file_path)
        if os.path.exists(full_path):
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()
            push_file(file_path, content, f"SEO optimization: Update meta tags with low-competition keywords")
            time.sleep(0.5)  # Rate limiting
        else:
            print(f"[SKIP] {file_path} not found")
    
    print("=" * 50)
    print("Done!")

if __name__ == "__main__":
    main()
