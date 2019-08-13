from getip import *
import requests
import random

url = 'http://httpbin.org/get'
headers = {'User-Agent':'Mozilla/5.0'}
# 获取代理IP,并随机取出1个
proxy_ip_list = get_ip_list()

# 函数功能: 给你一个url,死活也要爬下来
def get_page(url):
    while True:
        # 如果列表为空了,需要重新获取开放代理IP
        if not proxy_ip_list:
            proxy_ip_list = get_ip_list()

        ip_port = random.choice(proxy_ip_list)
        # 定义代理proxies
        proxies = {
            'http':'http://{}'.format(ip_port),
            'https':'https://{}'.format(ip_port)
        }
        try:
            html = requests.get(
                url = url,
                proxies = proxies,
                headers = headers,
                timeout = 5
            ).text
            print(html)
            break
        except Exception as e:
            proxy_ip_list.remove(ip_port)
            continue


get_page(url)

























