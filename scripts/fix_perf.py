import os
import re

# Critical inline CSS to prevent FOUC and CLS
CRITICAL_CSS = """<style>
/* Critical CSS - prevent FOUC and CLS */
*,*::before,*::after{margin:0;padding:0;box-sizing:border-box}
:root{
  --bg-main:#131c2e;--bg-dark:#0a0f1a;--bg-card:#1f2940;
  --bg-secondary:#2a3654;--text-primary:#F8FAFC;--text-secondary:#94A3B8;
  --primary:#22C55E;--space-sm:0.5rem;--space-md:1rem;--space-xl:2rem;
  --radius-md:8px;--radius-lg:12px;
}
body{font-family:'DM Sans','Segoe UI',-apple-system,BlinkMacSystemFont,sans-serif;background:var(--bg-main);color:var(--text-primary);line-height:1.6;min-height:100vh;display:flex;flex-direction:column}
.navbar{background:var(--bg-dark);height:64px;display:flex;align-items:center;justify-content:space-between;padding:0 var(--space-xl);border-bottom:1px solid var(--bg-secondary);position:sticky;top:0;z-index:100}
.navbar-brand{font-size:1.25rem;font-weight:700;color:var(--text-primary);text-decoration:none;display:flex;align-items:center;gap:var(--space-sm)}
.navbar-links{display:flex;align-items:center;gap:0.25rem;flex-wrap:wrap}
.nav-link{color:var(--text-secondary);text-decoration:none;padding:var(--space-sm) var(--space-md);border-radius:var(--radius-md);font-size:.875rem;font-weight:500;height:36px;min-width:36px;display:inline-flex;align-items:center;justify-content:center;gap:0.3rem}
.nav-link svg{width:16px;height:16px;flex-shrink:0}
.nav-link:hover,.nav-link.active{color:var(--primary);background:rgba(34,197,94,.1)}
.main-container{flex:1;max-width:1200px;margin:0 auto;padding:var(--space-xl);width:100%}
</style>"""

files = {
    'index.html': 'css/styles.css',
    'pages/format.html': '../css/styles.css',
    'pages/escape.html': '../css/styles.css',
    'pages/extract.html': '../css/styles.css',
    'pages/sort.html': '../css/styles.css',
    'pages/clean.html': '../css/styles.css',
    'pages/xml.html': '../css/styles.css',
    'pages/yaml.html': '../css/styles.css',
    'pages/viewer.html': '../css/styles.css',
    'pages/json2csv.html': '../css/styles.css',
    'pages/compare.html': '../css/styles.css',
    'pages/blog.html': '../css/styles.css',
    'pages/news.html': '../css/styles.css',
}

updated = []
for rel_path, css_path in files.items():
    fp = os.path.join(r'd:\网站开发-json', rel_path)
    if not os.path.exists(fp):
        print(f'SKIP {rel_path}')
        continue
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove old async CSS preload patterns and preconnects
    content = re.sub(
        r'[ \t]*<!--[^>]*[Pp]reload[^>]*-->\s*\n',
        '',
        content
    )
    content = re.sub(
        r'[ \t]*<link rel="preload" href="[^"]*styles\.css"[^>]*>\s*\n?',
        '',
        content
    )
    content = re.sub(
        r'[ \t]*<noscript><link rel="stylesheet" href="[^"]*styles\.css"></noscript>\s*\n?',
        '',
        content
    )
    content = re.sub(
        r'[ \t]*<!-- Preconnect[^>]*-->\s*\n',
        '',
        content
    )
    content = re.sub(
        r'[ \t]*<link rel="preconnect" href="https://fonts\.googleapis\.com">\s*\n?',
        '',
        content
    )
    content = re.sub(
        r'[ \t]*<link rel="preconnect" href="https://fonts\.gstatic\.com" crossorigin>\s*\n?',
        '',
        content
    )
    content = re.sub(
        r'[ \t]*<!-- Preload critical[^>]*-->\s*\n',
        '',
        content
    )

    # New tags to inject before </head>
    new_tags = (
        '    <!-- Preconnect to Google Fonts -->\n'
        '    <link rel="preconnect" href="https://fonts.googleapis.com">\n'
        '    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
        '    <!-- Google Fonts with display=swap to prevent CLS -->\n'
        '    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&display=swap">\n'
        f'    <!-- Main CSS - synchronous for LCP/CLS -->\n'
        f'    <link rel="stylesheet" href="{css_path}">\n'
    )

    content = content.replace('</head>', CRITICAL_CSS + '\n' + new_tags + '</head>')

    with open(fp, 'w', encoding='utf-8') as f:
        f.write(content)
    updated.append(rel_path)
    print(f'OK: {rel_path}')

print(f'\nUpdated {len(updated)} files')
