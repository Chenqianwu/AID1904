import requests

url = 'http://httpbin.org/get'
headers = {'User-Agent':'Mozilla/5.0'}
# 定义代理
proxies = {
    'http':'http://85.234.126.107:55555',
    'https':'https://85.234.126.107:55555'
}

html = requests.get(
    url = url,
    proxies = proxies,
    headers = headers,
    timeout = 5
).text

print(html)
















