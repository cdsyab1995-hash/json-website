#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Write a clean styles.css to fix the corrupted UTF-16 file
"""
import os

CSS_CONTENT = r"""/* AI JSON - Main Stylesheet - UTF-8 */

/* ============================================================
   CSS RESET & BASE
   ============================================================ */
*, *::before, *::after {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

:root {
    --bg-main: #131c2e;
    --bg-dark: #0a0f1a;
    --bg-card: #1f2940;
    --bg-secondary: #2a3654;
    --text-primary: #F8FAFC;
    --text-secondary: #94A3B8;
    --text-light: #64748B;
    --primary: #22C55E;
    --primary-hover: #16a34a;
    --danger: #EF4444;
    --warning: #F59E0B;
    --space-xs: 0.25rem;
    --space-sm: 0.5rem;
    --space-md: 1rem;
    --space-lg: 1.5rem;
    --space-xl: 2rem;
    --space-2xl: 3rem;
    --radius-sm: 4px;
    --radius-md: 8px;
    --radius-lg: 12px;
    --radius-xl: 16px;
    font-family: 'DM Sans', 'Segoe UI', -apple-system, BlinkMacSystemFont, sans-serif;
}

[data-theme="light"] {
    --bg-main: #f8fafc;
    --bg-dark: #ffffff;
    --bg-card: #ffffff;
    --bg-secondary: #e2e8f0;
    --text-primary: #0f172a;
    --text-secondary: #475569;
    --text-light: #94a3b8;
}

body {
    font-family: 'DM Sans', 'Segoe UI', -apple-system, BlinkMacSystemFont, sans-serif;
    background: var(--bg-main);
    color: var(--text-primary);
    line-height: 1.6;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
}

/* NAVBAR */
.navbar {
    background: var(--bg-dark);
    height: 64px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 var(--space-xl);
    border-bottom: 1px solid var(--bg-secondary);
    position: sticky;
    top: 0;
    z-index: 100;
}
.navbar-brand {
    font-size: 1.25rem;
    font-weight: 700;
    color: var(--text-primary);
    text-decoration: none;
    display: flex;
    align-items: center;
    gap: var(--space-sm);
    flex-shrink: 0;
}
.navbar-links {
    display: flex;
    align-items: center;
    gap: 0.25rem;
    overflow: hidden;
}
.nav-link {
    color: var(--text-secondary);
    text-decoration: none;
    padding: var(--space-sm) var(--space-md);
    border-radius: var(--radius-md);
    font-size: 0.875rem;
    font-weight: 500;
    height: 36px;
    min-width: 36px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 0.3rem;
    transition: color 0.15s, background 0.15s;
    white-space: nowrap;
}
.nav-link svg {
    width: 16px;
    height: 16px;
    flex-shrink: 0;
}
.nav-link:hover, .nav-link.active {
    color: var(--primary);
    background: rgba(34, 197, 94, 0.1);
}

/* Skip link */
.skip-link {
    position: absolute;
    top: -40px;
    left: 0;
    background: var(--primary);
    color: var(--bg-dark);
    padding: 8px;
    z-index: 9999;
    text-decoration: none;
    font-weight: 600;
}
.skip-link:focus { top: 0; }

/* Menu toggle */
.menu-toggle {
    display: none;
    background: none;
    border: none;
    color: var(--text-secondary);
    cursor: pointer;
    padding: 0.25rem;
}

/* CTA Button in navbar */
.navbar-cta {
    background: var(--primary) !important;
    color: var(--bg-dark) !important;
    font-weight: 600;
    border-radius: var(--radius-md);
    padding: 0.4rem 1rem !important;
    margin-left: 0.5rem;
}
.navbar-cta:hover {
    background: var(--primary-hover) !important;
    box-shadow: 0 2px 8px rgba(34, 197, 94, 0.3);
}

/* Theme Toggle */
.theme-toggle {
    background: none;
    border: 1px solid var(--bg-secondary);
    border-radius: var(--radius-md);
    color: var(--text-secondary);
    cursor: pointer;
    padding: 0.4rem;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 36px;
    height: 36px;
    transition: color 0.15s, border-color 0.15s;
}
.theme-toggle:hover { color: var(--primary); border-color: var(--primary); }
.theme-toggle svg { width: 16px; height: 16px; }
.icon-sun { display: none; }
[data-theme="light"] .icon-moon { display: none; }
[data-theme="light"] .icon-sun { display: block; }

/* DROPDOWN NAV */
.nav-dropdown {
    position: relative;
    display: inline-flex;
}
.nav-dropdown-menu {
    display: none;
    position: absolute;
    top: calc(100% + 4px);
    left: 0;
    background: var(--bg-dark);
    border: 1px solid var(--bg-secondary);
    border-radius: var(--radius-lg);
    padding: 0.5rem;
    min-width: 180px;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
    z-index: 200;
    flex-direction: column;
    gap: 0;
}
.nav-dropdown:hover .nav-dropdown-menu,
.nav-dropdown.open .nav-dropdown-menu {
    display: flex;
}
.nav-dropdown-menu .nav-link {
    justify-content: flex-start;
    width: 100%;
    height: auto;
    padding: 0.5rem 0.75rem;
    border-radius: var(--radius-sm);
}
.nav-dropdown-menu.wide {
    min-width: 400px;
    flex-wrap: wrap;
    flex-direction: row;
}
.nav-dropdown:hover .nav-dropdown-menu.wide,
.nav-dropdown.open .nav-dropdown-menu.wide {
    display: flex;
}
.nav-dropdown-menu.wide .nav-link { width: 48%; }

/* MAIN LAYOUT */
.main-container {
    flex: 1;
    max-width: 1200px;
    margin: 0 auto;
    padding: var(--space-xl);
    width: 100%;
    min-height: calc(100vh - 64px - 80px);
}
.page-header { margin-bottom: var(--space-xl); }
.page-header.text-center { text-align: center; }
.page-title {
    font-size: 2rem;
    font-weight: 700;
    color: var(--text-primary);
    margin-bottom: var(--space-sm);
    line-height: 1.3;
}
.page-description {
    color: var(--text-secondary);
    font-size: 1.05rem;
    max-width: 600px;
    margin: 0 auto;
}

/* FEATURE GRID & CARDS */
.feature-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
    gap: var(--space-lg);
    margin-top: var(--space-lg);
}
.feature-card {
    background: var(--bg-card);
    border: 1px solid var(--bg-secondary);
    border-radius: var(--radius-lg);
    padding: var(--space-lg);
    text-decoration: none;
    color: inherit;
    display: flex;
    flex-direction: column;
    gap: var(--space-sm);
    transition: border-color 0.15s, box-shadow 0.15s, transform 0.15s;
    min-height: 120px;
}
.feature-card:hover {
    border-color: var(--primary);
    box-shadow: 0 4px 16px rgba(34, 197, 94, 0.15);
    transform: translateY(-2px);
}
.feature-card h3 { font-size: 1rem; font-weight: 600; color: var(--text-primary); }
.feature-card p { font-size: 0.9rem; color: var(--text-secondary); line-height: 1.5; }
.feature-icon {
    width: 40px;
    height: 40px;
    background: rgba(34, 197, 94, 0.1);
    border-radius: var(--radius-md);
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
}
.feature-icon svg { width: 20px; height: 20px; stroke: var(--primary); }

