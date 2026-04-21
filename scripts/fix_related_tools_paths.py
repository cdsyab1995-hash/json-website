# -*- coding: utf-8 -*-
"""修复 pages/ 目录下的 Related Tools 路径问题

问题：pages/ 目录下的 HTML 文件使用了 href="../pages/xxx.html"
正确：应该是 href="xxx.html"（因为文件本身就在 pages/ 目录下）
"""
import os
import re

def fix_pages_related_tools():
    """修复 pages/ 目录下的 Related Tools 链接"""
    pages_dir = r"d:\网站开发-json\pages"
    fixed_count = 0
    
    for filename in os.listdir(pages_dir):
        if not filename.endswith('.html'):
            continue
        
        # 跳过子目录下的文件（news/, blog/ 等）
        if '/' in filename or '\\' in filename:
            continue
            
        filepath = os.path.join(pages_dir, filename)
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 修复 Related Tools 中的 ../pages/ 路径
        # 例如: href="../pages/format.html" -> href="format.html"
        new_content = re.sub(r'href="\.\./pages/', 'href="', content)
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"[OK] Fixed: {filename}")
            fixed_count += 1
    
    print(f"\nTotal files fixed in pages/: {fixed_count}")
    return fixed_count

def fix_subdirectory_navbar():
    """修复子目录（news/, blog/）下的导航栏路径"""
    base_dir = r"d:\网站开发-json\pages"
    fixed_count = 0
    
    for subdir in ['news', 'blog']:
        subdir_path = os.path.join(base_dir, subdir)
        if not os.path.exists(subdir_path):
            continue
        
        for filename in os.listdir(subdir_path):
            if not filename.endswith('.html'):
                continue
            
            filepath = os.path.join(subdir_path, filename)
            
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 子目录下的文件导航栏链接修复
            # href="../pages/blog.html" -> href="../blog.html"
            new_content = re.sub(r'href="\.\./pages/', 'href="../', content)
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"[OK] Fixed: {subdir}/{filename}")
                fixed_count += 1
    
    print(f"\nTotal files fixed in subdirectories: {fixed_count}")
    return fixed_count

if __name__ == "__main__":
    print("=" * 50)
    print("Fixing Related Tools path issues")
    print("=" * 50)
    
    count1 = fix_pages_related_tools()
    count2 = fix_subdirectory_navbar()
    
    print("\n" + "=" * 50)
    print(f"Grand total: {count1 + count2} files fixed")
    print("=" * 50)
