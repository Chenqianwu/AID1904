# 1. 打印程序执行时间
# 2. 随机的User-Agent,(确保每次发请求使用随机)
# 3. 数据爬下来后做处理(字符串),定义成字典
# 4. 一条龙: 获取 -> 调用解析 -> 数据处理

from urllib import request
import time
import re
import csv
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

    # # 保存,打印输出
    # def write_page(self,r_list):
    #     one_film_dict = {}
    #     for rt in r_list:
    #         one_film_dict['name'] = rt[0].strip()
    #         one_film_dict['star'] = rt[1].strip()
    #         one_film_dict['time'] = rt[2].strip()[5:15]
    #
    #         print(one_film_dict)

    # # 保存到csv文件(writerow)
    # def write_page(self,r_list):
    #     # 打开文件要在for循环之前,否则会打开很多次文件
    #     with open('maoyan.csv','a') as f:
    #         for rt in r_list:
    #             writer = csv.writer(f)
    #             writer.writerow(
    #                 [rt[0],rt[1].strip(),rt[2].strip()[5:15]]
    #             )

    # 保存到csv文件(writerows) -- 推荐使用此方法
    def write_page(self,r_list):
        # 空列表,最终writerows()的参数: [(),(),()]
        film_list = []
        with open('maoyan.csv','a') as f:
            writer = csv.writer(f)
            for rt in r_list:
                # 把处理过的数据定义成元组
                t = (rt[0],rt[1].strip(),rt[2].strip()[5:15])
                film_list.append(t)

            # 和for循环平级
            writer.writerows(film_list)


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