/* TOOL AREA */
.tool-area {
    background: var(--bg-card);
    border-radius: var(--radius-lg);
    padding: var(--space-xl);
    border: 1px solid var(--bg-secondary);
}
.tool-area + .tool-area, .tool-area.mt-lg { margin-top: var(--space-xl); }
.section-label { color: var(--text-primary); font-size: 1.25rem; font-weight: 600; margin-bottom: var(--space-lg); }

/* CODE EDITOR */
.code-editor {
    width: 100%;
    min-height: 200px;
    padding: var(--space-md);
    border: 1px solid var(--bg-secondary);
    border-radius: var(--radius-md);
    font-family: 'Consolas', 'Monaco', 'Fira Code', monospace;
    font-size: 0.875rem;
    resize: vertical;
    background: var(--bg-dark);
    color: var(--text-primary);
    line-height: 1.6;
    transition: border-color 0.15s, box-shadow 0.15s;
}
.code-editor:focus {
    outline: none;
    border-color: var(--primary);
    box-shadow: 0 0 0 3px rgba(34, 197, 94, 0.15);
}
[data-theme="light"] .code-editor { background: #f1f5f9; color: #0f172a; }

/* BUTTONS */
.btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
    padding: 0.75rem 1.5rem;
    border: none;
    border-radius: var(--radius-md);
    font-size: 0.9375rem;
    font-weight: 600;
    cursor: pointer;
    text-decoration: none;
    transition: all 0.2s;
    white-space: nowrap;
}
.btn-primary { background: var(--primary); color: var(--bg-dark); }
.btn-primary:hover { background: var(--primary-hover); box-shadow: 0 4px 12px rgba(34, 197, 94, 0.3); }
.btn-secondary { background: transparent; color: var(--primary); border: 1px solid var(--primary); }
.btn-secondary:hover { background: rgba(34, 197, 94, 0.1); }
.btn-ghost { background: var(--bg-secondary); color: var(--text-secondary); }
.btn-ghost:hover { background: var(--bg-card); color: var(--text-primary); }
.btn svg { width: 16px; height: 16px; }

