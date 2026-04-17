#!/usr/bin/env python3
"""Add theme toggle button to all pages"""
import os
import re

def add_theme_toggle(fp):
    """Add theme toggle button to a page"""
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if already has theme toggle
    if 'theme-toggle' in content:
        return False, 'Already has theme toggle'

    # Find the CTA button location: navbar-cta
    cta_pattern = r'(<a href="[^"]*format\.html" class="nav-link navbar-cta")'

    if not re.search(cta_pattern, content):
        return False, 'No CTA button found'

    # Theme toggle HTML
    theme_toggle = '''<!-- Theme Toggle -->
<button class="theme-toggle" id="themeToggle" aria-label="Toggle theme" title="Toggle theme">
    <svg class="icon-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>
    </svg>
    <svg class="icon-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <circle cx="12" cy="12" r="5"></circle>
        <line x1="12" y1="1" x2="12" y2="3"></line>
        <line x1="12" y1="21" x2="12" y2="23"></line>
        <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line>
        <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line>
        <line x1="1" y1="12" x2="3" y2="12"></line>
        <line x1="21" y1="12" x2="23" y2="12"></line>
        <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line>
        <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>
    </svg>
</button>
'''

    # Insert before CTA button
    new_content = re.sub(
        cta_pattern,
        theme_toggle + r'\1',
        content
    )

    if new_content != content:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True, 'Added theme toggle'
    else:
        return False, 'Pattern not matched'

def add_theme_script(fp):
    """Add theme toggle JavaScript to page"""
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if already has theme script
    if 'initTheme()' in content or 'themeToggle' in content and 'localStorage' in content:
        return False, 'Already has theme script'

    # Theme toggle JavaScript
    theme_script = '''
// Theme Toggle
(function() {
    var toggle = document.getElementById('themeToggle');
    if (!toggle) return;

    // Apply saved theme or system preference
    function applyTheme(theme) {
        if (theme === 'light') {
            document.documentElement.setAttribute('data-theme', 'light');
        } else {
            document.documentElement.removeAttribute('data-theme');
        }
    }

    // Initialize theme
    function initTheme() {
        var saved = localStorage.getItem('theme');
        if (saved) {
            applyTheme(saved);
        } else if (window.matchMedia && window.matchMedia('(prefers-color-scheme: light)').matches) {
            applyTheme('light');
        }
    }

    // Toggle theme
    toggle.addEventListener('click', function() {
        var current = document.documentElement.getAttribute('data-theme');
        var next = current === 'light' ? 'dark' : 'light';
        applyTheme(next);
        localStorage.setItem('theme', next);
    });

    initTheme();
})();
'''

    # Find </body> and insert before
    body_end = content.rfind('</body>')
    if body_end > 0:
        new_content = content[:body_end] + '<script>' + theme_script + '<\\/script>' + content[body_end:]
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True, 'Added theme script'
    else:
        return False, 'No </body> found'

def main():
    pages_dir = r'd:\网站开发-json\pages'
    root_files = [r'd:\网站开发-json\index.html']

    all_pages = [(fp, os.path.basename(fp)) for fp in root_files]
    for f in sorted(os.listdir(pages_dir)):
        if f.endswith('.html'):
            all_pages.append((os.path.join(pages_dir, f), f))

    print('=== Adding Theme Toggle ===\n')

    # First pass: add button
    print('Pass 1: Adding theme toggle button...')
    for fp, name in all_pages:
        changed, msg = add_theme_toggle(fp)
        if changed:
            print(f'  [ADDED] {name}')
        elif 'Already' in msg:
            print(f'  [SKIP] {name}: {msg}')
        else:
            print(f'  [WARN] {name}: {msg}')

    print('\nPass 2: Adding theme JavaScript...')
    for fp, name in all_pages:
        changed, msg = add_theme_script(fp)
        if changed:
            print(f'  [ADDED] {name}')
        else:
            print(f'  [SKIP] {name}: {msg}')

    print('\nDone!')

if __name__ == '__main__':
    main()
