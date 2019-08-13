import requests

# url = 'http://httpbin.org/get'
url = 'http://www.baidu.com/'
headers = {'User-Agent':'xxxxxxxxxxxxxxxxx'}

res = requests.get(url,headers=headers)
# 查看响应字符编码
res.encoding = 'utf-8'
# 查看响应内容(字符串)
print(res.text)
# 查看响应内容(bytes)
print(res.content)
# 查看HTTP响应码
print(res.status_code)
# 返回实际数据的URL地址
print(res.url)


