/* BUTTON GROUPS */
.btn-group { display: flex; gap: var(--space-sm); flex-wrap: wrap; align-items: center; }
.tool-actions { display: flex; gap: var(--space-sm); margin-bottom: var(--space-md); flex-wrap: wrap; align-items: center; }

/* STATUS BARS */
.status-bar {
    margin-top: var(--space-sm);
    padding: var(--space-sm) var(--space-md);
    border-radius: var(--radius-md);
    font-size: 0.875rem;
    font-weight: 500;
    min-height: 36px;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}
.status-bar.success { background: rgba(34, 197, 94, 0.1); color: var(--primary); border: 1px solid rgba(34, 197, 94, 0.2); }
.status-bar.error { background: rgba(239, 68, 68, 0.1); color: var(--danger); border: 1px solid rgba(239, 68, 68, 0.2); }
.status-bar.info { background: rgba(148, 163, 184, 0.1); color: var(--text-secondary); border: 1px solid var(--bg-secondary); }
.error-panel {
    background: rgba(239, 68, 68, 0.08);
    border: 1px solid rgba(239, 68, 68, 0.25);
    border-radius: var(--radius-md);
    padding: var(--space-md);
    margin-top: var(--space-sm);
    color: #fca5a5;
    font-size: 0.875rem;
    display: none;
}
.error-panel.visible { display: block; }

/* FORM ELEMENTS */
.form-group { display: flex; flex-direction: column; gap: var(--space-xs); margin-bottom: var(--space-md); }
label { font-size: 0.875rem; font-weight: 500; color: var(--text-secondary); }
input[type="text"], input[type="number"], select, textarea {
    background: var(--bg-dark);
    border: 1px solid var(--bg-secondary);
    border-radius: var(--radius-md);
    color: var(--text-primary);
    padding: 0.6rem 0.875rem;
    font-size: 0.875rem;
    font-family: inherit;
    width: 100%;
    transition: border-color 0.15s, box-shadow 0.15s;
}
input:focus, select:focus, textarea:focus {
    outline: none;
    border-color: var(--primary);
    box-shadow: 0 0 0 3px rgba(34, 197, 94, 0.15);
}

/* TABS */
.tabs { display: flex; border-bottom: 1px solid var(--bg-secondary); margin-bottom: var(--space-md); }
.tab-btn {
    background: none;
    border: none;
    border-bottom: 2px solid transparent;
    padding: var(--space-sm) var(--space-md);
    color: var(--text-secondary);
    font-size: 0.875rem;
    font-weight: 500;
    cursor: pointer;
    margin-bottom: -1px;
    transition: color 0.15s, border-color 0.15s;
}
.tab-btn.active, .tab-btn:hover { color: var(--primary); border-bottom-color: var(--primary); }

