import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'd:\网站开发-json\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the Tools text
pos = content.find('>Tools</a>')
print(f'>Tools</a> position: {pos}')

if pos < 0:
    pos = content.find('>Tools ')
    print(f'>Tools  position: {pos}')

if pos < 0:
    pos = content.find('Tools</a>')
    print(f'Tools</a> position: {pos}')

if pos > 0:
    start = max(0, pos - 600)
    end = min(len(content), pos + 20)
    print('\nContext:')
    print(repr(content[start:end]))
