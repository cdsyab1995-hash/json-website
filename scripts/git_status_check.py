#!/usr/bin/env python3
"""Check git status"""
import subprocess

git_path = r"C:\Users\Administrator\.workbuddy\binaries\git\cmd\git.exe"
repo_path = r"d:\网站开发-json"

# Check status
result = subprocess.run([git_path, "-C", repo_path, "status", "--short"], 
                       capture_output=True, text=True, encoding='utf-8', errors='ignore')
print("Status:")
print(result.stdout if result.stdout else "(no changes)")
print(result.stderr[:500] if result.stderr else "")

# Check log
result = subprocess.run([git_path, "-C", repo_path, "log", "--oneline", "-5"], 
                       capture_output=True, text=True, encoding='utf-8', errors='ignore')
print("\nRecent commits:")
print(result.stdout)
