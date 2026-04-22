#!/usr/bin/env python3
"""Delete loose .html files in tools/ that have corresponding directories."""
import os

TOOLS_DIR = r"d:\网站开发-json\tools"

files = [f for f in os.listdir(TOOLS_DIR) if f.endswith('.html')]
print(f"Found {len(files)} loose .html files in tools/")

deleted = 0
for f in sorted(files):
    path = os.path.join(TOOLS_DIR, f)
    slug = f.replace('.html', '')
    dir_path = os.path.join(TOOLS_DIR, slug)
    if os.path.isdir(dir_path):
        os.remove(path)
        print(f"[DEL] {f} (dir {slug}/ exists)")
        deleted += 1
    else:
        print(f"[SKIP] {f} (no dir {slug}/)")

print(f"\nDeleted {deleted} files.")
