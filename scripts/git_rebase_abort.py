#!/usr/bin/env python3
"""Abort rebase and force push"""
import subprocess
import os

os.chdir('d:/网站开发-json')

# Abort rebase
result = subprocess.run(['git', 'rebase', '--abort'], capture_output=True, text=True)
print("Rebase abort:", result.returncode)

# Reset to origin/main
result = subprocess.run(['git', 'reset', '--hard', 'origin/main'], capture_output=True, text=True)
print("Reset:", result.returncode)

# Re-apply changes manually
result = subprocess.run(['git', 'add', 'pages/format.html', 'pages/escape.html', 'pages/extract.html', 
                         'pages/sort.html', 'pages/clean.html', 'pages/xml.html', 'pages/yaml.html',
                         'pages/viewer.html', 'pages/json2csv.html', 'pages/compare.html', 
                         'pages/best-practices.html'], capture_output=True, text=True)
print("Add files:", result.returncode)

# Commit
result = subprocess.run(['git', 'commit', '-m', 'Fix navbar: add missing changelog links to 11 tool pages'], 
                        capture_output=True, text=True)
print("Commit:", result.returncode, result.stdout, result.stderr)

# Pull with rebase
result = subprocess.run(['git', 'pull', '--rebase', 'origin', 'main'], capture_output=True, text=True)
print("Pull:", result.returncode, result.stdout[:500], result.stderr[:500])

# Push
result = subprocess.run(['git', 'push', 'origin', 'main'], capture_output=True, text=True)
print("Push:", result.returncode, result.stdout[:500], result.stderr[:500])
