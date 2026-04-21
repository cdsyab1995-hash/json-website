"""
清理所有页面中的旧/重复 JSON-LD blocks
"""
import re
from pathlib import Path

PROJECT = Path("d:/网站开发-json")
PAGES = PROJECT / "pages"
BLOG = PAGES / "blog"

def clean_page(content):
    """Remove all existing JSON-LD blocks from <head> section"""
    head_start = content.find('<head>')
    head_end = content.find('</head>')
    if head_start == -1 or head_end == -1:
        return content

    head_content = content[head_start:head_end]

    # Remove JSON-LD blocks with preceding comments
    head_content = re.sub(
        r'<!-- JSON-LD.*?-->\s*<script type="application/ld\+json">.*?</script>',
        '', head_content, flags=re.DOTALL
    )

    # Remove standalone JSON-LD blocks
    head_content = re.sub(
        r'<script type="application/ld\+json">.*?</script>',
        '', head_content, flags=re.DOTALL
    )

    return content[:head_start] + head_content + content[head_end:]


def clean_file(filepath):
    content = open(filepath, 'r', encoding='utf-8').read()
    new_content = clean_page(content)
    changed = content != new_content
    open(filepath, 'w', encoding='utf-8').write(new_content)
    return changed


print('=' * 60)
print('Cleaning old JSON-LD blocks')
print('=' * 60)

count = 0
for filepath in list(PAGES.glob('*.html')) + list(BLOG.glob('*.html')):
    if clean_file(filepath):
        print(f'  [CLEANED] {filepath.relative_to(PROJECT)}')
        count += 1

print(f'\nCleaned {count} files')
print('Ready to run enhance_schema.py again')
print('=' * 60)
