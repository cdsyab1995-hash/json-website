#!/usr/bin/env python3
"""Final audit check for all 4 original issues"""
import re
import io
import sys
from pathlib import Path

for stream in [sys.stdout, sys.stderr]:
    if stream.encoding != 'utf-8':
        stream.reconfigure(encoding='utf-8', errors='replace')

BASE = Path('d:/网站开发-json')

print('='*60)
print('ISSUE 1: Format page Load Example - btnFormat ID mismatch')
print('='*60)
fmt = (BASE / 'tools/json-formatter/index.html').read_text(encoding='utf-8')
has_select = 'id="templateSelect"' in fmt
has_input = 'id="jsonInput"' in fmt
has_btnformat = 'id="btnFormat"' in fmt
app_js = (BASE / 'js/app.js').read_text(encoding='utf-8')
js_template = 'templateSelect' in app_js
js_jsoninput = "'jsonInput'" in app_js
js_btnformat = "'btnFormat'" in app_js
print(f'  HTML: templateSelect={has_select}, jsonInput={has_input}, btnFormat={has_btnformat}')
print(f'  JS:  templateSelect={js_template}, jsonInput={js_jsoninput}, btnFormat={js_btnformat}')
pkg_match = '"package"' in app_js
print(f'  Templates package key matches option value: {pkg_match}')
if has_select and has_input and has_btnformat and js_template and pkg_match:
    print('  STATUS: FIXED')
else:
    print('  STATUS: STILL BROKEN')

print()
print('='*60)
print('ISSUE 2: Article page structured data date consistency')
print('='*60)
all_ok = True
for subdir in ['blog', 'news']:
    base = BASE / subdir
    for d in sorted(base.iterdir()):
        if d.is_dir() and d.name != 'index.html':
            idx = d / 'index.html'
            if idx.exists():
                text = idx.read_text(encoding='utf-8')
                ld = re.search(r'<script type=.application/ld\+json.>(.*?)</script>', text, re.DOTALL)
                if ld:
                    dp = re.search(r'datePublished.*?([0-9-]+)', ld.group(1))
                    dm = re.search(r'dateModified.*?([0-9-]+)', ld.group(1))
                    pub = dp.group(1) if dp else None
                    mod = dm.group(1) if dm else None
                    vis = re.findall(r'([0-9]{4}-[0-9]{2}-[0-9]{2})', text[:3000])
                    vis_date = vis[0] if vis else None
                    if pub and vis_date and pub != vis_date:
                        print(f'  MISMATCH: {subdir}/{d.name} pub={pub} vis={vis_date}')
                        all_ok = False
if all_ok:
    print('  All article dates OK: FIXED')

print()
print('='*60)
print('ISSUE 3: HTML template quality (duplicate classes, trailing quotes, repeated blocks)')
print('='*60)
fmt = (BASE / 'tools/json-formatter/index.html').read_text(encoding='utf-8')
dup_classes = len(re.findall(r'class="[^"]*"[^>]*class="', fmt))
trail_quotes = len(re.findall(r'class="[^"]+">', fmt))
common_use_cases = fmt.count('Common Use Cases')
print(f'  tools/json-formatter/index.html:')
print(f'    duplicate class attrs: {dup_classes}')
print(f'    trailing quote issues: {trail_quotes}')
print(f'    Common Use Cases occurrences: {common_use_cases}')
index_html = (BASE / 'index.html').read_text(encoding='utf-8')
dup2 = len(re.findall(r'class="[^"]*"[^>]*class="', index_html))
print(f'  index.html: duplicate class attrs: {dup2}')
if dup_classes == 0 and trail_quotes == 0 and common_use_cases <= 1 and dup2 == 0:
    print('  STATUS: FIXED')

print()
print('='*60)
print('ISSUE 4: setLoading() disabled boolean issue')
print('='*60)
app_js = (BASE / 'js/app.js').read_text(encoding='utf-8')
idx = app_js.find('setLoading')
if idx >= 0:
    section = app_js[idx:idx+300]
    print(f'  setLoading code: {section[:200]}')
    # Check if it uses return value incorrectly
    if 'classList.add(' in section and 'btn.disabled=' in section:
        print('  STATUS: FIXED (btn.disabled set directly, not from classList return)')
    else:
        print('  STATUS: NEEDS REVIEW')

print()
print('='*60)
print('BONUS CHECKS')
print('='*60)

# Check canonical tags
print('Canonical tags:')
for fpath in ['about/index.html', 'blog/index.html', 'news/index.html',
              'tools/json-formatter/index.html']:
    f = BASE / fpath
    if f.exists():
        text = f.read_text(encoding='utf-8')
        has = bool(re.search(r'<link[^>]+rel=["\']canonical["\']', text))
        # Also check og:url and twitter:url
        canon_in_text = 'canonical' in text and '/pages/' not in text
        og_ok = 'og:url' in text and '/pages/' not in text
        print(f'  {fpath}: canonical={has}, no /pages/ refs={canon_in_text}')

# Check for 2026-01-01 in old files
print()
old_bad = []
for subdir in ['pages/blog', 'pages/news']:
    base = BASE / subdir
    if base.exists():
        for f in base.glob('*.html'):
            text = f.read_text(encoding='utf-8')
            ld = re.search(r'<script type=.application/ld\+json.>(.*?)</script>', text, re.DOTALL)
            if ld and '2026-01-01' in ld.group(1):
                old_bad.append(str(f.relative_to(BASE)))
if old_bad:
    print(f'OLD FILES with 2026-01-01: {len(old_bad)} still bad')
else:
    print('Old files with 2026-01-01: NONE (all fixed)')
