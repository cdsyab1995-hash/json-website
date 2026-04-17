#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix hash-generator, jwt-decoder, uuid-generator pages
These pages have incorrect structure: missing </head> and <body> tags
Insert them after the </style> tag
"""
import os
import re

PWA_TAGS_BEFORE_CLOSE_HEAD = """    <!-- PWA Manifest -->
    <link rel="manifest" href="../manifest.json">
    <meta name="theme-color" content="#22C55E">
    <meta name="mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <meta name="apple-mobile-web-app-title" content="JSON Tools">
    <link rel="apple-touch-icon" href="../images/icon-192.png">
</head>
<body>"""

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
    </script>"""

files = ['hash-generator.html', 'jwt-decoder.html', 'uuid-generator.html']
for filename in files:
    path = r'd:\网站开发-json\pages\{}'.format(filename)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Look for last </style> before the navigation links
    # The pattern is: </style>\n    <meta name="twitter... or </style>\n<a href
    # We need to:
    # 1. Insert </head><body> after the last </style> in head area
    # 2. Wrap the content in <body></body>
    # 3. Add PWA tags before </head>
    # 4. Add SW script before </body>
    
    # Find the first occurrence of <a href= that appears to be navbar link (not in head)
    # These problematic files have nav links directly after </style>
    
    # Strategy: Replace the transition from head to body content
    # Find: </style>\n    <meta name="twitter..." + navigation links
    
    # Find where </style> is, then check what follows
    style_end = content.find('</style>')
    if style_end == -1:
        print(f'WARNING: No </style> in {filename}')
        continue
    
    after_style = content[style_end + 8:]  # After </style>
    
    # Check what's right after </style>
    next_meaningful = after_style.strip()[:100]
    print(f'{filename}: After </style>: {repr(next_meaningful[:50])}')
    
    # Insert PWA tags and close head/open body after </style>
    before_style_end = content[:style_end + 8]
    
    # Replace the </style> + everything after (before body content) 
    # with </style> + PWA tags + </head><body>
    
    # Find the twitter meta and nav links pattern
    # Insert </head><body> before the nav/body content
    
    # The file has: </style>\n    <meta twitter...>\n<a href...> (body content starts)
    # We need to find where proper body content begins
    
    # Look for pattern right after </style>: twitter meta then nav links
    twitter_match = re.search(r'\s*<meta name="twitter:card"', after_style)
    if twitter_match:
        # Twitter meta is still in head, find after it
        twitter_section_end = after_style.find('</head>', twitter_match.start())
        if twitter_section_end == -1:
            # Find the first <a href that's a nav link (body content)
            nav_match = re.search(r'\n(<a href=|<nav|<header|<body)', after_style)
            if nav_match:
                head_remaining = after_style[:nav_match.start()]
                body_content = after_style[nav_match.start():]
                
                new_content = (before_style_end + 
                               head_remaining + '\n' +
                               PWA_TAGS_BEFORE_CLOSE_HEAD + 
                               body_content)
                
                # Add SW script before </body>
                new_content = new_content.replace('<\\/script></body>', 
                    '<\\/script>' + SW_SCRIPT + '\n</body>')
                
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f'Fixed {filename}')
            else:
                print(f'WARNING: Could not find body content start in {filename}')
        else:
            print(f'{filename} already has </head>')
    else:
        # No twitter meta, find body content directly after </style>
        nav_match = re.search(r'\n(<a href=|<nav|<header|<body)', after_style)
        if nav_match:
            head_remaining = after_style[:nav_match.start()]
            body_content = after_style[nav_match.start():]
            new_content = (before_style_end + 
                           head_remaining + '\n' +
                           PWA_TAGS_BEFORE_CLOSE_HEAD + 
                           body_content)
            new_content = new_content.replace('<\\/script></body>', 
                '<\\/script>' + SW_SCRIPT + '\n</body>')
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'Fixed {filename} (no twitter)')
        else:
            print(f'WARNING: Could not find body content in {filename}')
