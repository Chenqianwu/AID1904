import requests
url = 'http://httpbin.org/get'
proxies = {
    'http': 'http://309435365:szayclhp@182.92.188.108:16816',
    'https':'https://309435365:szayclhp@182.92.188.108:16816',
}
headers = {
    'User-Agent' : 'Mozilla/5.0',
}

html = requests.get(url,proxies=proxies,headers=headers,timeout=5).text
print(html)