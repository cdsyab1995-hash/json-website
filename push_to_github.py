#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GitHub Push Script"""

import subprocess
import os
import sys

def run_cmd(cmd, cwd=None):
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=cwd, encoding='utf-8', errors='replace')
        return result.returncode, result.stdout, result.stderr
    except Exception as e:
        return -1, "", str(e)

def main():
    repo_path = r"d:\网站开发-json"
    
    print("=" * 50)
    print("GitHub Push Script")
    print("=" * 50)
    
    # Check git
    code, out, err = run_cmd("git --version")
    if code != 0:
        print("[ERROR] Git not found")
        return
    
    print("[OK] Git: " + out.strip())
    
    # Init or check repo
    code, out, err = run_cmd("git rev-parse --git-dir", cwd=repo_path)
    if code != 0:
        print("[INFO] Initializing git repo...")
        run_cmd("git init", cwd=repo_path)
        run_cmd("git remote add origin git@github.com:cdsyab1995-hash/json-website.git", cwd=repo_path)
        print("[OK] Repo initialized")
    
    # Add files
    print("[INFO] Adding files...")
    run_cmd("git add -A", cwd=repo_path)
    
    # Commit
    print("[INFO] Committing...")
    code, out, err = run_cmd('git commit -m "Fix navbar and optimize title"', cwd=repo_path)
    if "nothing to commit" in out.lower() or code == 0:
        print("[OK] Committed or nothing to commit")
    
    # Push
    print("[INFO] Pushing to GitHub...")
    code, out, err = run_cmd("git push origin main", cwd=repo_path)
    if code != 0:
        print("[ERROR] Push failed: " + err[:200])
    else:
        print("[OK] Push successful!")
        print("=" * 50)
        print("Site will update in 1-2 minutes")
        print("https://cdsyab1995-hash.github.io/json-website/")
        print("=" * 50)

if __name__ == "__main__":
    main()
