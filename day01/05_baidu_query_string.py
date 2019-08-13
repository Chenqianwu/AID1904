# 请求模块
from urllib import request
# 编码模块
from urllib import parse

# 定义常用变量
word = input('请输入搜索内容:')
url = 'http://www.baidu.com/s?'
headers = {'User-Agent':'Mozilla/5.0'}

# 编码,拼接完整URL
# query_string: 'wd=%e8xxxx'
query_string = parse.urlencode({'wd':word})
url = url + query_string

# 三步走
req = request.Request(url=url,headers=headers)
res = request.urlopen(req)
html = res.read().decode('utf-8')

filename = '{}.html'.format(word)
with open(filename,'w',encoding='utf-8') as f:
    f.write(html)













