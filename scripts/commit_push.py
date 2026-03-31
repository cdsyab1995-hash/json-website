import subprocess

git = r"C:\Users\Administrator\.workbuddy\binaries\git\cmd\git.exe"
repo = r"d:\网站开发-json"

# Configure git user
subprocess.run([git, "-C", repo, "config", "--local", "user.name", "cdsyab1995"])
subprocess.run([git, "-C", repo, "config", "--local", "user.email", "cdsyab1995@users.noreply.github.com"])

# Add all files
subprocess.run([git, "-C", repo, "add", "-A"])

# Commit
result = subprocess.run([git, "-C", repo, "commit", "-m", "Improve accessibility: add link underlines, focus states, and aria-labels"], capture_output=True, text=True)
print("Commit result:")
print(result.stdout)
print(result.stderr)

# Push
result = subprocess.run([git, "-C", repo, "push", "origin", "main"], capture_output=True, text=True)
print("Push result:")
print(result.stdout)
print(result.stderr)
