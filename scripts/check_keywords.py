# -*- coding: utf-8 -*-
from pathlib import Path
BASE = Path("d:/网站开发-json")
dirs = ["about","best-practices","changelog","blog","news"]
for d in dirs:
    f = BASE / d / "index.html"
    if f.exists():
        text = f.read_text(encoding="utf-8")
        has = 'meta name="keywords"' in text
        print(f"{d}/index.html: has_keywords={has}")
