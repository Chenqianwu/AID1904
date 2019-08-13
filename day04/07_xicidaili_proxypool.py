import requests
from lxml import etree
from fake_useragent import UserAgent


# 获取User-Agent
def get_random_ua():
    # 1.创建User-Agent对象
    ua = UserAgent()

    return ua.random

url = 'https://www.xicidaili.com/nn/'

# 获取所有代理IP的地址和端口号
# [{'http':'http://xxxx:xx','https':'https://xxxx:xxx'},]
def get_ip_list():
    # 获取
    headers = { 'User-Agent' : get_random_ua() }
    proxies = {
        'http': 'http://182.35.81.10:9999',
        'https': 'https://182.35.81.10:9999'
    }
    html = requests.get(url,proxies=proxies,headers=headers).text
    # 解析
    parse_html = etree.HTML(html)
    # r_list: [<element tr at xxx>,<element tr at xxx>]
    r_list = parse_html.xpath('//tr')
    # 空列表,存放所有ip和port
    proxy_list = []
    # 依次遍历
    for r in r_list[1:]:
        ip = r.xpath('./td[2]/text()')[0]
        port = r.xpath('./td[3]/text()')[0]

        proxy_list.append(
            {
                'http':'http://{}:{}'.format(ip,port),
                'https':'https://{}:{}'.format(ip,port)
            }
        )
    # proxy_list: [{},{},{},{}]
    return proxy_list

# 测试代理,建立代理IP池
def proxy_pool():
    # 调用上面函数
    proxy_list = get_ip_list()
    # 可用代理IP列表
    useful_proxy = []
    # 测试代理是否可用
    for proxy in proxy_list:
        # proxy: {'http':'http://xxxx:xx'}
        headers = {'User-Agent':get_random_ua()}
        try:
            res = requests.get(
                url = 'http://httpbin.org/get',
                headers=headers,
                proxies = proxy,
                timeout = 5
            )
            print(res.text)
            useful_proxy.append(proxy)
            print(useful_proxy)
        except Exception as e:
            print('{}不能用'.format(proxy))
            continue


if __name__ == '__main__':
    proxy_pool()















