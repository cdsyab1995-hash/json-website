#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Restore index.html from the accf78d commit (which has the latest blog but broken layout)
We'll rebuild index.html properly with correct structure.
"""
import subprocess
import sys
import os

PYTHON = r"C:\Users\Administrator\.workbuddy\binaries\python\versions\3.13.12\python.exe"
GIT = r"C:\Users\Administrator\.workbuddy\binaries\git\cmd\git.exe"
REPO = r"d:\网站开发-json"

def git_show(commit, path):
    """Get file content from a specific git commit"""
    result = subprocess.run(
        [GIT, "-C", REPO, "show", f"{commit}:{path}"],
        capture_output=True,
        encoding="utf-8",
        errors="replace"
    )
    return result.stdout

def main():
    # Get index.html from commit 8b82662 (before the P0 optimization that broke things)
    print("Extracting index.html from commit 8b82662...")
    content = git_show("8b82662", "index.html")
    
    if not content or len(content) < 1000:
        print(f"ERROR: Content too short ({len(content)} chars), trying another commit...")
        content = git_show("433580a", "index.html")
    
    if not content or len(content) < 1000:
        print(f"ERROR: Still too short ({len(content)} chars)")
        return
    
    print(f"Got content: {len(content)} chars, {content.count(chr(10))} lines")
    preview = content[:200].encode('ascii', errors='replace').decode('ascii')
    print(f"First 200 chars: {preview}")
    
    # Save to file
    output = os.path.join(REPO, "index_restored.html")
    with open(output, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"Saved to: {output}")

if __name__ == "__main__":
    main()
