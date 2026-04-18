#!/usr/bin/env python3
"""Fix navbar order: About/Changelog swap, add Try Formatter, add Home where missing"""
import os
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

pages_dir = r'd:\网站开发-json\pages'

def fix_navbar_order(content, fname):
    """Fix navbar order issues"""
    changes = []
    
    # 1. Fix About/Changelog order - swap if Changelog comes before About
    # Pattern: ...News</a>...Changelog...</a>...About...</a>...
    # Should be: ...News</a>...About...</a>...Changelog...</a>...
    
    # Find the section between "News" and "Try Formatter" (or end)
    news_match = re.search(r'(News</a>)(.*?)(Try Formatter</a>|</div>\s*</div>\s*</div>\s*</nav>)', content, re.DOTALL)
    if news_match:
        between = news_match.group(2)
        # Check if Changelog comes before About
        changelog_pos = between.find('Changelog')
        about_pos = between.find('About')
        
        if changelog_pos >= 0 and about_pos >= 0 and changelog_pos < about_pos:
            # Swap them
            # Extract chunks
            before_changelog = between[:changelog_pos]
            changelog_chunk = between[changelog_pos:changelog_pos+len('Changelog</a>')]
            between_chunks = between[changelog_pos+len('Changelog</a>'):about_pos]
            about_chunk = between[about_pos:about_pos+len('About</a>')]
            
            new_between = before_changelog + about_chunk + between_chunks + changelog_chunk
            new_content = news_match.group(1) + new_between + news_match.group(3)
            
            # Reconstruct
            content = content[:news_match.start()] + new_content + content[news_match.end():]
            changes.append(f"{fname}: swapped About/Changelog order")
    
    # 2. Add "Try Formatter" if missing and About/Changelog exist
    # Find if Try Formatter exists
    if 'Try Formatter' not in content:
        # Add it after Changelog
        changelog_match = re.search(r'(Changelog</a>)(</div>\s*</div>\s*</div>\s*</nav>|</div>\s*</nav>)', content)
        if changelog_match:
            try_formatter = '<a href="format.html" class="nav-link cta">Try Formatter</a>'
            content = content[:changelog_match.end()] + '\n' + try_formatter + content[changelog_match.end():]
            changes.append(f"{fname}: added Try Formatter")
    
    # 3. Add Home if missing
    if 'Home</a>' not in content:
        # Find first nav link and prepend Home
        first_link = re.search(r'(<div class="navbar-links">)(\s*<a href)', content)
        if first_link:
            home_link = '\n            <a href="../index.html" class="nav-link">\n                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n                    <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path>\n                    <polyline points="9 22 9 12 15 12 15 22"></polyline>\n                </svg>\n                Home\n            </a>'
            content = content[:first_link.end()] + home_link + content[first_link.end():]
            changes.append(f"{fname}: added Home link")
    
    return content, changes

# Process all pages
html_files = sorted([f for f in os.listdir(pages_dir) if f.endswith('.html')])

all_changes = []
for fname in html_files:
    fpath = os.path.join(pages_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content, changes = fix_navbar_order(content, fname)
    
    if changes:
        all_changes.extend(changes)
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed: {fname}")
        for c in changes:
            print(f"  - {c}")
    else:
        print(f"OK: {fname}")

print(f"\nTotal: {len(all_changes)} fixes applied")