/* DIFF / COMPARE */
.diff-added { background: rgba(34, 197, 94, 0.12); color: #86efac; border-left: 3px solid var(--primary); padding-left: 0.5rem; }
.diff-removed { background: rgba(239, 68, 68, 0.12); color: #fca5a5; border-left: 3px solid var(--danger); padding-left: 0.5rem; }
.diff-modified { background: rgba(245, 158, 11, 0.12); color: #fcd34d; border-left: 3px solid var(--warning); padding-left: 0.5rem; }

/* JSON TREE VIEW */
.json-tree { font-family: 'Consolas', 'Monaco', monospace; font-size: 0.875rem; line-height: 1.8; }
.json-tree .key { color: #7dd3fc; }
.json-tree .string { color: #86efac; }
.json-tree .number { color: #fcd34d; }
.json-tree .boolean { color: #c4b5fd; }
.json-tree .null { color: #94a3b8; }
.tree-toggle { cursor: pointer; user-select: none; }
.tree-toggle::before { content: '\25B6'; display: inline-block; margin-right: 4px; transition: transform 0.15s; font-size: 0.7em; color: var(--text-secondary); }
.tree-toggle.open::before { transform: rotate(90deg); }

/* FAQ */
.faq-container { display: flex; flex-direction: column; gap: var(--space-sm); }
.faq-item { background: var(--bg-secondary); border-radius: var(--radius-md); overflow: hidden; }
.faq-question { padding: var(--space-md) var(--space-lg); cursor: pointer; font-weight: 500; color: var(--text-primary); list-style: none; display: flex; align-items: center; justify-content: space-between; user-select: none; }
.faq-question::-webkit-details-marker { display: none; }
.faq-question::after { content: '+'; font-size: 1.25rem; color: var(--primary); flex-shrink: 0; margin-left: var(--space-md); }
details[open] .faq-question::after { content: '\2212'; }
.faq-answer { padding: 0 var(--space-lg) var(--space-md); color: var(--text-secondary); font-size: 0.95rem; line-height: 1.7; }

/* FOOTER */
.footer {
    background: var(--bg-dark);
    color: var(--text-secondary);
    text-align: center;
    padding: var(--space-xl);
    margin-top: auto;
    border-top: 1px solid var(--bg-secondary);
    font-size: 0.875rem;
    min-height: 80px;
}
.footer a { color: var(--primary); text-decoration: none; }
.footer a:hover { text-decoration: underline; }

/* BLOG / ARTICLE */
.article-header { margin-bottom: var(--space-xl); }
.article-meta { display: flex; gap: var(--space-md); color: var(--text-secondary); font-size: 0.875rem; flex-wrap: wrap; margin-bottom: var(--space-sm); }
.article-content h2 { font-size: 1.5rem; font-weight: 700; color: var(--text-primary); margin: var(--space-xl) 0 var(--space-md); padding-bottom: 0.5rem; border-bottom: 1px solid var(--bg-secondary); }
.article-content h3 { font-size: 1.25rem; font-weight: 600; color: var(--primary); margin: var(--space-lg) 0 var(--space-sm); }
.article-content p { color: var(--text-secondary); line-height: 1.8; margin-bottom: var(--space-md); }
.article-content ul, .article-content ol { color: var(--text-secondary); padding-left: 1.5rem; margin-bottom: var(--space-md); line-height: 1.8; }
.article-content code { background: var(--bg-secondary); color: var(--primary); padding: 0.125rem 0.375rem; border-radius: var(--radius-sm); font-family: 'Consolas', 'Monaco', monospace; font-size: 0.875em; }
.article-content pre { background: var(--bg-dark); border: 1px solid var(--bg-secondary); border-radius: var(--radius-md); padding: var(--space-md); overflow-x: auto; margin-bottom: var(--space-md); }
.article-content pre code { background: none; padding: 0; color: var(--text-primary); font-size: 0.875rem; }
.article-content a { color: var(--primary); text-decoration: underline; }

/* BADGES */
.badge { display: inline-block; padding: 0.2rem 0.6rem; border-radius: 100px; font-size: 0.75rem; font-weight: 600; }
.badge-green { background: rgba(34, 197, 94, 0.15); color: var(--primary); }
.badge-blue { background: rgba(59, 130, 246, 0.15); color: #93c5fd; }
.badge-orange { background: rgba(245, 158, 11, 0.15); color: #fcd34d; }

/* ACCESSIBILITY */
a:focus-visible { outline: 2px solid var(--primary); outline-offset: 2px; border-radius: var(--radius-sm); }
button:focus-visible { outline: 2px solid var(--primary); outline-offset: 2px; }

/* RESPONSIVE */
@media (max-width: 768px) {
    .navbar { padding: 0 var(--space-md); position: relative; }
    .menu-toggle { display: flex; align-items: center; justify-content: center; order: 2; }
    .navbar-links {
        display: none;
        flex-direction: column;
        align-items: flex-start;
        position: absolute;
        top: 64px;
        left: 0;
        right: 0;
        background: var(--bg-dark);
        border-bottom: 1px solid var(--bg-secondary);
        padding: var(--space-md);
        gap: 0.25rem;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
        z-index: 99;
        max-height: 80vh;
        overflow-y: auto;
    }
    .navbar-links.open { display: flex; }
    .nav-link { width: 100%; justify-content: flex-start; }
    .nav-dropdown-menu, .nav-dropdown-menu.wide {
        position: static;
        box-shadow: none;
        border: none;
        padding-left: var(--space-lg);
        min-width: 0;
        width: 100%;
        background: transparent;
    }
    .nav-dropdown-menu.wide .nav-link { width: 100%; }
    .main-container { padding: var(--space-md); }
    .page-title { font-size: 1.5rem; }
    .feature-grid { grid-template-columns: 1fr; }
    .tool-area { padding: var(--space-md); }
    .two-col { grid-template-columns: 1fr; }
}

/* UTILITIES */
.text-center { text-align: center; }
.mt-sm { margin-top: var(--space-sm); }
.mt-md { margin-top: var(--space-md); }
.mt-lg { margin-top: var(--space-lg); }
.mt-xl { margin-top: var(--space-xl); }
.mb-sm { margin-bottom: var(--space-sm); }
.mb-md { margin-bottom: var(--space-md); }
.mb-lg { margin-bottom: var(--space-lg); }
.flex { display: flex; }
.flex-col { flex-direction: column; }
.items-center { align-items: center; }
.justify-between { justify-content: space-between; }
.gap-sm { gap: var(--space-sm); }
.gap-md { gap: var(--space-md); }
.gap-lg { gap: var(--space-lg); }
.hidden { display: none !important; }
.color-primary { color: var(--primary); }
.color-secondary { color: var(--text-secondary); }
.font-mono { font-family: 'Consolas', 'Monaco', 'Fira Code', monospace; }
.two-col { display: grid; grid-template-columns: 1fr 1fr; gap: var(--space-lg); }

/* BLOG GRID */
.blog-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: var(--space-lg); margin-top: var(--space-lg); }
.blog-card { background: var(--bg-card); border: 1px solid var(--bg-secondary); border-radius: var(--radius-lg); padding: var(--space-lg); text-decoration: none; color: inherit; display: flex; flex-direction: column; gap: var(--space-sm); transition: border-color 0.15s, box-shadow 0.15s, transform 0.15s; }
.blog-card:hover { border-color: var(--primary); box-shadow: 0 4px 16px rgba(34, 197, 94, 0.15); transform: translateY(-2px); }
.blog-card-date { font-size: 0.8rem; color: var(--text-secondary); }
.blog-card-title { font-size: 1rem; font-weight: 600; color: var(--primary); line-height: 1.4; }
.blog-card-excerpt { font-size: 0.9rem; color: var(--text-secondary); line-height: 1.6; flex: 1; }

/* SCROLLBAR */
::-webkit-scrollbar { width: 8px; height: 8px; }
::-webkit-scrollbar-track { background: var(--bg-dark); }
::-webkit-scrollbar-thumb { background: var(--bg-secondary); border-radius: 4px; }
::-webkit-scrollbar-thumb:hover { background: var(--text-secondary); }

/* P0: CLS PREVENTION */
img, video, iframe { contain: layout; }
img:not([width]):not([height]) { background-color: var(--bg-secondary); min-height: 100px; }
.font-loading { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
"""

out = r"d:\网站开发-json\css\styles.css"
with open(out, "w", encoding="utf-8", newline="\n") as f:
    f.write(CSS_CONTENT)

# Verify
with open(out, "rb") as f:
    first_bytes = f.read(10)

print(f"Written: {os.path.getsize(out)} bytes")
print(f"First bytes hex: {first_bytes.hex()}")
print(f"Is UTF-8 (starts with /): {first_bytes[:1] == b'/'}")

# Quick read test
with open(out, "r", encoding="utf-8") as f:
    lines = f.readlines()
print(f"Lines: {len(lines)}")
print(f"First line: {repr(lines[0][:60])}")
