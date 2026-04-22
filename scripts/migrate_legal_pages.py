#!/usr/bin/env python3
"""
Migrate cookie/privacy/terms pages to use shared navbar.js.
Uses regex to replace the entire nav block with placeholder + navbar.js script.
"""
import re
import os

BASE = r"d:\网站开发-json"

PAGES = [
    os.path.join(BASE, "cookie", "index.html"),
    os.path.join(BASE, "privacy", "index.html"),
    os.path.join(BASE, "terms", "index.html"),
]

def migrate(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Check if already migrated
    if 'id="navbar-placeholder"' in content:
        print(f"[SKIP] Already migrated: {filepath}")
        return True

    # Check old nav exists
    if '<nav class="navbar">' not in content:
        print(f"[WARN] No hardcoded nav found in {filepath}")
        return False

    # Replace the entire nav block: from '<!-- Navigation --> <nav' to '</nav> <!-- Main Content -->'
    # The nav block spans from the nav start to the closing </nav> before main content
    pattern = r'<!-- Navigation --> <nav class="navbar">.*?</nav>(?=\s+<!-- Main Content -->)'
    replacement = '<!-- Navigation -->\n<div id="navbar-placeholder"></div>\n'

    new_content, count = re.subn(pattern, replacement, content, flags=re.DOTALL)
    if count == 0:
        print(f"[WARN] No nav block matched in {filepath}")
        return False

    # Fix relative CSS path: css/styles.css -> /css/styles.css
    new_content = new_content.replace('href="css/styles.css"', 'href="/css/styles.css"')

    # Fix relative JS path: js/app.js -> /js/app.js
    new_content = new_content.replace('src="js/app.js"', 'src="/js/app.js"')

    # Add navbar.js script before app.js
    if '/js/navbar.js' not in new_content:
        new_content = new_content.replace(
            '<script src="/js/app.js"',
            '<script src="/js/navbar.js"></script>\n    <script src="/js/app.js"'
        )

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"[OK] Migrated {filepath} (replaced {count} nav block)")
    return True

def main():
    for page in PAGES:
        migrate(page)

if __name__ == "__main__":
    main()
