#!/usr/bin/env python3
"""
将所有页面的硬编码导航栏替换为共享 navbar.js 组件调用。

处理范围：
- tools/*.html          (24个工具页)
- about / blog / news / best-practices / changelog  (5个静态页)
- pages/blog/*.html     (14篇博客详情)
- pages/news/*.html     (12篇新闻详情)
- index.html            (首页)
"""

import re
from pathlib import Path

BASE = Path('d:/网站开发-json')

# 需要处理的文件列表
TARGET_DIRS = [
    BASE / 'tools',
    BASE / 'pages',
    BASE / 'pages' / 'blog',
    BASE / 'pages' / 'news',
]
TARGET_ROOTS = [
    BASE / 'about',
    BASE / 'blog',
    BASE / 'news',
    BASE / 'best-practices',
    BASE / 'changelog',
    BASE / 'index.html',
]

# 匹配导航栏 HTML 块的正则
# 从 <nav class="navbar"> 到 </nav>
NAV_PATTERN = re.compile(
    r'<!--\s*Navigation\s*-->\s*<nav class="navbar">.*?</nav>',
    re.DOTALL
)

# 替换为占位符
NAV_PLACEHOLDER = '<!-- Navigation -->\n<div id="navbar-placeholder"></div>'

# navbar.js 注入标记（放在 </head> 前）
NAVBAR_SCRIPT = '<script src="/js/navbar.js"></script>'

def inject_navbar_script(content):
    """在 </head> 前注入 navbar.js（避免重复注入）"""
    if 'navbar.js' in content:
        return content
    return content.replace('</head>', f'{NAVBAR_SCRIPT}\n</head>', 1)

def process_file(path: Path):
    try:
        text = path.read_text(encoding='utf-8')
    except Exception as e:
        print(f'[ERROR] read {path}: {e}')
        return False

    original = text

    # 1. 替换导航栏 HTML
    if NAV_PATTERN.search(text):
        text = NAV_PATTERN.sub(NAV_PLACEHOLDER, text)
    else:
        # 尝试不带注释的形式
        nav_bare = re.compile(r'<nav class="navbar">.*?</nav>', re.DOTALL)
        if nav_bare.search(text):
            text = nav_bare.sub(NAV_PLACEHOLDER, text)
        else:
            print(f'[SKIP] no navbar found: {path.name}')
            return False

    # 2. 注入 navbar.js
    text = inject_navbar_script(text)

    if text == original:
        print(f'[SKIP] no change: {path.name}')
        return False

    path.write_text(text, encoding='utf-8')
    print(f'[OK] {path.relative_to(BASE)}')
    return True


def main():
    count = 0

    # 处理 tools/ 目录
    for d in TARGET_DIRS:
        if d.exists():
            for f in sorted(d.glob('*.html')):
                if process_file(f):
                    count += 1

    # 处理根目录静态页
    for p in TARGET_ROOTS:
        if p.exists():
            if process_file(p):
                count += 1

    print(f'\n总计处理：{count} 个文件')


if __name__ == '__main__':
    main()
