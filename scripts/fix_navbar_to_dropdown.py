"""
Fix non-tool pages (about, changelog, blog, news, best-practices) to use
the same dropdown navbar + Try Formatter CTA as the tool pages.
"""
import re
from pathlib import Path

REPO = Path(r"d:\网站开发-json")

# Pages that currently have flat navbar (not tool pages)
TARGET_PAGES = {
    "about.html":           ("about",          "About"),
    "changelog.html":       ("changelog",      "Changelog"),
    "blog.html":            ("blog",            "Tutorial"),
    "news.html":            ("news",            "News"),
    "best-practices.html":  ("best-practices", "Best Practices"),
}

# Standard dropdown navbar for pages/xxx.html  (../ paths)
NAVBAR_TEMPLATE = """\
        <div class="navbar-links">
            <a href="../index.html" class="nav-link">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path>
                    <polyline points="9 22 9 12 15 12 15 22"></polyline>
                </svg>
                Home
            </a>
            <!-- Tools Dropdown -->
            <div class="nav-dropdown">
                <a href="#" class="nav-link nav-dropdown-toggle">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <rect x="3" y="3" width="7" height="7"></rect>
                        <rect x="14" y="3" width="7" height="7"></rect>
                        <rect x="14" y="14" width="7" height="7"></rect>
                        <rect x="3" y="14" width="7" height="7"></rect>
                    </svg>
                    Tools
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="width:12px;height:12px"><polyline points="6 9 12 15 18 9"></polyline></svg>
                </a>
                <div class="nav-dropdown-menu">
                    <a href="format.html" class="nav-link">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <polyline points="4 7 4 4 20 4 20 7"></polyline>
                            <line x1="9" y1="20" x2="15" y2="20"></line>
                            <line x1="12" y1="4" x2="12" y2="20"></line>
                        </svg>
                        Format
                    </a>
                    <a href="escape.html" class="nav-link">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <polyline points="16 18 22 12 16 6"></polyline>
                            <polyline points="8 6 2 12 8 18"></polyline>
                        </svg>
                        Escape
                    </a>
                    <a href="extract.html" class="nav-link">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <circle cx="11" cy="11" r="8"></circle>
                            <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                        </svg>
                        Extract
                    </a>
                    <a href="sort.html" class="nav-link">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <line x1="12" y1="5" x2="12" y2="19"></line>
                            <polyline points="19 12 12 19 5 12"></polyline>
                        </svg>
                        Sort
                    </a>
                    <a href="clean.html" class="nav-link">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"></path>
                        </svg>
                        Clean
                    </a>
                    <a href="xml.html" class="nav-link">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                            <polyline points="14 2 14 8 20 8"></polyline>
                        </svg>
                        XML
                    </a>
                    <a href="yaml.html" class="nav-link">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M4 4l4 16 4-16"></path>
                            <path d="M12 4l4 16"></path>
                        </svg>
                        YAML
                    </a>
                    <a href="viewer.html" class="nav-link">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path>
                            <circle cx="12" cy="12" r="3"></circle>
                        </svg>
                        Viewer
                    </a>
                    <a href="json2csv.html" class="nav-link">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                            <polyline points="14 2 14 8 20 8"></polyline>
                            <line x1="8" y1="13" x2="16" y2="13"></line>
                            <line x1="8" y1="17" x2="16" y2="17"></line>
                        </svg>
                        CSV
                    </a>
                    <a href="compare.html" class="nav-link">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M16 3h5v5"></path>
                            <path d="M8 3H3v5"></path>
                            <path d="M21 3l-7 7"></path>
                            <path d="M3 3l7 7"></path>
                            <path d="M16 21h5v-5"></path>
                            <path d="M8 21H3v-5"></path>
                            <path d="M21 21l-7-7"></path>
                            <path d="M3 21l7-7"></path>
                        </svg>
                        Compare
                    </a>
                </div>
            </div>
            <a href="blog.html" class="nav-link BLOG_ACTIVE">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path>
                    <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path>
                </svg>
                Tutorial
            </a>
            <a href="best-practices.html" class="nav-link BESTPRACTICES_ACTIVE">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
                    <polyline points="22 4 12 14.01 9 11.01"></polyline>
                </svg>
                Best Practices
            </a>
            <a href="news.html" class="nav-link NEWS_ACTIVE">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"></path>
                </svg>
                News
            </a>
            <a href="about.html" class="nav-link ABOUT_ACTIVE">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <circle cx="12" cy="12" r="10"></circle>
                    <line x1="12" y1="16" x2="12" y2="12"></line>
                    <line x1="12" y1="8" x2="12.01" y2="8"></line>
                </svg>
                About
            </a>
            <a href="changelog.html" class="nav-link CHANGELOG_ACTIVE">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <circle cx="12" cy="12" r="10"></circle>
                    <polyline points="12 6 12 12 16 14"></polyline>
                </svg>
                Changelog
            </a>
            <!-- CTA Button -->
            <a href="format.html" class="nav-link navbar-cta">
                Try Formatter
            </a>
        </div>"""


