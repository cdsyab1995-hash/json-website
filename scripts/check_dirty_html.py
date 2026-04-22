# -*- coding: utf-8 -*-
import re
from pathlib import Path

BASE = Path("d:/网站开发-json")
files = [BASE / "index.html", BASE / "tools" / "json-formatter.html"]
for f in files:
    text = f.read_text(encoding="utf-8")
    dup = re.findall(r'class="[^"]*"\s+class="', text)
    extra = re.findall(r'class="[^"]+">', text)
    print(f"{f.name}: duplicate_class={len(dup)}, extra_quote={len(extra)}")
    if dup:
        print("  DUP:", dup[:3])
    if extra:
        print("  EXTRA:", extra[:3])
