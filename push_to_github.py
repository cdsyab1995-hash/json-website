# -*- coding: utf-8 -*-
import subprocess
import os

def main():
    work_dir = r'd:\网站开发-json'
    message = 'Clean up: remove dead code'
    
    git = r'C:\Program Files\Git\cmd\git.exe'
    
    # Add all changes
    print('Adding changes...')
    subprocess.run([git, 'add', '-A'], cwd=work_dir)
    
    # Commit
    print(f'Committing: {message}')
    subprocess.run([git, 'commit', '-m', message], cwd=work_dir)
    
    # Push
    print('Pushing...')
    result = subprocess.run([git, 'push'], cwd=work_dir)
    
    if result.returncode == 0:
        print('Successfully pushed!')
    else:
        print('Push failed')

if __name__ == '__main__':
    main()
