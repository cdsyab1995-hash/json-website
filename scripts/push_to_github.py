# -*- coding: utf-8 -*-
"""Git push script"""
import subprocess
import os

def main():
    work_dir = r'd:\网站开发-json'
    git = r'C:\Program Files\Git\cmd\git.exe'
    
    # Pull first
    print('Pulling remote changes...')
    subprocess.run([git, 'pull', 'origin', 'main'], cwd=work_dir)
    
    # Add all changes
    print('Adding changes...')
    subprocess.run([git, 'add', '-A'], cwd=work_dir)
    
    # Commit
    print('Committing...')
    subprocess.run([git, 'commit', '-m', 'Update aijsons.com'], cwd=work_dir)
    
    # Push
    print('Pushing...')
    result = subprocess.run([git, 'push'], cwd=work_dir)
    
    if result.returncode == 0:
        print('Successfully pushed!')
    else:
        print('Push failed')

if __name__ == '__main__':
    main()
