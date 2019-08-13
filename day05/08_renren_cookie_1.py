import requests
from lxml import etree

# 个人主页: 需要登录才能访问的页面
url = 'http://www.renren.com/970294164/profile'
# headers: 登录成功后抓取到的
# headers: Cookie Referer User-Agent
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Cookie": "anonymid=jyh1eu2i-cyz4t3; depovince=GW; _r01_=1; JSESSIONID=abcIfzm7XnmzL9Lr-rJWw; ick_login=32e5f56c-3e0d-45e5-b32b-6ae7b75b28d4; first_login_flag=1; ln_uact=15110225726; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; jebe_key=0290509b-c7d2-4f23-b8d5-f1d8d5c3b041%7C3317b1face1adcda7e34f17db4558a85%7C1563960241750%7C1%7C1563960243395; jebe_key=0290509b-c7d2-4f23-b8d5-f1d8d5c3b041%7C3317b1face1adcda7e34f17db4558a85%7C1563960241750%7C1%7C1563960243399; wp_fold=0; jebecookies=0187e4c8-6b7b-42b9-89c0-541d1b155188|||||; _de=5411E55883CC3142BC1347536B8CB062; p=10e3b6ffa09e867a161342d10cdcb44e4; t=1a806af66471637b44e420e4a20c2ce14; societyguester=1a806af66471637b44e420e4a20c2ce14; id=970294164; xnsid=dcaed6e4; ver=7.0; loginfrom=null; td_cookie=18446744071215120067",
    "Host": "www.renren.com",
    "Referer": "http://www.renren.com/",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
}

html = requests.get(url=url,headers=headers).text

parse_html = etree.HTML(html)
r_list = parse_html.xpath('//*[@id="operate_area"]/div[1]/ul/li[1]/span/text()')
print(r_list)

















