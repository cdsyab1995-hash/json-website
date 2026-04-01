import subprocess
import os

git_path = r"C:\Users\Administrator\.workbuddy\binaries\git\cmd\git.exe"
repo_path = r"d:\网站开发-json"
commit_msg = "新增SEO文章：中文版AI工作流+数字化转型，英文版WebAssembly趋势+AI API"

print(f"Git path: {git_path}")
print(f"Repo path: {repo_path}")
print(f"Exists: {os.path.exists(git_path)}")

# Add all files
print("\n--- Step 1: git add ---")
result = subprocess.run([git_path, "-C", repo_path, "add", "-A"], capture_output=True, text=True)
print(f"Exit code: {result.returncode}")
print(f"Stdout: {result.stdout}")
print(f"Stderr: {result.stderr}")

# Commit
print("\n--- Step 2: git commit ---")
result = subprocess.run([git_path, "-C", repo_path, "commit", "-m", commit_msg], capture_output=True, text=True)
print(f"Exit code: {result.returncode}")
print(f"Stdout: {result.stdout}")
print(f"Stderr: {result.stderr}")

# Push
print("\n--- Step 3: git push ---")
result = subprocess.run([git_path, "-C", repo_path, "push", "origin", "main"], capture_output=True, text=True)
print(f"Exit code: {result.returncode}")
print(f"Stdout: {result.stdout}")
print(f"Stderr: {result.stderr}")

print("\nDone!")
