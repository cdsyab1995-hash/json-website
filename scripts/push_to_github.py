import subprocess
import sys

git_path = r"C:\Users\Administrator\.workbuddy\binaries\git\cmd\git.exe"
python_path = r"C:\Users\Administrator\.workbuddy\binaries\python\versions\3.13.12\python.exe"
repo_path = r"d:\网站开发-json"

commit_msg = sys.argv[1] if len(sys.argv) > 1 else "Update: code improvements"

# Configure git user
subprocess.run([git_path, "-C", repo_path, "config", "--local", "user.name", "cdsyab1995"], stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
subprocess.run([git_path, "-C", repo_path, "config", "--local", "user.email", "cdsyab1995@users.noreply.github.com"], stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)

# Add all files
result = subprocess.run([git_path, "-C", repo_path, "add", "-A"], capture_output=True, text=True, encoding='utf-8', errors='ignore')
print("[OK] Files added")

# Commit
result = subprocess.run([git_path, "-C", repo_path, "commit", "-m", commit_msg], capture_output=True, text=True, encoding='utf-8', errors='ignore')
if result.returncode == 0:
    print(f"[OK] Committed: {commit_msg}")
else:
    print("Nothing to commit" if "nothing to commit" in result.stderr.lower() else result.stderr)

# Push
result = subprocess.run([git_path, "-C", repo_path, "push", "origin", "main"], capture_output=True, text=True, encoding='utf-8', errors='ignore')
if result.returncode == 0:
    print("[OK] Pushed to GitHub!")
else:
    print(f"Push failed: {result.stderr}")
