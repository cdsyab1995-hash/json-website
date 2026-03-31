import subprocess

git = r"C:\Users\Administrator\.workbuddy\binaries\git\cmd\git.exe"
repo = r"d:\网站开发-json"

result = subprocess.run([git, "-C", repo, "status"], capture_output=True, text=True)
print("STDOUT:", result.stdout)
print("STDERR:", result.stderr)
print("Return code:", result.returncode)
