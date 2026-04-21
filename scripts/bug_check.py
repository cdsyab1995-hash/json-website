import os, re
from pathlib import Path

PROJECT = Path(r'd:\网站开发-json')
issues = []

def check_file(name, path, checks):
    """Run checks on a file, return list of (severity, msg)"""
    results = []
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        results.append(('ERROR', f'Cannot read: {e}'))
        return results

    for check_name, pattern, severity in checks:
        if isinstance(pattern, str):
            pattern = re.compile(pattern, re.DOTALL)
        matches = pattern.findall(content)
        count = len(matches)
        if isinstance(pattern.pattern, str):
            desc = pattern.pattern[:60]
        else:
            desc = str(pattern)[:60]
        results.append((severity, f'{name}: {check_name}={count} [{desc}]'))
    return results

# === CHECK 1: clean_schema should have removed ALL JSON-LD ===
# If any file still has old schema blocks, that's a bug
print('=== CHECK 1: Old JSON-LD leftover ===')
pages_dir = PROJECT / 'pages'
for f in list(pages_dir.glob('*.html')) + list((pages_dir / 'blog').glob('*.html')):
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    # Check for any application/ld+json blocks
    ld_blocks = re.findall(r'<script type="application/ld\+json">', c)
    if ld_blocks:
        issues.append(('ERROR', f'{f.name}: Still has {len(ld_blocks)} JSON-LD blocks after clean_schema?'))

# === CHECK 2: enhance_schema should add exactly 2 schema blocks per tool page ===
# (WebApplication + BreadcrumbList), optionally 1 FAQPage
print('\n=== CHECK 2: Tool pages Schema count ===')
tool_pages = ['format.html', 'escape.html', 'extract.html', 'sort.html', 'clean.html',
              'xml.html', 'yaml.html', 'viewer.html', 'json2csv.html', 'compare.html']
for name in tool_pages:
    p = pages_dir / name
    if not p.exists():
        issues.append(('ERROR', f'{name}: File not found'))
        continue
    with open(p, 'r', encoding='utf-8') as fp:
        c = fp.read()
    wa = bool(re.search(r'"@type":\s*"WebApplication"', c))
    bc = bool(re.search(r'"@type":\s*"BreadcrumbList"', c))
    faq = len(re.findall(r'"@type":\s*"FAQPage"', c))
    ar = c.count('aggregateRating')
    sw = bool(re.search(r'"softwareVersion"', c))
    ok = wa and bc and ar == 1 and sw
    status = '[OK]' if ok else '[WARN]'
    print(f'  {status} {name}: WebApp={wa}, BC={bc}, FAQ={faq}, Rating={ar}, Version={sw}')
    if not ok:
        issues.append(('WARN', f'{name}: Missing schema fields - WA={wa}, BC={bc}, AR={ar}, SV={sw}'))

# === CHECK 3: Blog articles should have Article + BreadcrumbList ===
print('\n=== CHECK 3: Blog articles Schema count ===')
blog_dir = pages_dir / 'blog'
blog_slugs = ['ai-tool-calling-mcp-2026', 'curl-json-api-guide', 'jwt-security-best-practices-2026',
              'zod-json-schema-validation-ai', 'json-schema-complete-guide-2026']
for slug in blog_slugs:
    p = blog_dir / f'{slug}.html'
    if not p.exists():
        issues.append(('ERROR', f'blog/{slug}.html: File not found'))
        continue
    with open(p, 'r', encoding='utf-8') as fp:
        c = fp.read()
    art = len(re.findall(r'"@type":\s*"Article"', c))
    bc = len(re.findall(r'"@type":\s*"BreadcrumbList"', c))
    wc = bool(re.search(r'"wordCount"', c))
    img = bool(re.search(r'"image":', c))
    me = bool(re.search(r'"mainEntityOfPage"', c))
    ok = art == 1 and bc == 1 and wc and img and me
    status = '[OK]' if ok else '[WARN]'
    print(f'  {status} {slug}: Article={art}, BC={bc}, wordCount={wc}, image={img}, mainEntity={me}')
    if not ok:
        issues.append(('WARN', f'{slug}: Missing schema - Art={art}, BC={bc}, WC={wc}, Img={img}, ME={me}'))

# === CHECK 4: _redirects file exists? ===
print('\n=== CHECK 4: _redirects file ===')
rd = PROJECT / '_redirects'
if rd.exists():
    with open(rd, 'r', encoding='utf-8') as fp:
        rc = fp.read()
    lines = [l for l in rc.splitlines() if l.strip() and not l.strip().startswith('#')]
    print(f'  [OK] _redirects exists: {len(lines)} rules')
    # Check format
    for i, line in enumerate(lines[:5]):
        parts = line.split()
        if len(parts) < 2:
            issues.append(('ERROR', f'_redirects line {i+1}: Not enough parts - {line}'))
else:
    issues.append(('ERROR', '_redirects: File NOT found!'))

# === CHECK 5: Related Tools section in pages ===
print('\n=== CHECK 5: Related Tools section ===')
for name in ['format.html', 'compare.html', 'json2csv.html']:
    p = pages_dir / name
    if not p.exists():
        continue
    with open(p, 'r', encoding='utf-8') as fp:
        c = fp.read()
    rt = bool(re.search(r'class="related-tools-section"', c))
    card = c.count('related-tool-card')
    status = '[OK]' if rt and card >= 2 else '[WARN]'
    print(f'  {status} {name}: section={rt}, cards={card}')
    if not rt:
        issues.append(('WARN', f'{name}: Missing related-tools-section'))

# === CHECK 6: JSON syntax validity of schema blocks ===
print('\n=== CHECK 6: JSON-LD syntax validation ===')
import json
all_html_files = list(pages_dir.glob('*.html')) + list(blog_dir.glob('*.html'))
for f in all_html_files[:10]:  # Check first 10
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    ld_blocks = re.findall(r'<script type="application/ld\+json">\s*(\{.*?\})\s*</script>', c, re.DOTALL)
    for block in ld_blocks:
        try:
            json.loads(block)
        except json.JSONDecodeError as e:
            issues.append(('ERROR', f'{f.name}: JSON-LD parse error: {e}'))

print('\n=== SUMMARY ===')
if issues:
    for sev, msg in issues:
        prefix = '[!!]' if sev == 'ERROR' else '[W]'
        print(f'  {prefix} {msg}')
else:
    print('  No issues found!')