def build_navbar(page_key: str) -> str:
    nav = NAVBAR_TEMPLATE
    # Set active class for current page
    for key in ["BLOG", "BESTPRACTICES", "NEWS", "ABOUT", "CHANGELOG"]:
        placeholder = f"{key}_ACTIVE"
        if page_key.upper().replace("-", "") == key:
            nav = nav.replace(placeholder, "active")
        else:
            nav = nav.replace(placeholder, "")
    # Clean up double spaces from empty replacements
    nav = re.sub(r' class="nav-link "', ' class="nav-link"', nav)
    return nav


def fix_page(filepath: Path, page_key: str, page_label: str):
    content = filepath.read_text(encoding="utf-8")

    # Find the <div class="navbar-links"> ... </div> block and replace it
    # Strategy: match from <div class="navbar-links"> to the closing </div> of that block
    # We look for the pattern and replace everything inside navbar-links

    new_navbar = build_navbar(page_key)

    # Pattern: match <div class="navbar-links">...</div> (outermost, not nested)
    # Use a simple approach: find start tag, count depth to find matching close tag
    start_tag = '<div class="navbar-links">'
    start_idx = content.find(start_tag)
    if start_idx == -1:
        print(f"  [SKIP] {filepath.name} - no navbar-links found")
        return False

    # Find the matching closing </div>
    search_from = start_idx + len(start_tag)
    depth = 1
    pos = search_from
    while pos < len(content) and depth > 0:
        open_pos = content.find("<div", pos)
        close_pos = content.find("</div>", pos)
        if close_pos == -1:
            break
        if open_pos != -1 and open_pos < close_pos:
            depth += 1
            pos = open_pos + 4
        else:
            depth -= 1
            if depth == 0:
                end_idx = close_pos + len("</div>")
            pos = close_pos + 6

    if depth != 0:
        print(f"  [ERROR] {filepath.name} - could not find matching </div>")
        return False

    old_block = content[start_idx:end_idx]

    # Check if already has dropdown
    if "nav-dropdown" in old_block:
        # Has dropdown but may be missing Try Formatter
        if "navbar-cta" not in old_block:
            # Add Try Formatter before the closing </div>
            new_block = old_block[:-6] + '\n            <!-- CTA Button -->\n            <a href="format.html" class="nav-link navbar-cta">\n                Try Formatter\n            </a>\n        </div>'
            content = content[:start_idx] + new_block + content[end_idx:]
            filepath.write_text(content, encoding="utf-8")
            print(f"  [FIXED CTA] {filepath.name} - added Try Formatter button")
            return True
        else:
            print(f"  [OK] {filepath.name} - already has dropdown + CTA")
            return False
    else:
        # Replace entire navbar-links block with new dropdown version
        content = content[:start_idx] + new_navbar + content[end_idx:]
        filepath.write_text(content, encoding="utf-8")
        print(f"  [FIXED] {filepath.name} - replaced flat nav with dropdown + CTA")
        return True


def main():
    pages_dir = REPO / "pages"
    fixed = []
    for filename, (page_key, page_label) in TARGET_PAGES.items():
        filepath = pages_dir / filename
        if not filepath.exists():
            print(f"  [NOT FOUND] {filename}")
            continue
        print(f"Processing {filename}...")
        if fix_page(filepath, page_key, page_label):
            fixed.append(filename)

    print(f"\n=== Done. Fixed {len(fixed)} files: {fixed} ===")


if __name__ == "__main__":
    main()
