#!/usr/bin/env python3
"""
批量更新所有HTML页面，添加性能优化标签
"""
import os
import re

def add_performance_optimizations(html_content, page_type="tool"):
    """添加性能优化标签"""
    
    # DNS Prefetch 和 Preconnect
    perf_tags = '''    <!-- DNS Prefetch & Preconnect -->
    <link rel="dns-prefetch" href="https://fonts.googleapis.com">
    <link rel="dns-prefetch" href="https://fonts.gstatic.com">
    <link rel="preconnect" href="https://fonts.googleapis.com" crossorigin>
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <!-- Preload 关键字体 -->
    <link rel="preload" as="font" type="font/woff2" crossorigin href="https://fonts.gstatic.com/s/dmsans/v15/rP2Hp2ywxg089UriCZOIHQ.woff2" onload="this.onload=null">
    <!-- Google Fonts 异步加载 -->
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&display=swap" media="print" onload="this.media='all'">
    <noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&display=swap"></noscript>
    <!-- 关键CSS内联 -->
    <style>
    *,*::before,*::after{margin:0;padding:0;box-sizing:border-box}
    :root{--bg-main:#131c2e;--bg-dark:#0a0f1a;--bg-card:#1f2940;--bg-secondary:#2a3654;--text-primary:#F8FAFC;--text-secondary:#94A3B8;--primary:#22C55E;--space-sm:0.5rem;--space-md:1rem;--space-xl:2rem;--radius-md:8px;--radius-lg:12px;font-family:'DM Sans','Segoe UI',-apple-system,BlinkMacSystemFont,sans-serif}
    body{background:var(--bg-main);color:var(--text-primary);line-height:1.6;min-height:100vh;display:flex;flex-direction:column}
    .navbar{background:var(--bg-dark);height:64px;display:flex;align-items:center;justify-content:space-between;padding:0 var(--space-xl);border-bottom:1px solid var(--bg-secondary);position:sticky;top:0;z-index:100}
    .navbar-brand{font-size:1.25rem;font-weight:700;color:var(--text-primary);text-decoration:none;display:flex;align-items:center;gap:var(--space-sm)}
    .navbar-links{display:flex;align-items:center;gap:0.25rem;flex-wrap:wrap}
    .nav-link{color:var(--text-secondary);text-decoration:none;padding:var(--space-sm) var(--space-md);border-radius:var(--radius-md);font-size:.875rem;font-weight:500;height:36px;min-width:36px;display:inline-flex;align-items:center;justify-content:center;gap:0.3rem}
    .nav-link:hover,.nav-link.active{color:var(--primary);background:rgba(34,197,94,.1)}
    .main-container{flex:1;max-width:1200px;margin:0 auto;padding:var(--space-xl);width:100%}
    .tool-area{background:var(--bg-card);border-radius:var(--radius-lg);padding:var(--space-xl);border:1px solid var(--bg-secondary)}
    .code-editor{width:100%;min-height:200px;padding:var(--space-md);border:1px solid var(--bg-secondary);border-radius:var(--radius-md);font-family:'Consolas','Monaco',monospace;font-size:0.875rem;resize:vertical;background:var(--bg-dark);color:var(--text-primary)}
    .code-editor:focus{outline:none;border-color:var(--primary);box-shadow:0 0 0 3px rgba(34,197,94,.15)}
    .btn{display:inline-flex;align-items:center;justify-content:center;gap:0.5rem;padding:0.75rem 1.5rem;border:none;border-radius:var(--radius-md);font-size:0.9375rem;font-weight:600;cursor:pointer;text-decoration:none;transition:all 0.2s;transform:translateZ(0);will-change:transform,box-shadow}
    .btn-primary{background:var(--primary);color:var(--bg-dark)}
    .btn-primary:hover{background:var(--primary-hover);box-shadow:0 4px 12px rgba(34,197,94,.3)}
    .btn-secondary{background:transparent;color:var(--primary);border:1px solid var(--primary)}
    .btn-secondary:hover{background:rgba(34,197,94,.1)}
    .footer{background:var(--bg-dark);color:var(--text-secondary);text-align:center;padding:var(--space-xl);margin-top:auto;border-top:1px solid var(--bg-secondary)}
    .footer a{color:var(--primary);text-decoration:none}
    </style>
    <!-- 预加载资源 -->
    <link rel="preload" href="css/styles.css" as="style">
    <link rel="preload" href="js/app.js" as="script">
    <!-- 异步加载完整CSS -->
    <link rel="stylesheet" href="css/styles.css" media="print" onload="this.media='all'">
    <noscript><link rel="stylesheet" href="css/styles.css"></noscript>
'''
    
    # 查找并替换<head>标签后的位置
    # 找到 <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans...
    # 或者如果没有，找到 </head> 前面的位置
    
    # 移除旧的字体和CSS链接
    patterns_to_remove = [
        r'<link rel="preconnect" href="https://fonts.googleapis\.com">\s*',
        r'<link rel="preconnect" href="https://fonts\.gstatic\.com" crossorigin>\s*',
        r'<link rel="stylesheet" href="https://fonts\.googleapis\.com/css2?family=DM\+Sans[^"]*">\s*',
        r'<link rel="stylesheet" href="css/styles\.css">\s*',
    ]
    
    for pattern in patterns_to_remove:
        html_content = re.sub(pattern, '', html_content)
    
    # 在</head>前插入新的优化标签
    html_content = html_content.replace('</head>', perf_tags + '</head>')
    
    # 添加JS优化脚本（如果有</body>）
    js_optimization = '''
    <!-- 性能优化：预取下一页资源 -->
    <script>
    (function(){
        var idle=window.requestIdleCallback||function(cb){return setTimeout(cb,1)};
        idle(function(){
            document.querySelectorAll('a[href^="pages/"],a[href^="../"]').forEach(function(link){
                var pr=document.createElement('link');
                pr.rel='prefetch';
                pr.href=link.href;
                document.head.appendChild(pr);
            });
        },{timeout:2000});
    })();
    </script>
    '''
    
    # 确保JS defer加载
    if 'src="js/app.js"' in html_content:
        html_content = re.sub(
            r'<script\s+src="js/app\.js"[^>]*>\s*</script>',
            '<script src="js/app.js" defer></script>',
            html_content
        )
    elif 'src="../js/app.js"' in html_content:
        html_content = re.sub(
            r'<script\s+src="../js/app\.js"[^>]*>\s*</script>',
            '<script src="../js/app.js" defer></script>',
            html_content
        )
    
    return html_content


