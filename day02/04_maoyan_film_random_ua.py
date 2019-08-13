# 1. 打印程序执行时间
# 2. 随机的User-Agent,(确保每次发请求使用随机)
# 3. 数据爬下来后做处理(字符串),定义成字典
# 4. 一条龙: 获取 -> 调用解析 -> 数据处理

from urllib import request
import time
import re
import csv
import random
# 导入自己定义的useragents.py中的ua_list
from useragents import ua_list

class MaoyanSpider(object):
    def __init__(self):
        self.url = 'https://maoyan.com/board/4?offset={}'

    # 获取
    def get_page(self,url):
        # 每次使用随机的user-agent
        headers = {'User-Agent':random.choice(ua_list)}
        req = request.Request(
            url=url,
            headers=headers
        )
        res = request.urlopen(req)
        html = res.read().decode('utf-8')
        # 直接调用解析函数
        self.parse_page(html)

    # 解析
    def parse_page(self,html):
        pattren = re.compile('<div class="movie-item-info">.*?title="(.*?)".*?class="star">(.*?)</p>.*?releasetime">(.*?)</p>',re.S)
        # rlist: [('霸王别姬','张国荣','1993'),(),()]
        r_list = pattren.findall(html)
        self.write_page(r_list)

    # 保存
    def write_page(self,r_list):
        one_film_dict = {}
        for rt in r_list:
            one_film_dict['name'] = rt[0].strip()
            one_film_dict['star'] = rt[1].strip()
            one_film_dict['time'] = rt[2].strip()[5:15]

            print(one_film_dict)

    def main(self):
        for offset in range(0,31,10):
            url = self.url.format(offset)
            self.get_page(url)
            time.sleep(random.randint(1,3))


if __name__ == '__main__':
    start = time.time()
    spider = MaoyanSpider()
    spider.main()
    end = time.time()
    print('执行时间: %.2f' % (end-start))












