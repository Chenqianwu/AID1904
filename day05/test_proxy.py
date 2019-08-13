import requests

url = 'http://httpbin.org/get'
proxy = {
    'http':'http://182.34.33.207:9999',
    'https':'https://182.34.33.207:9999',
}

print(requests.get(url,proxies=proxy).text)