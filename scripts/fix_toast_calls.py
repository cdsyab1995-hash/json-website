from pathlib import Path

js_path = Path(r'd:\网站开发-json\js\app.js')
content = js_path.read_text(encoding='utf-8')

# Replace conditional showToast calls with direct calls (no guard check)
# Use actual Unicode chars instead of escape sequences
old1 = " if (window.showToast) showToast('JSON formatted successfully \u2713','success');"
new1 = " window.showToast('JSON formatted successfully \u2713','success');"

old2 = " if (window.showToast) showToast('JSON minified successfully \u2713','success');"
new2 = " window.showToast('JSON minified successfully \u2713','success');"

old3 = " if (window.showToast) showToast('Copied to clipboard \u2713','success');"
new3 = " window.showToast('Copied to clipboard \u2713','success');"

count = 0
for old, new in [(old1, new1), (old2, new2), (old3, new3)]:
    if old in content:
        content = content.replace(old, new)
        count += 1
        print(f'Replaced: {repr(old[:50])}')
    else:
        print(f'NOT FOUND: {repr(old[:50])}')

js_path.write_text(content, encoding='utf-8')
print(f'\nTotal updated: {count} showToast calls')
