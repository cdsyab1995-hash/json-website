import subprocess
import os

os.chdir(r'd:\网站开发-json\awesome-json-tools')

# Initialize git if not already
subprocess.run(['git', 'init'], check=True, capture_output=True)
subprocess.run(['git', 'add', '.'], check=True, capture_output=True)
subprocess.run(['git', 'commit', '-m', 'Initial commit: Add awesome-json-tools README'], check=True, capture_output=True)
subprocess.run(['git', 'remote', 'add', 'origin', 'git@github.com:cdsyab1995-hash/awesome-json-tools.git'], check=True, capture_output=True)
subprocess.run(['git', 'branch', '-M', 'main'], check=True, capture_output=True)
subprocess.run(['git', 'push', '-u', 'origin', 'main'], check=True, capture_output=True)

print('Push completed!')
