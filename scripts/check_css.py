#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess
import os
import sys

GIT = r"C:\Users\Administrator\.workbuddy\binaries\git\cmd\git.exe"
REPO = r"d:\网站开发-json"

def git_cat_file(commit, path):
    result = subprocess.run(
        [GIT, "-C", REPO, "show", f"{commit}:{path}"],
        capture_output=True
    )
    return result.stdout

def main():
    commits = ["8b82662", "fafd4ef", "60f5ab7", "817dc99"]
    for c in commits:
        data = git_cat_file(c, "css/styles.css")
        print(f"Commit {c}: {len(data)} bytes")
        if data:
            # Check first bytes
            first = data[:20]
            print(f"  First bytes: {first[:20]}")
            # Try decode
            try:
                text = data.decode("utf-8")
                lines = text.split("\n")
                print(f"  Lines: {len(lines)}")
                print(f"  First line: {lines[0][:100]}")
                # Save this one
                out = os.path.join(REPO, f"css_backup_{c}.css")
                with open(out, "wb") as f:
                    f.write(data)
                print(f"  Saved to: {out}")
                break
            except Exception as e:
                print(f"  Decode error: {e}")
        print()

if __name__ == "__main__":
    main()
