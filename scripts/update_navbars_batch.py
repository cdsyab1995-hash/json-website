#!/usr/bin/env python3
"""Batch update remaining tool pages with dropdown navigation"""
import os
import re

BASE_DIR = r'd:\网站开发-json\pages'

# The new navbar template (without Tools dropdown - will be added per page)
NAVBAR_END = '''            <a href="blog.html" class="nav-link">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path>
                    <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path>
                </svg>
                Tutorial
            </a>
            <a href="news.html" class="nav-link">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"></path>
                </svg>
                News
            </a>
            <a href="about.html" class="nav-link">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <circle cx="12" cy="12" r="10"></circle>
                    <line x1="12" y1="16" x2="12" y2="12"></line>
                    <line x1="12" y1="8" x2="12.01" y2="8"></line>
                </svg>
                About
            </a>
            <!-- CTA Button -->
            <a href="format.html" class="nav-link navbar-cta">
                Try Formatter
            </a>
        </div>
    </nav>'''

def get_tools_dropdown(active_tool):
    """Generate the Tools dropdown with active state for the current tool"""
    tools = [
        ('format.html', 'Format', '''<polyline points="4 7 4 4 20 4 20 7"></polyline>
                            <line x1="9" y1="20" x2="15" y2="20"></line>
                            <line x1="12" y1="4" x2="12" y2="20"></line>'''),
        ('escape.html', 'Escape', '''<polyline points="16 18 22 12 16 6"></polyline>
                            <polyline points="8 6 2 12 8 18"></polyline>'''),
        ('extract.html', 'Extract', '''<circle cx="11" cy="11" r="8"></circle>
                            <line x1="21" y1="21" x2="16.65" y2="16.65"></line>'''),
        ('sort.html', 'Sort', '''<line x1="12" y1="5" x2="12" y2="19"></line>
                            <polyline points="19 12 12 19 5 12"></polyline>'''),
        ('clean.html', 'Clean', '''<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"></path>'''),
        ('xml.html', 'XML', '''<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                            <polyline points="14 2 14 8 20 8"></polyline>'''),
        ('yaml.html', 'YAML', '''<path d="M4 4l4 16 4-16"></path>
                            <path d="M12 4l4 16"></path>'''),
        ('viewer.html', 'Viewer', '''<path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path>
                            <circle cx="12" cy="12" r="3"></circle>'''),
        ('json2csv.html', 'CSV', '''<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                            <polyline points="14 2 14 8 20 8"></polyline>
                            <line x1="8" y1="13" x2="16" y2="13"></line>
                            <line x1="8" y1="17" x2="16" y2="17"></line>'''),
        ('compare.html', 'Compare', '''<path d="M16 3h5v5"></path>
                            <path d="M8 3H3v5"></path>
                            <path d="M21 3l-7 7"></path>
                            <path d="M3 3l7 7"></path>
                            <path d="M16 21h5v-5"></path>
                            <path d="M8 21H3v-5"></path>
                            <path d="M21 21l-7-7"></path>
                            <path d="M3 21l7-7"></path>'''),
    ]
    
    dropdown_items = []
    for href, name, svg_path in tools:
        active_class = ' class="nav-link active"' if href == active_tool else ' class="nav-link"'
        dropdown_items.append(f'''<a href="{href}"{active_class}>
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            {svg_path}
                        </svg>
                        {name}
                    </a>''')
    
    return f'''            <!-- Tools Dropdown -->
            <div class="nav-dropdown">
                <a href="#" class="nav-link nav-dropdown-toggle">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <rect x="3" y="3" width="7" height="7"></rect>
                        <rect x="14" y="3" width="7" height="7"></rect>
                        <rect x="14" y="14" width="7" height="7"></rect>
                        <rect x="3" y="14" width="7" height="7"></rect>
                    </svg>
                    Tools
                </a>
                <div class="nav-dropdown-menu">
                    {''.join(dropdown_items)}
                </div>
            </div>'''

def get_home_link():
    return '''            <a href="../index.html" class="nav-link">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path>
                    <polyline points="9 22 9 12 15 12 15 22"></polyline>
                </svg>
                Home
            </a>'''

def update_page(filepath, active_tool):
    """Update a page with new dropdown navigation"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Build new navbar
    new_navbar = f'''        <div class="navbar-links">
{get_home_link()}
{get_tools_dropdown(active_tool)}
{NAVBAR_END}'''
    
    # Find and replace navbar-links section
    pattern = r'<div class="navbar-links">.*?</div>\s*</nav>'
    match = re.search(pattern, content, re.DOTALL)
    
    if match:
        new_content = content[:match.start()] + new_navbar + content[match.end():]
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'[OK] {os.path.basename(filepath)}')
        return True
    else:
        print(f'[SKIP] {os.path.basename(filepath)} - no navbar found')
        return False

def main():
    # Pages to update (map filename -> active tool)
    pages = {
        'sort.html': 'sort.html',
        'clean.html': 'clean.html',
        'xml.html': 'xml.html',
        'yaml.html': 'yaml.html',
        'viewer.html': 'viewer.html',
        'json2csv.html': 'json2csv.html',
        'compare.html': 'compare.html',
    }
    
    print('Updating remaining tool pages with dropdown navigation...\n')
    
    for page, active_tool in pages.items():
        filepath = os.path.join(BASE_DIR, page)
        if os.path.exists(filepath):
            update_page(filepath, active_tool)
        else:
            print(f'[MISSING] {page}')
    
    print('\nDone!')

if __name__ == '__main__':
    main()
