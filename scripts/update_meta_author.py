import os

pages_dir = r'd:\网站开发-json\pages'
old_str = 'AI JSON - Free JSON Tools for US Developers'
new_str = 'AI JSON - JSON Tools for US Developers'

count = 0
for root, dirs, files in os.walk(pages_dir):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            if old_str in content:
                content = content.replace(old_str, new_str)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                count += 1
                print(f'Updated: {filepath}')

print(f'\nTotal files updated: {count}')
