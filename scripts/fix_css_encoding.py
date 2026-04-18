#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Convert styles.css from UTF-16 LE to UTF-8
"""
import subprocess
import os

GIT = r"C:\Users\Administrator\.workbuddy\binaries\git\cmd\git.exe"
REPO = r"d:\网站开发-json"

def main():
    # Get the latest clean version (8b82662 has the best content)
    result = subprocess.run(
        [GIT, "-C", REPO, "show", "8b82662:css/styles.css"],
        capture_output=True
    )
    data = result.stdout
    print(f"Raw bytes: {len(data)}, BOM: {data[:4].hex()}")
    
    # Try various encodings
    text = None
    for enc in ["utf-8-sig", "utf-8", "utf-16", "latin-1", "cp1252"]:
        try:
            text = data.decode(enc)
            print(f"Decoded with {enc}: {len(text)} chars, {text.count(chr(10))} lines")
            print(f"First 100 chars: {repr(text[:100])}")
            break
        except Exception as e:
            print(f"{enc} failed: {e}")
    
    if text is None:
        print("All decodings failed")
        return
    
    # Write as UTF-8 (no BOM)
    out = os.path.join(REPO, "css", "styles.css")
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    
    print(f"Saved UTF-8 version to: {out}")
    
    # Verify
    with open(out, "rb") as f:
        check = f.read(10)
    print(f"Verification - first bytes: {check.hex()}")
    print(f"Expected: starts with '/*' = {check[:2] == b'/*'}")

if __name__ == "__main__":
    main()
