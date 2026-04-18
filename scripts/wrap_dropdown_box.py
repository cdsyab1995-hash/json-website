#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Wrap nav-dropdown-menu content with nav-dropdown-menu-box div in all HTML files.
Also need to wrap dropdown links for all pages.
"""
import sys, re, os, glob
sys.stdout.reconfigure(encoding='utf-8')

def wrap_dropdown_box(content, filename):
    """
    Find <div class="nav-dropdown-menu ..."> ... </div>
    and wrap the inner content with <div class="nav-dropdown-menu-box">
    """
    # Pattern: <div class="nav-dropdown-menu..."> ... all links ... </div>
    # The closing </div> is the one that closes the menu, NOT the nav-dropdown container
    
    # Find the nav-dropdown-menu div
    menu_start = re.search(r'<div class="nav-dropdown-menu[^"]*">', content)
    if not menu_start:
        return content, False
    
    start_pos = menu_start.start()
    inner_start = menu_start.end()
    
    # Already wrapped?
    if 'nav-dropdown-menu-box' in content[inner_start:inner_start+60]:
        return content, False
    
    # Find matching closing </div>
    # Count depth
    depth = 1
    pos = inner_start
    while pos < len(content) and depth > 0:
        next_open = content.find('<div', pos)
        next_close = content.find('</div>', pos)
        if next_close == -1:
            break
        if next_open != -1 and next_open < next_close:
            depth += 1
            pos = next_open + 4
        else:
            depth -= 1
            if depth == 0:
                menu_end = next_close
                break
            pos = next_close + 6
    
    if depth != 0:
        print('  WARNING: Could not find matching </div> in ' + filename)
        return content, False
    
    # Get inner content
    inner_content = content[inner_start:menu_end]
    
    # Wrap it
    wrapped = '\n<div class="nav-dropdown-menu-box">' + inner_content + '</div>\n'
    new_content = content[:inner_start] + wrapped + content[menu_end:]
    
    return new_content, True

# Process all HTML files
files = [r'd:\网站开发-json\index.html']
files += glob.glob(r'd:\网站开发-json\pages\*.html')

fixed = 0
for filepath in sorted(files):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content, changed = wrap_dropdown_box(content, os.path.basename(filepath))
    
    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print('FIXED: ' + os.path.basename(filepath))
        fixed += 1
    else:
        # Check if already has box or no dropdown
        if 'nav-dropdown-menu' in content:
            if 'nav-dropdown-menu-box' in content:
                print('SKIP (already wrapped): ' + os.path.basename(filepath))
            else:
                print('WARN (dropdown found but not wrapped): ' + os.path.basename(filepath))

print('\nTotal fixed: ' + str(fixed))
