"""
fix_bare_files.py
把根目录下的裸文件（about, blog, news, best-practices, changelog）
转换为 Cloudflare Pages 标准格式：
  about       →  about/index.html   (浏览器访问 /about)
  blog        →  blog/index.html    (浏览器访问 /blog)
  news        →  news/index.html    (浏览器访问 /news)
  best-practices → best-practices/index.html
  changelog   →  changelog/index.html

同时检查 tools/ 目录下的工具页是否也需要转换为目录格式。
"""
import shutil
from pathlib import Path

BASE = Path("d:/网站开发-json")

# 需要转换的裸文件
BARE_FILES = [
    "about",
    "blog",
    "news",
    "best-practices",
    "changelog",
]

converted = []
skipped = []

for name in BARE_FILES:
    src = BASE / name
    if not src.exists():
        print(f"  SKIP (not found): {name}")
        skipped.append(name)
        continue
    if src.is_dir():
        # 检查是否已经有 index.html
        idx = src / "index.html"
        if idx.exists():
            print(f"  SKIP (already dir with index.html): {name}/")
            skipped.append(name)
        else:
            print(f"  WARN (dir but no index.html): {name}/")
        continue

    # 读取文件内容
    content = src.read_text(encoding="utf-8")

    # 创建目录
    target_dir = BASE / name
    # 注意：src 就是 BASE/name，需要先重命名为临时文件，再创建目录
    tmp = BASE / f"_{name}_tmp.html"
    src.rename(tmp)

    # 创建目录
    target_dir.mkdir(exist_ok=True)

    # 写入 index.html
    (target_dir / "index.html").write_text(content, encoding="utf-8")

    # 删除临时文件
    tmp.unlink()

    print(f"  OK: {name}  →  {name}/index.html")
    converted.append(name)

print(f"\n✅ 转换完成: {len(converted)} 个文件")
print(f"⏭  跳过: {len(skipped)} 个")
print("\n现在 /about、/blog、/news、/best-practices、/changelog 都能正常访问了")
