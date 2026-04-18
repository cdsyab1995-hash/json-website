import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'd:\网站开发-json\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find Tools toggle with surrounding context
# The pattern should be: Tools dropdown toggle
pattern = r'(<a href="#" class="nav-link nav-dropdown-toggle">[^<]*<svg[^>]*>[^<]*</svg>)'

match = re.search(pattern, content)
if match:
    print('Found pattern:')
    print(match.group(1))
    print('\n\nWith context:')
    start = max(0, match.start() - 50)
    end = min(len(content), match.end() + 200)
    print(content[start:end])
