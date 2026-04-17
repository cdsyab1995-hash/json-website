#!/usr/bin/env python3
"""Analyze index.html layout for CLS issues"""
import os
import re

fp = r'd:\网站开发-json\index.html'
with open(fp, 'r', encoding='utf-8') as f:
    content = f.read()

print('=== index.html Layout Analysis ===\n')

# Check for dynamically loaded content
print('1. Dynamic content patterns:')
if 'innerHTML' in content:
    print('   [FOUND] innerHTML usage - may cause CLS')
if 'document.write' in content:
    print('   [FOUND] document.write - causes CLS')
if 'fetch(' in content or 'XMLHttpRequest' in content:
    print('   [FOUND] Async content loading')
if '@import' in content:
    print('   [FOUND] @import - may cause CLS')

# Check for fonts
print('\n2. Font loading:')
if 'font-display: swap' in content:
    print('   [OK] font-display: swap')
elif 'display=swap' in content:
    print('   [OK] display=swap in URL')
else:
    print('   [WARNING] No font-display specified')

# Check for critical CSS
print('\n3. CSS loading:')
if 'media="print"' in content:
    print('   [OK] Non-blocking CSS (media="print" trick)')
if 'rel="preload"' in content:
    print('   [OK] CSS preloading')
if 'rel="preconnect"' in content:
    print('   [OK] Preconnect for fonts')

# Check for third-party scripts
print('\n4. Third-party scripts:')
third_party = []
if 'cdnjs.cloudflare.com' in content:
    third_party.append('Cloudflare CDN')
if 'unpkg.com' in content:
    third_party.append('unpkg')
if 'jsdelivr' in content:
    third_party.append('jsDelivr')
if 'google-analytics' in content:
    third_party.append('Google Analytics')
if 'googletagmanager' in content:
    third_party.append('GTM')
if 'adsense' in content:
    third_party.append('AdSense')

if third_party:
    for tp in third_party:
        print(f'   [FOUND] {tp}')
else:
    print('   [OK] No third-party scripts')

# Check ads
print('\n5. Ads:')
if 'adsbygoogle' in content:
    print('   [FOUND] Google AdSense')
if 'ad-container' in content.lower():
    print('   [FOUND] Ad container')
if 'advertisement' in content.lower():
    print('   [FOUND] Ad placeholder')

# Check container heights
print('\n6. Container sizing:')
if 'min-height' in content:
    print('   [OK] Has min-height')
else:
    print('   [WARNING] No min-height')
if 'aspect-ratio' in content:
    print('   [OK] Has aspect-ratio')
else:
    print('   [INFO] No aspect-ratio on main containers')

# Check images
print('\n7. Image optimization:')
img_count = content.count('<img')
lazy_count = content.count('loading="lazy"')
if img_count > 0:
    print(f'   Images: {img_count}, Lazy: {lazy_count}')
    if lazy_count == img_count:
        print('   [OK] All images lazy loaded')
    else:
        print('   [WARNING] Not all images lazy loaded')
else:
    print('   No images on this page')

# Check hero section
print('\n8. Hero section:')
if 'hero' in content.lower():
    hero_match = re.search(r'<section[^>]*class="[^"]*hero[^"]*"[^>]*>', content, re.I)
    if hero_match:
        print(f'   [FOUND] {hero_match.group(0)[:100]}')
        hero_content = content[hero_match.start():hero_match.start()+500]
        if 'min-height' in hero_content:
            print('   [OK] Hero has min-height')
        if 'height:' in hero_content:
            print('   [OK] Hero has explicit height')
