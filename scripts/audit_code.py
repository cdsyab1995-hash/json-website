#!/usr/bin/env python3
"""
全面代码审计脚本 - 精简并排查bug
"""
import os
import re
import sys
from collections import Counter

sys.stdout.reconfigure(encoding='utf-8')

root_dir = r'd:\网站开发-json'

def audit_css():
    """审计 CSS 文件"""
    print('=' * 60)
    print('CSS 审计')
    print('=' * 60)
    
    css_path = os.path.join(root_dir, 'css', 'styles.css')
    with open(css_path, 'r', encoding='utf-8') as f:
        css = f.read()
    
    issues = []
    
    # 1. 检查重复的CSS变量定义
    var_pattern = r'(--[\w-]+):\s*([^;]+);'
    vars_found = re.findall(var_pattern, css)
    var_names = [v[0] for v in vars_found]
    duplicates = [v for v, count in Counter(var_names).items() if count > 1]
    if duplicates:
        issues.append(f'Duplicate CSS variables: {duplicates}')
    
    # 2. 检查空规则
    empty_rules = re.findall(r'([^{}]+)\{\s*\}', css)
    if empty_rules:
        issues.append(f'Empty CSS rules: {len(empty_rules)} found')
    
    # 3. 检查未闭合的括号
    open_braces = css.count('{')
    close_braces = css.count('}')
    if open_braces != close_braces:
        issues.append(f'Unmatched braces: {open_braces} open, {close_braces} close')
    
    # 4. 检查过长的选择器
    long_selectors = re.findall(r'[^\n]{100,}', css)
    if long_selectors:
        issues.append(f'Very long lines: {len(long_selectors)} found')
    
    # 5. 统计CSS体积
    css_size = len(css.encode('utf-8'))
    print(f'CSS file size: {css_size:,} bytes ({css_size/1024:.1f} KB)')
    
    # 6. 检查未使用的通用选择器
    unused_patterns = ['* {', '.clearfix {', '.text-center {', '.text-left {', '.text-right {']
    for p in unused_patterns:
        if p in css:
            issues.append(f'Potentially unused: {p}')
    
    if issues:
        print('Issues found:')
        for issue in issues:
            print(f'  - {issue}')
    else:
        print('No major issues found')
    
    return issues

def audit_html():
    """审计 HTML 文件"""
    print('\n' + '=' * 60)
    print('HTML 审计')
    print('=' * 60)
    
    html_files = []
    
    # 收集所有 HTML 文件
    for root, dirs, files in os.walk(root_dir):
        for f in files:
            if f.endswith('.html'):
                html_files.append(os.path.join(root, f))
    
    issues = []
    total_inline_css = 0
    total_inline_js = 0
    duplicate_ids = {}
    broken_links = []
    
    for filepath in html_files:
        rel_path = os.path.relpath(filepath, root_dir)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 1. 统计内联样式
        inline_styles = len(re.findall(r'style="[^"]*"', content))
        total_inline_css += inline_styles
        if inline_styles > 5:
            issues.append(f'{rel_path}: {inline_styles} inline styles (should use CSS classes)')
        
        # 2. 统计内联脚本
        inline_scripts = len(re.findall(r'<script[^>]*>(?!.*</script>)', content))
        total_inline_js += len(re.findall(r'<script[^>]*>.*?</script>', content, re.DOTALL))
        
        # 3. 检查重复的 ID
        ids = re.findall(r'\sid="([^"]+)"', content)
        for id_name in ids:
            if id_name not in duplicate_ids:
                duplicate_ids[id_name] = []
            duplicate_ids[id_name].append(rel_path)
        
        # 4. 检查无意义的注释
        empty_comments = len(re.findall(r'<!--\s*-->', content))
        if empty_comments > 0:
            issues.append(f'{rel_path}: {empty_comments} empty HTML comments')
        
        # 5. 检查重复的 meta 标签
        meta_patterns = ['description', 'keywords', 'author', 'robots']
        for pattern in meta_patterns:
            matches = re.findall(rf'<meta name="{pattern}"', content)
            if len(matches) > 1:
                issues.append(f'{rel_path}: duplicate <meta name="{pattern}"> x{len(matches)}')
        
        # 6. 检查冗余的 class
        redundant_classes = re.findall(r'class="[^"]*(?:undefined|null|false)[^"]*"', content)
        if redundant_classes:
            issues.append(f'{rel_path}: suspicious class names: {redundant_classes[:3]}')
    
    # 输出重复的 ID
    duplicate_ids = {k: v for k, v in duplicate_ids.items() if len(v) > 1}
    if duplicate_ids:
        issues.append(f'Duplicate IDs found in {len(duplicate_ids)} elements')
        for id_name, files in list(duplicate_ids.items())[:5]:
            print(f'  ID "{id_name}" used in: {files}')
    
    print(f'Total HTML files: {len(html_files)}')
    print(f'Total inline styles: {total_inline_css}')
    print(f'Total inline scripts: {total_inline_js}')
    
    if issues:
        print(f'\nIssues found: {len(issues)}')
        for issue in issues[:20]:
            print(f'  - {issue}')
    else:
        print('No major issues found')
    
    return issues

