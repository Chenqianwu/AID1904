'''包装请求头,向httbin.org发请求'''
from urllib import request

# 定义常用变量
url = 'http://httpbin.org/get'
headers = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)'}

# 创建请求对象(包装请求) - Request
req = request.Request(url=url,headers=headers)
# 发请求,获取响应对象 - urlopen
res = request.urlopen(req)
# 读取内容 - read.....
html = res.read().decode('utf-8')

print(html)















