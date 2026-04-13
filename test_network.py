import os
import urllib.request

# 检查代理设置
proxy = os.environ.get('HTTP_PROXY') or os.environ.get('http_proxy')
https_proxy = os.environ.get('HTTPS_PROXY') or os.environ.get('https_proxy')
print(f'HTTP_PROXY: {proxy}')
print(f'HTTPS_PROXY: {https_proxy}')

# 测试HTTPS连接
try:
    response = urllib.request.urlopen('https://github.com', timeout=10)
    print('HTTPS Connection: SUCCESS')
except Exception as e:
    print(f'HTTPS Connection: FAILED')
    print(f'Error Type: {type(e).__name__}')
    print(f'Error Message: {str(e)}')
