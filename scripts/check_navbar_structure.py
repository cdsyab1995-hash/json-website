import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')

pages_dir = r'd:\网站开发-json\pages'
html_files = [f for f in os.listdir(pages_dir) if f.endswith('.html')]

print('=== NAVBAR STRUCTURE CHECK ===')
print('Checking for: Home, Tools (dropdown), Tutorial, Practices, News, About, Changelog, Try Formatter button\n')

results = {}
for fname in sorted(html_files):
    fpath = os.path.join(pages_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check for each nav element
    has_home = 'Home' in content or 'href="../index.html"' in content or 'href="index.html"' in content
    has_tools_dropdown = 'nav-dropdown' in content and 'Tools' in content
    has_tools_flat = 'Tools' in content and 'nav-dropdown' not in content
    has_tutorial = 'Tutorial' in content
    has_practices = 'Practices' in content
    has_news = 'News' in content
    has_about = 'About' in content
    has_changelog = 'Changelog' in content
    has_try_formatter = 'Try Formatter' in content or 'Try Formatter' in content
    
    results[fname] = {
        'home': has_home,
        'tools_dropdown': has_tools_dropdown,
        'tools_flat': has_tools_flat,
        'tutorial': has_tutorial,
        'practices': has_practices,
        'news': has_news,
        'about': has_about,
        'changelog': has_changelog,
        'try_formatter': has_try_formatter
    }
    
    status = []
    if has_tools_dropdown: status.append('Tools↓')
    elif has_tools_flat: status.append('Tools=')
    else: status.append('NO Tools')
    
    if has_tutorial: status.append('Tutorial')
    if has_practices: status.append('Practices')
    if has_news: status.append('News')
    if has_about: status.append('About')
    if has_changelog: status.append('Changelog')
    if has_try_formatter: status.append('TryFmt')
    
    print(f'{fname:35} | {" | ".join(status)}')

# Summary of inconsistencies
print('\n=== INCONSISTENCIES ===')
tutorial_pages = [f for f, r in results.items() if r['tutorial']]
no_tutorial_pages = [f for f, r in results.items() if not r['tutorial']]

if len(tutorial_pages) != len(html_files):
    print(f'Tutorial link inconsistent:')
    print(f'  HAS Tutorial ({len(tutorial_pages)}): {", ".join(tutorial_pages[:5])}{"..." if len(tutorial_pages) > 5 else ""}')
    print(f'  NO Tutorial ({len(no_tutorial_pages)}): {", ".join(no_tutorial_pages[:5])}{"..." if len(no_tutorial_pages) > 5 else ""}')

# Check Tools dropdown consistency
dropdown_pages = [f for f, r in results.items() if r['tools_dropdown']]
flat_pages = [f for f, r in results.items() if r['tools_flat']]
no_tools_pages = [f for f, r in results.items() if not r['tools_dropdown'] and not r['tools_flat']]

print(f'\nTools nav structure:')
print(f'  Dropdown: {len(dropdown_pages)} pages')
print(f'  Flat list: {len(flat_pages)} pages')
if flat_pages:
    print(f'    Flat pages: {", ".join(flat_pages)}')
print(f'  No Tools: {len(no_tools_pages)} pages')
if no_tools_pages:
    print(f'    Missing: {", ".join(no_tools_pages)}')
