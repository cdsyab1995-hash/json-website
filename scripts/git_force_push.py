#!/usr/bin/env python3
"""Abort rebase and force push"""
import subprocess
import sys

git_path = r"C:\Users\Administrator\.workbuddy\binaries\git\cmd\git.exe"
repo_path = r"d:\网站开发-json"

# Abort any ongoing rebase
result = subprocess.run([git_path, "-C", repo_path, "rebase", "--abort"], 
                       capture_output=True, text=True, encoding='utf-8', errors='ignore')
print("Rebase abort:", result.returncode)

# Reset to origin/main (force)
result = subprocess.run([git_path, "-C", repo_path, "reset", "--hard", "origin/main"], 
                       capture_output=True, text=True, encoding='utf-8', errors='ignore')
print("Reset to origin/main:", result.returncode, result.stderr[:200] if result.stderr else "")

# Add files
files = ['pages/format.html', 'pages/escape.html', 'pages/extract.html', 
         'pages/sort.html', 'pages/clean.html', 'pages/xml.html', 'pages/yaml.html',
         'pages/viewer.html', 'pages/json2csv.html', 'pages/compare.html', 
         'pages/best-practices.html']
result = subprocess.run([git_path, "-C", repo_path, "add"] + files, 
                       capture_output=True, text=True, encoding='utf-8', errors='ignore')
print("Add files:", result.returncode)

# Commit
result = subprocess.run([git_path, "-C", repo_path, "commit", "-m", 
                        "Fix navbar: add missing changelog links to 11 tool pages"], 
                       capture_output=True, text=True, encoding='utf-8', errors='ignore')
print("Commit:", result.returncode, result.stderr[:200] if result.stderr else "")

# Pull with rebase
result = subprocess.run([git_path, "-C", repo_path, "pull", "--rebase", "origin", "main"], 
                       capture_output=True, text=True, encoding='utf-8', errors='ignore', timeout=60)
print("Pull:", result.returncode, result.stderr[:300] if result.stderr else "")

# Push
result = subprocess.run([git_path, "-C", repo_path, "push", "origin", "main"], 
                       capture_output=True, text=True, encoding='utf-8', errors='ignore', timeout=60)
print("Push:", result.returncode)
if result.returncode == 0:
    print("[OK] Successfully pushed!")
else:
    print("Error:", result.stderr[:500])
