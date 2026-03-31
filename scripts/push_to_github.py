import subprocess
import os

git_path = r"C:\Users\Administrator\.workbuddy\binaries\git\cmd\git.exe"
repo_path = r"d:\网站开发-json"

# Configure git user
subprocess.run([git_path, "-C", repo_path, "config", "--local", "user.name", "cdsyab1995"])
subprocess.run([git_path, "-C", repo_path, "config", "--local", "user.email", "cdsyab1995@users.noreply.github.com"])

# Add all files
subprocess.run([git_path, "-C", repo_path, "add", "-A"])

# Commit
result = subprocess.run([git_path, "-C", repo_path, "commit", "-m", "Improve accessibility: add link underlines, focus states, and aria-labels"], capture_output=True, text=True)
print(result.stdout)
print(result.stderr)

# Push
result = subprocess.run([git_path, "-C", repo_path, "push", "origin", "main"], capture_output=True, text=True)
print(result.stdout)
print(result.stderr)
