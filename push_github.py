import requests
import base64
import os

TOKEN = "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"
REPO = "cdsyab1995-hash/awesome-json-tools"
BASE_URL = f"https://api.github.com/repos/{REPO}"

HEADERS = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def upload_file(path, content):
    """Upload a file to GitHub"""
    url = f"{BASE_URL}/contents/{path}"
    
    # Encode content to base64
    content_bytes = content.encode('utf-8')
    content_b64 = base64.b64encode(content_bytes).decode('utf-8')
    
    # Check if file exists
    response = requests.get(url, headers=HEADERS)
    sha = None
    if response.status_code == 200:
        sha = response.json().get('sha')
    
    # Upload file
    data = {
        "message": f"Add {path}",
        "content": content_b64
    }
    if sha:
        data["sha"] = sha
    
    response = requests.put(url, headers=HEADERS, json=data)
    
    if response.status_code in [200, 201]:
        print(f"[OK] {path} uploaded successfully")
        return True
    else:
        print(f"[FAIL] {path} failed: {response.status_code} - {response.text}")
        return False

# Read files
repo_path = r"d:\网站开发-json\awesome-json-tools"

files = {
    "README.md": open(os.path.join(repo_path, "README.md"), "r", encoding="utf-8").read(),
    "CONTRIBUTING.md": open(os.path.join(repo_path, "CONTRIBUTING.md"), "r", encoding="utf-8").read(),
    "LICENSE": open(os.path.join(repo_path, "LICENSE"), "r", encoding="utf-8").read(),
}

# Upload files
print("Uploading awesome-json-tools to GitHub...")
for filename, content in files.items():
    upload_file(filename, content)

print("\nDone!")
