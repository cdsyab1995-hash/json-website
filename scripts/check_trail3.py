#!/usr/bin/env python3
from pathlib import Path
import re
BASE = Path('d:/网站开发-json')

fmt = (BASE / 'tools/json-formatter/index.html').read_text(encoding='utf-8')
print(f'File length: {len(fmt)} chars')

# Find all trailing quote issues (class="...">)
# More carefully: look for cases where > comes right after " without space
# This is the audit's specific concern: class="..."> vs class="..." >
issues = re.findall(r'class="[^"]+">', fmt)
print(f'Found {len(issues)} class="..."> patterns')

# Look for specific malformed patterns: class="X"" or class="X"">
# These would indicate double quotes
bad_patterns = re.findall(r'class="[^"]+""[^>]*>', fmt)
print(f'Found {len(bad_patterns)} double-quote issues')

# Look for the pattern: class="..."  > (space before >) - normal
normal = re.findall(r'class="[^"]+" >', fmt)
print(f'Found {len(normal)} normal class="..." > patterns')

# Check first 500 chars
print('\nFirst 500 chars of file:')
print(repr(fmt[:500]))
