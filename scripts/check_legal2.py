#!/usr/bin/env python3
for path in [r"d:\网站开发-json\privacy\index.html", r"d:\网站开发-json\terms\index.html"]:
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()
    print(f"{'privacy' if 'privacy' in path else 'terms'}: "
          f"placeholder={('id=\"navbar-placeholder\"' in c)}, "
          f"navbar.js={('/js/navbar.js' in c)}, "
          f"old_nav={('<nav class=\"navbar\">' in c)}, "
          f"css_abs={('href=\"/css/styles.css\"' in c)}")
