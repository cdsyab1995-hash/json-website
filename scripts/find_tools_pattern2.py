import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'd:\网站开发-json\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the Tools dropdown section
tools_match = re.search(r'class="nav-dropdown-toggle"', content)
if tools_match:
    # Get context around it
    start = max(0, tools_match.start() - 100)
    end = min(len(content), tools_match.end() + 500)
    context = content[start:end]
    print('Context around Tools toggle:')
    print(context)
    print('\n\n--- Looking for chevron ---')
    if 'chevron' in context.lower():
        print('Chevron found!')
    else:
        print('No chevron in this section')
