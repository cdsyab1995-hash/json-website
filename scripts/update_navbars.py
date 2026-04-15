#!/usr/bin/env python3
"""Batch update navigation bars in tool pages"""
import re
import os

# Pages to update (excluding format.html which is already updated)
pages = [
    'escape.html', 'extract.html', 'sort.html', 'clean.html',
    'xml.html', 'yaml.html', 'viewer.html', 'json2csv.html', 'compare.html'
]

# Navigation dropdown HTML template - tools section
def get_nav_dropdown():
    return '''            <!-- Tools Dropdown -->
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
                    <a href="format.html" class="nav-link">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <polyline points="4 7 4 4 20 4 20 7"></polyline>
                            <line x1="9" y1="20" x2="15" y2="20"></line>
                            <line x1="12" y1="4" x2="12" y2="20"></line>
                        </svg>
                        Format
                    </a>
                    <a href="escape.html" class="nav-link">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <polyline points="16 18 22 12 16 6"></polyline>
                            <polyline points="8 6 2 12 8 18"></polyline>
                        </svg>
                        Escape
                    </a>
                    <a href="extract.html" class="nav-link">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <circle cx="11" cy="11" r="8"></circle>
                            <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                        </svg>
                        Extract
                    </a>
                    <a href="sort.html" class="nav-link">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <line x1="12" y1="5" x2="12" y2="19"></line>
                            <polyline points="19 12 12 19 5 12"></polyline>
                        </svg>
                        Sort
                    </a>
                    <a href="clean.html" class="nav-link">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"></path>
                        </svg>
                        Clean
                    </a>
                    <a href="xml.html" class="nav-link">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                            <polyline points="14 2 14 8 20 8"></polyline>
                        </svg>
                        XML
                    </a>
                    <a href="yaml.html" class="nav-link">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M4 4l4 16 4-16"></path>
                            <path d="M12 4l4 16"></path>
                        </svg>
                        YAML
                    </a>
                    <a href="viewer.html" class="nav-link">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path>
                            <circle cx="12" cy="12" r="3"></circle>
                        </svg>
                        Viewer
                    </a>
                    <a href="json2csv.html" class="nav-link">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                            <polyline points="14 2 14 8 20 8"></polyline>
                            <line x1="8" y1="13" x2="16" y2="13"></line>
                            <line x1="8" y1="17" x2="16" y2="17"></line>
                        </svg>
                        CSV
                    </a>
                    <a href="compare.html" class="nav-link">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M16 3h5v5"></path>
                            <path d="M8 3H3v5"></path>
                            <path d="M21 3l-7 7"></path>
                            <path d="M3 3l7 7"></path>
                            <path d="M16 21h5v-5"></path>
                            <path d="M8 21H3v-5"></path>
                            <path d="M21 21l-7-7"></path>
                            <path d="M3 21l7-7"></path>
                        </svg>
                        Compare
                    </a>
                </div>
            </div>'''

# Static nav links (Tutorial, News, About, CTA)
def get_static_nav():
    return '''            <a href="blog.html" class="nav-link">
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
            </a>'''

# Home link
def get_home_link(active=False):
    return f'''<a href="../index.html" class="nav-link">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path>
                    <polyline points="9 22 9 12 15 12 15 22"></polyline>
                </svg>
                Home
            </a>'''

# Pattern to find the navbar links section
old_nav_pattern = r'<div class="navbar-links">.*?</div>\s*</nav>'

def get_tool_name(page):
    """Get tool name for active state"""
    name = page.replace('.html', '')
    names = {
        'escape': 'Escape',
        'extract': 'Extract', 
        'sort': 'Sort',
        'clean': 'Clean',
        'xml': 'XML',
        'yaml': 'YAML',
        'viewer': 'Viewer',
        'json2csv': 'CSV',
        'compare': 'Compare'
    }
    return names.get(name, name.capitalize())

def build_new_navlinks(page):
    """Build new nav-links div for the page"""
    tool_name = get_tool_name(page)
    
    # Build nav dropdown with active state
    dropdown = get_nav_dropdown()
    # Mark the current tool as active
    dropdown = dropdown.replace('href="' + page + '"', 'href="' + page + '" class="nav-link active"')
    
    new_navlinks = f'''<div class="navbar-links">
{get_home_link()}
{dropdown}
{get_static_nav()}
        </div>'''
    return new_navlinks

def update_page(filepath):
    """Update a single page's navigation"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find and replace the navbar-links section
    # Match from <div class="navbar-links"> to the closing </div> before </nav>
    pattern = r'(<div class="navbar-links">)(.*?)(</div>\s*</nav>)'
    match = re.search(pattern, content, re.DOTALL)
    
    if not match:
        print(f"  [SKIP] Could not find navbar-links in {filepath}")
        return False
    
    # Build new navlinks
    new_navlinks = build_new_navlinks(os.path.basename(filepath))
    
    # Replace
    new_content = content[:match.start()] + new_navlinks + content[match.end():]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"  [OK] Updated {filepath}")
    return True

def main():
    base_dir = r'd:\网站开发-json\pages'
    
    print("Updating tool page navigation bars...\n")
    
    for page in pages:
        filepath = os.path.join(base_dir, page)
        if os.path.exists(filepath):
            update_page(filepath)
        else:
            print(f"  [MISSING] {filepath}")
    
    print("\nDone!")

if __name__ == '__main__':
    main()
