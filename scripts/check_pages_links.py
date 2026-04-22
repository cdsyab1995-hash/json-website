#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import sys
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BASE = Path('d:/网站开发-json')
for fname in ['cookie.html', 'privacy.html', 'terms.html']:
    f = BASE / fname
    text = f.read_text(encoding='utf-8')
    links = re.findall('href="([^"]+)"', text)
    bad = [l for l in links if 'pages/' in l and not l.startswith('http')]
    print(f'{fname}: pages/ links = {bad[:5]}')
