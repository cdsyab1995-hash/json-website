#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Complete Git Setup and Push Script"""

import subprocess
import os

GIT_BIN = r"C:\Users\Administrator\.workbuddy\binaries\git\cmd\git.exe"
REPO_PATH = r"d:\网站开发-json"
REMOTE_URL = "git@github.com:cdsyab1995-hash/json-website.git"

def run(cmd, cwd=None, env=None):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=cwd, env=env)
    return result.returncode, result.stdout, result.stderr

def git(*args, cwd=REPO_PATH):
    cmd = [GIT_BIN] + list(args)
    return run(cmd, cwd=cwd)

def main():
    print("=" * 60)
    print("GitHub Setup and Push Script")
    print("=" * 60)

    # 1. 检查Git版本
    print("\n[1/6] Checking Git...")
    code, out, err = git("--version")
    if code == 0:
        print(f"  OK: {out.strip()}")
    else:
        print(f"  ERROR: {err}")
        return

    # 2. 配置Git用户
    print("\n[2/6] Configuring Git user...")
    git("config", "--local", "user.name", "cdsyab1995")
    git("config", "--local", "user.email", "cdsyab1995@users.noreply.github.com")
    git("config", "--local", "core.autocrlf", "false")
    git("config", "--local", "core.longpaths", "true")
    print("  OK: User configured")

    # 3. 检查或初始化仓库
    print("\n[3/6] Checking repository...")
    code, _, _ = git("rev-parse", "--git-dir")
    if code != 0:
        print("  Initializing new repository...")
        git("init")
        print("  OK: Repository initialized")
    else:
        print("  OK: Repository exists")

    # 4. 添加远程仓库
    print("\n[4/6] Setting up remote...")
    code, out, _ = git("remote", "-v")
    if "origin" in out:
        print("  OK: Remote already exists")
    else:
        git("remote", "add", "origin", REMOTE_URL)
        print("  OK: Remote added")

    # 5. 添加文件并提交
    print("\n[5/6] Committing files...")
    git("add", "-A")
    code, out, err = git("commit", "-m", "Fix navbar and optimize title for SEO")
    if "nothing to commit" in out.lower():
        print("  OK: Nothing to commit (already up to date)")
    else:
        print("  OK: Files committed")
        print(f"  {out[:200]}")

    # 6. 推送到GitHub
    print("\n[6/6] Pushing to GitHub...")
    print("  (Using SSH key authentication)")
    code, out, err = git("push", "-u", "origin", "main", "--force")
    if code == 0:
        print("\n" + "=" * 60)
        print("SUCCESS! Code pushed to GitHub!")
        print("=" * 60)
        print("\nWebsite will update in 1-2 minutes")
        print("URL: https://cdsyab1995-hash.github.io/json-website/")
        print("=" * 60)
    else:
        print(f"  ERROR: {err[:500]}")
        print("\nNOTE: If you see 'Permission denied', please:")
        print("1. Go to GitHub -> Settings -> SSH Keys")
        print("2. Add your SSH public key")
        print("   (File: C:\\Users\\Administrator\\.ssh\\id_ed25519.pub)")

if __name__ == "__main__":
    main()
