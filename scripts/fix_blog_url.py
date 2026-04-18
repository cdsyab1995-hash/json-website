import sys, re
sys.stdout.reconfigure(encoding='utf-8')

path = r'd:\网站开发-json\pages\blog.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix 1: Wrong URL concatenation
content = content.replace(
    'aijsons.com/pages/blog.htmlindex.html',
    'aijsons.com/pages/blog/index.html'
)

# Fix 2: The og:url meta tag
content = re.sub(
    r'<meta property="og:url" content="https://www\.aijsons\.com/pages/blog\.html">',
    '<meta property="og:url" content="https://www.aijsons.com/pages/blog.html">',
    content
)

# Fix JSON-LD properly
content = re.sub(
    r'"url":\s*"https://www\.aijsons\.com/pages/blog\.html"',
    '"url": "https://www.aijsons.com/pages/blog.html"',
    content
)

# Fix canonical
content = re.sub(
    r'<link rel="canonical" href="https://www\.aijsons\.com/pages/blog\.html">',
    '<link rel="canonical" href="https://www.aijsons.com/pages/blog.html">',
    content
)

# Check datasets section - if missing, add it
if 'datasets-list' not in content:
    print('datasets-list missing - adding section')
    # Find the templates section and add datasets after it
    templates_end = content.find('<div class="templates-grid"')
    if templates_end > 0:
        # Find the end of the templates section (next h2 or section)
        # Insert datasets section after templates
        datasets_section = '''
        <!-- JSON DATASETS -->
        <section class="container" style="margin: 3rem auto; max-width: 900px;">
            <h2 class="section-title">JSON Datasets</h2>
            <p class="section-description">Real-world JSON datasets for testing, prototyping, and learning.</p>
            <div class="datasets-list">
                <div class="dataset-card">
                    <h3>JSONPlaceholder</h3>
                    <p>Fake data for testing and prototyping. Includes users, posts, comments, todos, and photos APIs.</p>
                    <a href="https://jsonplaceholder.typicode.com/" target="_blank" rel="noopener" class="dataset-link">jsonplaceholder.typicode.com</a>
                </div>
                <div class="dataset-card">
                    <h3>REST Countries</h3>
                    <p>All countries data in JSON format. Get country names, capitals, populations, currencies, languages, and more.</p>
                    <a href="https://restcountries.com/" target="_blank" rel="noopener" class="dataset-link">restcountries.com</a>
                </div>
                <div class="dataset-card">
                    <h3>GitHub Gists API</h3>
                    <p>Explore real JSON files from public GitHub Gists. Great for finding configuration files and data samples.</p>
                    <a href="https://api.github.com/gists" target="_blank" rel="noopener" class="dataset-link">api.github.com/gists</a>
                </div>
            </div>
        </section>
'''
        # Find the closing of templates section (the </section> after the grid)
        # Actually let's find the last template-card and add after the grid
        grid_end = content.find('</div>', templates_end)  # first </div> closes the grid
        # find the full grid container end
        idx = content.find('<div class="templates-grid"', templates_end)
        # count divs to find the end of templates-grid
        depth = 0
        end_idx = idx
        for i, c in enumerate(content[idx:], idx):
            if c == '<':
                if content[i:i+5] == '<div ':
                    depth += 1
                elif content[i:i+6] == '</div>':
                    depth -= 1
                    if depth == 0:
                        end_idx = i + 6
                        break
        content = content[:end_idx] + datasets_section + content[end_idx:]
        print('Added datasets section')
else:
    print('datasets-list already present')

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Fixed!')
print(f'Total size: {len(content)} chars')
print(f'datasets-list now:', 'datasets-list' in content)

# Final check
with open(path, 'r', encoding='utf-8') as f:
    final = f.read()
ld_m = re.search(r'"url":\s*"([^"]+)"', final)
print('JSON-LD url:', ld_m.group(1) if ld_m else 'NOT FOUND')
canonical = re.search(r'rel="canonical" href="([^"]+)"', final)
print('canonical:', canonical.group(1) if canonical else 'NOT FOUND')
og_url = re.search(r'og:url" content="([^"]+)"', final)
print('og:url:', og_url.group(1) if og_url else 'NOT FOUND')
