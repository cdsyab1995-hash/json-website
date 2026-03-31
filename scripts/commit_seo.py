#!/usr/bin/env python
"""Commit and push SEO improvements"""
import subprocess
import sys

git = r'C:\Users\Administrator\.workbuddy\binaries\git\cmd\git.exe'
repo = r'd:\网站开发-json'

def run_git(args):
    result = subprocess.run(
        [git, '-C', repo] + args,
        capture_output=True, text=True
    )
    print(result.stdout)
    if result.stderr:
        print(result.stderr)
    return result.returncode

# Add all changes
print("Adding changes...")
run_git(['add', '-A'])

# Commit
print("\nCommitting...")
run_git(['commit', '-m', 'Fix SEO: correct canonical URLs, Open Graph, and JSON-LD paths'])

# Push
print("\nPushing...")
result = run_git(['push', 'origin', 'main'])
print(f"\nExit code: {result}")
