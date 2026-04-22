#!/usr/bin/env python3
"""Delete the entire pages/ directory (all content migrated elsewhere)."""
import shutil
import os

PAGES_DIR = r"d:\网站开发-json\pages"

if not os.path.exists(PAGES_DIR):
    print("[SKIP] pages/ does not exist")
else:
    # Count files
    total = sum(len(files) for _, _, files in os.walk(PAGES_DIR))
    size = sum(os.path.getsize(os.path.join(dp, f))
               for dp, _, files in os.walk(PAGES_DIR)
               for f in files)
    print(f"Deleting pages/ ({total} files, {size/1024:.1f} KB)...")
    shutil.rmtree(PAGES_DIR)
    print(f"[DEL] pages/ deleted successfully")
