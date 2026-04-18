import sys, os
sys.stdout.reconfigure(encoding='utf-8')

# Get the full navbar from css-minifier.html to understand its structure
with open(r'd:\网站开发-json\pages\css-minifier.html', 'r', encoding='utf-8') as f:
    content = f.read()

start = content.find('<header class="navbar">')
end = content.find('</header>', start)
navbar = content[start:end + len('</header>')]
print(navbar[:3000])
print('\n---TRUNCATED---')
print(navbar[-1000:])
