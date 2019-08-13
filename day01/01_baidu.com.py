# 导入请求模块(python标准库模块)
import urllib.request

# url = 'http://www.baidu.com/'
url = 'http://httpbin.org/get'

# 向百度发请求,得到响应对象
response = urllib.request.urlopen(url)
# 获取响应对象内容(网页源代码)
# read() -> bytes
# decode() -> string
print(response.read().decode('utf-8'))

# 返回http响应码
# print(response.getcode())
# 返回实际数据URL地址
# print(response.geturl())










