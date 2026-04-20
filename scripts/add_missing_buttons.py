#!/usr/bin/env python3
"""
添加缺失的 Copy/Clear 按钮到工具页
"""

import os
import re

PAGES_DIR = r"d:\网站开发-json\pages"

# 需要添加 Copy 按钮的页面
PAGES_NEED_COPY = [
    "escape.html",
    "extract.html",
    "sort.html",
    "compare.html",
    "viewer.html",
    "json2csv.html",
    "xml.html",
    "yaml.html",
]

# 需要添加 Clear 按钮的页面
PAGES_NEED_CLEAR = [
    "escape.html",
    "extract.html",
    "sort.html",
    "compare.html",
    "viewer.html",
    "json2csv.html",
    "xml.html",
    "yaml.html",
]

# 需要添加模板选择的页面
PAGES_NEED_TEMPLATE = [
    "escape.html",
    "extract.html",
    "clean.html",
    "viewer.html",
    "compare.html",
    "xml.html",
    "yaml.html",
]

# 按钮 HTML 模板
COPY_BTN = '''<button class="btn btn-secondary" id="btnCopy" style="margin-left: 0.5rem;">
    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
        <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
    </svg>
    Copy
</button>'''

CLEAR_BTN = '''<button class="btn btn-ghost" id="btnClear" style="margin-left: 0.5rem;">
    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <polyline points="3 6 5 6 21 6"></polyline>
        <path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path>
    </svg>
    Clear
</button>'''

TEMPLATE_SELECT = '''            <select id="templateSelect" style="padding: 6px 12px; border-radius: 6px; border: 1px solid var(--bg-secondary); background: var(--bg-secondary); cursor: pointer; color: var(--text-primary);">
                <option value="">Load Example...</option>
                <option value="example0">Example 1</option>
            </select>'''


def add_copy_button(content, page_name):
    """添加 Copy 按钮"""
    if 'btnCopy' in content:
        return content, False
    
    # 在 btnUnescape 或最后一个按钮后添加
    patterns = [
        r'(<button[^>]*id="btnUnescape"[^>]*>.*?</button>\s*)(</div>)',
        r'(<button[^>]*id="btnEscape"[^>]*>.*?</button>\s*)(</div>)',
        r'(<button[^>]*id="btnCompare"[^>]*>.*?</button>\s*)(</div>)',
        r'(<button[^>]*class="btn[^"]*"[^>]*>[^<]*</button>\s*)(</div>\s*</div>\s*</section>)',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, content, re.DOTALL)
        if match:
            content = content.replace(match.group(0), match.group(1) + COPY_BTN + '\n                ' + match.group(2), 1)
            return content, True
    
    return content, False


def add_clear_button(content, page_name):
    """添加 Clear 按钮"""
    if 'btnClear' in content:
        return content, False
    
    # 在 btnCopy 后或操作按钮区域添加
    if 'btnCopy' in content:
        content = content.replace(
            COPY_BTN,
            COPY_BTN + '\n                ' + CLEAR_BTN
        )
        return content, True
    
    # 否则在操作按钮末尾添加
    patterns = [
        r'(<button[^>]*id="btnUnescape"[^>]*>.*?</button>\s*)(</div>)',
        r'(<button[^>]*id="btnEscape"[^>]*>.*?</button>\s*)(</div>)',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, content, re.DOTALL)
        if match:
            content = content.replace(match.group(0), match.group(1) + CLEAR_BTN + '\n                ' + match.group(2), 1)
            return content, True
    
    return content, False


def add_template_select(content, page_name):
    """添加示例模板下拉"""
    if 'templateSelect' in content:
        return content, False
    
    # 在 toolbar 或操作区域添加
    if 'class="toolbar"' in content:
        # 找到 toolbar 结束位置
        pattern = r'(class="toolbar[^"]*"[^>]*>.*?<div[^>]*class="btn-group"[^>]*>)(.*?)(</div>\s*</div>)'
        match = re.search(pattern, content, re.DOTALL)
        if match:
            content = content.replace(
                match.group(0),
                match.group(1) + match.group(2) + '\n                    ' + TEMPLATE_SELECT + match.group(3),
                1
            )
            return content, True
    
    return content, False


def process_page(filepath, page_name):
    """处理单个页面"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    changes = []
    
    if page_name in PAGES_NEED_COPY:
        content, added = add_copy_button(content, page_name)
        if added:
            changes.append("Copy")
    
    if page_name in PAGES_NEED_CLEAR:
        content, added = add_clear_button(content, page_name)
        if added:
            changes.append("Clear")
    
    if page_name in PAGES_NEED_TEMPLATE:
        content, added = add_template_select(content, page_name)
        if added:
            changes.append("Template")
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, changes
    return False, []


def main():
    all_pages = set(PAGES_NEED_COPY + PAGES_NEED_CLEAR + PAGES_NEED_TEMPLATE)
    
    updated = 0
    for page in sorted(all_pages):
        filepath = os.path.join(PAGES_DIR, page)
        if os.path.exists(filepath):
            changed, changes = process_page(filepath, page)
            if changed:
                print(f"[OK] {page}: added {', '.join(changes)}")
                updated += 1
            else:
                print(f"[--] {page}: no changes needed")
        else:
            print(f"[X] {page}: not found")
    
    print(f"\n[OK] Updated {updated} pages")


if __name__ == "__main__":
    main()
