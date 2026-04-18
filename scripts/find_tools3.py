import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'd:\网站开发-json\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find "Tools" in content
pos = content.find('Tools')
print(f'"Tools" position: {pos}')

if pos > 0:
    start = max(0, pos - 100)
    end = min(len(content), pos + 100)
    print('\nContext around Tools:')
    print(repr(content[start:end]))