def audit_js():
    """审计 JS 文件"""
    print('\n' + '=' * 60)
    print('JavaScript 审计')
    print('=' * 60)
    
    js_path = os.path.join(root_dir, 'js', 'app.js')
    with open(js_path, 'r', encoding='utf-8') as f:
        js = f.read()
    
    issues = []
    
    # 1. 检查 console.log
    console_logs = len(re.findall(r'console\.(log|debug|info)', js))
    if console_logs > 0:
        issues.append(f'{console_logs} console.log/debug/info statements (should be removed in production)')
    
    # 2. 检查调试代码
    debugger_stmt = len(re.findall(r'\bdebugger\b', js))
    if debugger_stmt > 0:
        issues.append(f'{debugger_stmt} debugger statements')
    
    # 3. 检查未使用的变量警告
    unused_vars = re.findall(r'(?:var|let|const)\s+(\w+)\s*;', js)
    unused_vars = [v for v in unused_vars if v.startswith('_') or v in ['unused', 'temp', 'tmp']]
    if unused_vars:
        issues.append(f'Potentially unused variables: {unused_vars}')
    
    # 4. 检查 TODO/FIXME
    todos = re.findall(r'(TODO|FIXME|HACK|XXX):', js)
    if todos:
        issues.append(f'{len(todos)} TODO/FIXME comments')
    
    # 5. 检查过于复杂的函数
    func_complexity = js.count('function ')
    issues.append(f'{func_complexity} function declarations')
    
    js_size = len(js.encode('utf-8'))
    print(f'JS file size: {js_size:,} bytes ({js_size/1024:.1f} KB)')
    
    # 6. 检查重复的代码块
    lines = [l.strip() for l in js.split('\n') if l.strip() and not l.strip().startswith('//')]
    line_counts = Counter(lines)
    duplicates = {k: v for k, v in line_counts.items() if v > 3 and len(k) > 30}
    if duplicates:
        issues.append(f'{len(duplicates)} duplicate code blocks found')
    
    if issues:
        print('Issues found:')
        for issue in issues:
            print(f'  - {issue}')
    else:
        print('No major issues found')
    
    return issues

def check_navbar_consistency():
    """检查导航栏一致性"""
    print('\n' + '=' * 60)
    print('导航栏一致性检查')
    print('=' * 60)
    
    pages_dir = os.path.join(root_dir, 'pages')
    nav_patterns = {}
    
    for filename in os.listdir(pages_dir):
        if not filename.endswith('.html'):
            continue
        
        filepath = os.path.join(pages_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 提取导航链接
        nav_links = re.findall(r'href="([^"]+)"[^>]*>([^<]+)<', content)
        key = tuple(sorted([l[1].strip() for l in nav_links if l[1].strip()]))
        if key not in nav_patterns:
            nav_patterns[key] = []
        nav_patterns[key].append(filename)
    
    print(f'Found {len(nav_patterns)} different navigation patterns:')
    for i, (pattern, files) in enumerate(nav_patterns.items()):
        print(f'\nPattern {i+1} ({len(files)} files):')
        for f in files[:5]:
            print(f'  - {f}')
        if len(files) > 5:
            print(f'  ... and {len(files)-5} more')

if __name__ == '__main__':
    print('AI JSON 网站代码审计报告')
    print('=' * 60)
    print()
    
    audit_css()
    audit_html()
    audit_js()
    check_navbar_consistency()
    
    print('\n' + '=' * 60)
    print('审计完成')
    print('=' * 60)
