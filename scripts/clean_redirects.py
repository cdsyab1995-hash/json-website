#!/usr/bin/env python3
"""Clean up _redirects: remove duplicate entries, normalize spacing."""
import re

path = r"d:\网站开发-json\_redirects"
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

lines = content.split('\n')

# Collect unique non-empty lines
seen = set()
result_lines = []
for line in lines:
    stripped = line.strip()
    # Skip empty lines and pure comment lines
    if not stripped or (stripped.startswith('#') and not stripped.startswith('# ')):
        if stripped.startswith('# URL Redirects') or stripped.startswith('# Tool pages') or \
           stripped.startswith('# Blog') or stripped.startswith('# News') or \
           stripped.startswith('# Static pages') or stripped.startswith('# Homepage'):
            result_lines.append(line)
        continue
    # Skip duplicate comments
    if stripped.startswith('#'):
        continue
    # Deduplicate redirect rules
    if stripped not in seen:
        seen.add(stripped)
        result_lines.append(line)
    else:
        print(f"[DUP] {stripped}")

result = '\n'.join(result_lines) + '\n'
with open(path, 'w', encoding='utf-8') as f:
    f.write(result)

print(f"\nCleaned _redirects: {len(lines)} -> {len(result_lines)} lines")
