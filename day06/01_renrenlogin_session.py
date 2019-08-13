import requests

# 定义常用变量　
post_url = 'http://www.renren.com/PLogin.do'
get_url = 'http://www.renren.com/970294164/profile'
post_data = {
    'email':'15110225726',
    'password':''
}
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'Referer' : 'http://www.renren.com/'
}

# 实例化session对象
session = requests.session()
# 先POST -> form-action
session.post(url=post_url,data=post_data,headers=headers)
# 再GET -> 个人主页(需要登录才能访问的页面)
html = session.get(url=get_url,headers=headers).text

print(html)















