import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'd:\网站开发-json\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find exact position and content
pos = content.find('Tools</a>')
if pos > 0:
    print('Found "Tools</a>" at position:', pos)
    # Show context
    start = max(0, pos - 500)
    end = min(len(content), pos + 50)
    print('\nContext:')
    print(repr(content[start:end]))
