#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Get CSS from git and properly decode it
"""
import subprocess
import os

GIT = r"C:\Users\Administrator\.workbuddy\binaries\git\cmd\git.exe"
REPO = r"d:\网站开发-json"

def main():
    # Get raw hash of css/styles.css from commit 8b82662
    result = subprocess.run(
        [GIT, "-C", REPO, "ls-tree", "8b82662", "css/styles.css"],
        capture_output=True, encoding="utf-8"
    )
    print("ls-tree:", result.stdout.strip())
    
    # Also check current git objects
    result2 = subprocess.run(
        [GIT, "-C", REPO, "ls-tree", "HEAD", "css/styles.css"],
        capture_output=True, encoding="utf-8"
    )
    print("HEAD css:", result2.stdout.strip())
    
    # Get raw content using git cat-file -p blob hash
    # Parse hash from ls-tree output
    line = result.stdout.strip()
    if line:
        parts = line.split()
        blob_hash = parts[2] if len(parts) >= 3 else None
        print(f"Blob hash: {blob_hash}")
        
        if blob_hash:
            result3 = subprocess.run(
                [GIT, "-C", REPO, "cat-file", "-p", blob_hash],
                capture_output=True
            )
            raw = result3.stdout
            print(f"Raw size: {len(raw)} bytes")
            print(f"First 20 bytes hex: {raw[:20].hex()}")
            
            # Check if it's a valid UTF-8 CSS
            if raw[:2] == b'/*' or raw[:3] == b'\xef\xbb\xbf':
                print("Looks valid!")
                # Strip UTF-8 BOM if present
                if raw[:3] == b'\xef\xbb\xbf':
                    raw = raw[3:]
                    print("Stripped UTF-8 BOM")
                text = raw.decode('utf-8')
            else:
                # Try to find '/*' which should be the CSS comment start
                idx = raw.find(b'/*')
                print(f"'/*' starts at byte: {idx}")
                if idx > 0:
                    useful = raw[idx:]
                    print(f"Content from '/*': {len(useful)} bytes")
                    text = useful.decode('utf-8', errors='replace')
                else:
                    text = raw.decode('utf-8', errors='replace')
            
            lines = text.split('\n')
            print(f"Lines: {len(lines)}")
            print(f"First real line: {repr(lines[0][:100])}")
            
            # Save
            out = os.path.join(REPO, "css", "styles_clean.css")
            with open(out, "w", encoding="utf-8", newline="\n") as f:
                f.write(text)
            print(f"Saved to: {out}")

if __name__ == "__main__":
    main()
