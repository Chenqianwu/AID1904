# 1. 打印程序执行时间
# 2. 随机的User-Agent,(确保每次发请求使用随机)
# 3. 数据爬下来后做处理(字符串),定义成字典
# 4. 一条龙: 获取 -> 调用解析 -> 数据处理

import requests
from lxml import etree
import time
import random

class MaoyanSpider(object):
    def __init__(self):
        self.url = 'https://maoyan.com/board/4?offset={}'
        self.ua_list = [
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1',
            'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0',
            'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)'
        ]
        # 用于记录页数
        self.page = 1

    # 获取
    def get_page(self,url):
        # 每次使用随机的user-agent
        headers = {'User-Agent':random.choice(self.ua_list)}
        html = requests.get(
            url=url,
            headers=headers
        ).content.decode('utf-8')

        # 直接调用解析函数
        self.parse_page(html)

    # 解析
    def parse_page(self,html):
        # 创建解析对象
        parse_html = etree.HTML(html)
        movie_dict = {}
        # 1.基准xpath: 匹配每个电影信息的节点对象
        dd_list = parse_html.xpath('//dl[@class="board-wrapper"]/dd')
        # 2.for依次遍历每个节点对象,获取信息
        for dd in dd_list:
            # 名称
            movie_dict['name'] = dd.xpath('./a/@title')[0].strip()
            # 主演
            movie_dict['star'] = dd.xpath('.//p[@class="star"]/text()')[0].strip()
            # 时间
            movie_dict['time'] = dd.xpath('.//p[@class="releasetime"]/text()')[0].strip()

            print(movie_dict)


    def main(self):
        for offset in range(0,31,10):
            url = self.url.format(offset)
            self.get_page(url)
            time.sleep(random.randint(1,3))
            print('第%d页爬取完成' % self.page)
            self.page += 1


if __name__ == '__main__':
    start = time.time()
    spider = MaoyanSpider()
    spider.main()
    end = time.time()
    print('执行时间: %.2f' % (end-start))












