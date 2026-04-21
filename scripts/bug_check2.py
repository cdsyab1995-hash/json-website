import os, re
from pathlib import Path

PROJECT = Path(r'd:\网站开发-json')
issues = []

print('=== CHECK 7: _redirects format validation ===')
rd = PROJECT / '_redirects'
with open(rd, 'r', encoding='utf-8') as fp:
    lines = fp.readlines()
for i, line in enumerate(lines):
    line = line.strip()
    if not line or line.startswith('#'):
        continue
    parts = line.split()
    if len(parts) < 2:
        issues.append(('ERROR', f'_redirects:{i+1} - Not enough parts: "{line}"'))
    elif len(parts) == 2:
        # Source -> Destination
        pass
    elif len(parts) == 3:
        # Source -> Destination Status
        if parts[2] not in ('301', '302', '200'):
            issues.append(('ERROR', f'_redirects:{i+1} - Unknown status: "{line}"'))
    else:
        issues.append(('WARN', f'_redirects:{i+1} - Many parts: "{line}"'))

if not issues:
    print('  [OK] All redirect rules format correct')

print('\n=== CHECK 8: blog.html / blog/index.html wordCount ===')
blog_index = PROJECT / 'pages' / 'blog' / 'index.html'
if blog_index.exists():
    with open(blog_index, 'r', encoding='utf-8') as fp:
        c = fp.read()
    wc = bool(re.search(r'"wordCount"', c))
    print(f'  blog/index.html: wordCount={wc}')
    if not wc:
        issues.append(('WARN', 'blog/index.html: Missing wordCount in schema'))
else:
    print('  blog/index.html: Not found (this is ok)')

print('\n=== CHECK 9: CSS .related-tools-section exists? ===')
css = PROJECT / 'css' / 'styles.css'
with open(css, 'r', encoding='utf-8') as fp:
    css_content = fp.read()
has_rt = '.related-tools-section' in css_content
has_card = '.related-tool-card' in css_content
has_grid = '.related-tools-grid' in css_content
print(f'  .related-tools-section: {has_rt}')
print(f'  .related-tool-card: {has_card}')
print(f'  .related-tools-grid: {has_grid}')
if not has_rt or not has_card:
    issues.append(('ERROR', 'CSS missing .related-tools-section or .related-tool-card'))

print('\n=== CHECK 10: BreadcrumbList URL correctness ===')
# Check a few key files for correct URLs in breadcrumb
files_to_check = [
    ('pages/format.html', 'https://www.aijsons.com/pages/format.html'),
    ('pages/json2csv.html', 'https://www.aijsons.com/pages/json2csv.html'),
    ('pages/blog/ai-tool-calling-mcp-2026.html', 'https://aijsons.com/pages/blog/ai-tool-calling-mcp-2026.html'),
]
for fname, expected_url in files_to_check:
    p = PROJECT / fname
    if not p.exists():
        continue
    with open(p, 'r', encoding='utf-8') as fp:
        c = fp.read()
    # Extract last BreadcrumbList item URL
    m = re.search(r'"BreadcrumbList".*?"item":\s*"([^"]+)"', c, re.DOTALL)
    if m:
        url_in_bc = m.group(1)
        if url_in_bc != expected_url:
            issues.append(('WARN', f'{fname}: Breadcrumb URL mismatch. Got "{url_in_bc}", expected "{expected_url}"'))
        else:
            print(f'  [OK] {fname}: Breadcrumb URL correct')
    else:
        issues.append(('ERROR', f'{fname}: No BreadcrumbList item found'))

print('\n=== CHECK 11: Blog articles wordCount - verify calculation ===')
blog_dir = PROJECT / 'pages' / 'blog'
articles = list(blog_dir.glob('*.html'))
for ap in articles[:5]:
    with open(ap, 'r', encoding='utf-8') as fp:
        c = fp.read()
    # Extract wordCount from schema
    m = re.search(r'"wordCount":\s*(\d+)', c)
    if m:
        wc = int(m.group(1))
        # Rough estimate: article content should have at least wc words
        content_m = re.search(r'<div class="article-content">(.*?)</div>', c, re.DOTALL)
        if content_m:
            text = re.sub(r'<[^>]+>', ' ', content_m.group(1))
            text = re.sub(r'\s+', ' ', text).strip()
            actual_words = len(text.split())
            # Allow some variance due to strip
            if wc < 400 and actual_words > 600:
                issues.append(('WARN', f'{ap.name}: wordCount={wc} seems low vs actual ~{actual_words}'))
            print(f'  {ap.name}: wordCount={wc}, actual~{actual_words}')
        else:
            print(f'  {ap.name}: wordCount={wc} (no article-content div found)')
    else:
        print(f'  {ap.name}: NO wordCount found')

print('\n=== CHECK 12: Enhance schema Blog URL path ===')
# Check blog articles have the right URL in schema
for slug in ['ai-tool-calling-mcp-2026', 'jwt-security-best-practices-2026']:
    p = blog_dir / f'{slug}.html'
    if not p.exists():
        continue
    with open(p, 'r', encoding='utf-8') as fp:
        c = fp.read()
    # The URL in Article schema should match the page URL
    m_url = re.search(r'"@type":\s*"Article".*?"url":\s*"([^"]+)"', c, re.DOTALL)
    m_bc = re.search(r'"BreadcrumbList".*?"item":\s*"([^"]+)"', c, re.DOTALL)
    if m_url:
        print(f'  {slug}: Article url="{m_url.group(1)}"')
    if m_bc:
        print(f'  {slug}: Breadcrumb item="{m_bc.group(1)}"')

print('\n=== SUMMARY ===')
if issues:
    for sev, msg in issues:
        prefix = '[!!]' if sev == 'ERROR' else '[W]'
        print(f'  {prefix} {msg}')
else:
    print('  No issues found!')
