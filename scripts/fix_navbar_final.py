#!/usr/bin/env python3
"""Fix navbar order - proper implementation"""
import os
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

pages_dir = r'd:\网站开发-json\pages'
root_dir = r'd:\网站开发-json'

# First fix root index.html
print("Fixing root index.html...")
root_index = os.path.join(root_dir, 'index.html')
with open(root_index, 'r', encoding='utf-8') as f:
    content = f.read()

# Root index.html: check Tools dropdown links
# They should be 'format.html' not 'pages/format.html'
if 'href="pages/format.html"' in content:
    content = content.replace('href="pages/format.html"', 'href="format.html"')
    content = content.replace('href="pages/escape.html"', 'href="escape.html"')
    content = content.replace('href="pages/extract.html"', 'href="extract.html"')
    content = content.replace('href="pages/sort.html"', 'href="sort.html"')
    content = content.replace('href="pages/clean.html"', 'href="clean.html"')
    content = content.replace('href="pages/xml.html"', 'href="xml.html"')
    content = content.replace('href="pages/yaml.html"', 'href="yaml.html"')
    content = content.replace('href="pages/viewer.html"', 'href="viewer.html"')
    content = content.replace('href="pages/json2csv.html"', 'href="json2csv.html"')
    content = content.replace('href="pages/compare.html"', 'href="compare.html"')
    content = content.replace('href="pages/regex-tester.html"', 'href="regex-tester.html"')
    content = content.replace('href="pages/base64.html"', 'href="base64.html"')
    content = content.replace('href="pages/url-encoder.html"', 'href="url-encoder.html"')
    content = content.replace('href="pages/csv-to-excel.html"', 'href="csv-to-excel.html"')
    content = content.replace('href="pages/excel-remove-duplicates.html"', 'href="excel-remove-duplicates.html"')
    content = content.replace('href="pages/merge-csv.html"', 'href="merge-csv.html"')
    content = content.replace('href="pages/batch-file-renamer.html"', 'href="batch-file-renamer.html"')
    content = content.replace('href="pages/pdf-split.html"', 'href="pdf-split.html"')
    content = content.replace('href="pages/timestamp-converter.html"', 'href="timestamp-converter.html"')
    content = content.replace('href="pages/css-minifier.html"', 'href="css-minifier.html"')
    content = content.replace('href="pages/html-encoder.html"', 'href="html-encoder.html"')
    print("  Fixed Tools dropdown links in root index.html")
    with open(root_index, 'w', encoding='utf-8') as f:
        f.write(content)

# Now process all pages
html_files = sorted([f for f in os.listdir(pages_dir) if f.endswith('.html')])

total_fixes = 0
for fname in html_files:
    fpath = os.path.join(pages_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    changes = []
    
    # Check if navbar exists
    if 'class="navbar"' not in content:
        print(f"SKIP (no navbar): {fname}")
        continue
    
    # Fix 1: Swap Changelog and About order
    # Pattern: ...News</a>...<a...>Changelog</a>...<a...>About</a>...
    # Should be: ...News</a>...<a...>About</a>...<a...>Changelog</a>...
    
    # Find Changelog link
    changelog_pattern = r'(<a href="changelog\.html" class="nav-link">.*?</a>)'
    about_pattern = r'(<a href="about\.html" class="nav-link">.*?</a>)'
    
    changelog_match = re.search(changelog_pattern, content, re.DOTALL)
    about_match = re.search(about_pattern, content, re.DOTALL)
    
    if changelog_match and about_match:
        if changelog_match.start() < about_match.start():
            # Changelog comes before About - swap them
            # Extract the chunks
            before = content[:changelog_match.start()]
            cg = changelog_match.group(1)
            between = content[changelog_match.end():about_match.start()]
            ab = about_match.group(1)
            after = content[about_match.end():]
            
            # Rebuild: before + About + between + Changelog + after
            content = before + ab + between + cg + after
            changes.append("swapped About/Changelog order")
    
    # Fix 2: Remove duplicate Home links (caused by previous script)
    home_pattern = r'(<a href="[^"]*index\.html" class="nav-link">.*?Home.*?</a>\s*)'
    home_matches = list(re.finditer(home_pattern, content, re.DOTALL))
    if len(home_matches) > 1:
        # Keep only the first one, remove others
        for i in range(len(home_matches) - 1, 0, -1):
            content = content[:home_matches[i].start()] + content[home_matches[i].end():]
        changes.append("removed duplicate Home links")
    
    # Fix 3: Add Home if missing (but not duplicate)
    if '>Home<' not in content or '>Home </a>' not in content:
        # Check if any nav-link exists
        if '<a href=' in content and 'class="nav-link"' in content:
            # Find the Tools dropdown and add Home before it
            tools_match = re.search(r'(<!-- Tools Dropdown -->|<div class="nav-dropdown">)', content)
            if tools_match:
                home_link = '''            <a href="../index.html" class="nav-link">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path>
                    <polyline points="9 22 9 12 15 12 15 22"></polyline>
                </svg>
                Home
            </a>
'''
                content = content[:tools_match.start()] + home_link + content[tools_match.start():]
                changes.append("added Home link")
    
    # Fix 4: Add Try Formatter if missing
    if '>Try Formatter<' not in content and 'Try Formatter' not in content:
        # Add before </div></div></nav>
        if '</nav>' in content:
            cta = '            <a href="format.html" class="nav-link cta">Try Formatter</a>\n'
            content = content.replace('</nav>', cta + '</nav>')
            changes.append("added Try Formatter")
    
    if changes:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        total_fixes += len(changes)
        print(f"Fixed: {fname} - {', '.join(changes)}")

print(f"\nTotal: {total_fixes} fixes applied")
