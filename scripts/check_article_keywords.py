# -*- coding: utf-8 -*-
from pathlib import Path
BASE = Path("d:/网站开发-json")
count = 0
for subdir in (BASE / "blog").iterdir():
    if subdir.is_dir():
        f = subdir / "index.html"
        if f.exists() and 'meta name="keywords"' in f.read_text(encoding="utf-8"):
            count += 1
print(f"blog articles with keywords: {count}")