def update_file(filepath):
    """更新单个文件"""
    print(f"Updating: {filepath}")
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 跳过已有优化标签的文件
        if 'dns-prefetch' in content:
            print(f"  SKIP - Already optimized")
            return False
        
        # 确定页面类型
        if 'pages/' in filepath:
            page_type = 'tool'
        else:
            page_type = 'index'
        
        # 添加性能优化
        new_content = add_performance_optimizations(content, page_type)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"  DONE")
        return True
    except Exception as e:
        print(f"  ERROR: {e}")
        return False


def main():
    """主函数"""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(base_dir)
    
    # 需要更新的HTML文件列表
    html_files = [
        os.path.join(project_dir, 'index.html'),
    ]
    
    # 添加工具页面
    pages_dir = os.path.join(project_dir, 'pages')
    if os.path.exists(pages_dir):
        for filename in os.listdir(pages_dir):
            if filename.endswith('.html'):
                html_files.append(os.path.join(pages_dir, filename))
    
    print(f"Found {len(html_files)} HTML files to update")
    print("-" * 50)
    
    updated = 0
    skipped = 0
    for filepath in sorted(html_files):
        if update_file(filepath):
            updated += 1
        else:
            skipped += 1
    
    print("-" * 50)
    print(f"Updated: {updated}, Skipped: {skipped}")


if __name__ == '__main__':
    main()
