# -*- coding: utf-8 -*-
import os

fp = r'd:\网站开发-json\index.html'
content = open(fp, encoding='utf-8')

old_pattern = '''</a>
        <!-- Tutorial Card -->
        <a href="pages/blog.html" class="feature-card" aria-label="JSON Tutorial">'''

new_pattern = '''</a>
        <!-- Merge CSV Card -->
        <a href="pages/merge-csv.html" class="feature-card" aria-label="Merge CSV Files">
            <div class="feature-icon">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M16 16v4a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h2"></path>
                    <path d="M8 12v4a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2v-4a2 2 0 0 0-2-2H10a2 2 0 0 0-2 2"></path>
                </svg>
            </div>
            <h3>Merge CSV</h3>
            <p>Combine multiple CSV files into one. Merge spreadsheet data with automatic header alignment.</p>
        </a>
        <!-- Batch Rename Card -->
        <a href="pages/batch-file-renamer.html" class="feature-card" aria-label="Batch File Renamer">
            <div class="feature-icon">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path>
                    <path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path>
                </svg>
            </div>
            <h3>Batch Rename</h3>
            <p>Rename multiple files at once. Find and replace, add prefix/suffix, sequential numbering.</p>
        </a>
        <!-- PDF Split Card -->
        <a href="pages/pdf-split.html" class="feature-card" aria-label="PDF Split">
            <div class="feature-icon">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                    <polyline points="14 2 14 8 20 8"></polyline>
                    <line x1="12" y1="18" x2="12" y2="12"></line>
                    <line x1="9" y1="15" x2="15" y2="15"></line>
                </svg>
            </div>
            <h3>PDF Split</h3>
            <p>Extract specific pages from PDF documents. Split PDF into separate files.</p>
        </a>
        <!-- Tutorial Card -->
        <a href="pages/blog.html" class="feature-card" aria-label="JSON Tutorial">'''

new_content = content.read().replace(old_pattern, new_pattern)

if new_content != content.read():
    with open(fp, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('Updated index.html with new feature cards')
else:
    print('Pattern not found or already updated')
