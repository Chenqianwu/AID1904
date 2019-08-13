import requests

# 基准url地址
baseurl = 'http://tieba.baidu.com/f?'
# 查询参数
params = {
    'kw':'赵丽颖吧',
    'pn':'50'
}
# 请求头
headers = {'User-Agent':'Mozilla/5.0'}

res = requests.get(
    url = baseurl,
    params = params,
    headers = headers
)
print(res.content.decode('utf-8','ignore'))





















