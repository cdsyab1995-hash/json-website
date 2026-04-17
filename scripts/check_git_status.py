import subprocess
import sys

git_path = r"C:\Users\Administrator\.workbuddy\binaries\git\cmd\git.exe"
repo_path = r"d:\网站开发-json"

# Check status
result = subprocess.run([git_path, "-C", repo_path, "status"], capture_output=True, text=True, encoding='utf-8', errors='ignore')
print("STATUS:")
print(result.stdout)
print(result.stderr)

# Check diff
result2 = subprocess.run([git_path, "-C", repo_path, "diff", "--stat"], capture_output=True, text=True, encoding='utf-8', errors='ignore')
print("\nDIFF:")
print(result2.stdout)
print(result2.stderr)

# Check what files changed
result3 = subprocess.run([git_path, "-C", repo_path, "status", "--porcelain"], capture_output=True, text=True, encoding='utf-8', errors='ignore')
print("\nPORCELAIN:")
print(result3.stdout or "No changes")
