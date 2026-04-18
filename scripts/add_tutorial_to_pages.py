import sys, os
sys.stdout.reconfigure(encoding='utf-8')

pages_dir = r'd:\网站开发-json\pages'
fixed_count = 0

for fname in ['blog.html', 'hash-generator.html', 'uuid-generator.html']:
    fpath = os.path.join(pages_dir, fname)
    if not os.path.exists(fpath):
        print(f'Not found: {fname}')
        continue
    
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the nav-dropdown section end and add Tutorial link after it
    # Pattern: after nav-dropdown closes, before Practices link
    old_pattern = '''                </div>
            </div>
            <a href="best-practices.html" class="nav-link">'''
    
    new_pattern = '''                </div>
            </div>
            <a href="blog.html" class="nav-link">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path>
                    <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path>
                </svg>
                Tutorial
            </a>
            <a href="best-practices.html" class="nav-link">'''
    
    if old_pattern in content:
        new_content = content.replace(old_pattern, new_pattern)
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        fixed_count += 1
        print(f'Fixed: {fname} - added Tutorial link')
    else:
        print(f'Pattern not found in: {fname}')

print(f'\nTotal fixed: {fixed_count}')
