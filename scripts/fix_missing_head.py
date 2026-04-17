#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix 3 pages that are missing </head> closing tag
and inject PWA tags at the correct location
"""
import os
import re

PWA_TAGS = """    <!-- PWA Manifest -->
    <link rel="manifest" href="../manifest.json">
    <meta name="theme-color" content="#22C55E">
    <meta name="mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <meta name="apple-mobile-web-app-title" content="JSON Tools">
    <link rel="apple-touch-icon" href="../images/icon-192.png">
</head>"""

SW_SCRIPT = """
    <!-- PWA Service Worker -->
    <script>
    if ('serviceWorker' in navigator) {
        window.addEventListener('load', function() {
            navigator.serviceWorker.register('/sw.js').then(function(reg) {
                console.log('[PWA] SW registered:', reg.scope);
            }).catch(function(err) {
                console.warn('[PWA] SW registration failed:', err);
            });
        });
    }
    </script>
</body>"""

files = ['hash-generator.html', 'jwt-decoder.html', 'uuid-generator.html']
for filename in files:
    path = r'd:\网站开发-json\pages\{}'.format(filename)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the <body tag which marks end of head section
    # Look for the pattern: last style/script tag or preload/link tag before <body
    body_match = re.search(r'(\<body[^>]*\>)', content, re.IGNORECASE)
    if body_match:
        insert_pos = body_match.start()
        before_body = content[:insert_pos]
        after_body = content[insert_pos:]
        
        # Add </head> and PWA tags before <body>
        new_content = before_body + PWA_TAGS + '\n' + after_body
        
        # Also add SW registration before </body>
        new_content = new_content.replace('</body>', SW_SCRIPT)
        
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Fixed {filename}')
    else:
        print(f'WARNING: Could not find <body> in {filename}')
