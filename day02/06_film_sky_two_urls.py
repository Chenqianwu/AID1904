from urllib import request
import re
import time
import random
from useragents import *
import pymysql

class FilmSky(object):
    def __init__(self):
        self.url = 'https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html'
        # 定义两个对象
        self.db = pymysql.connect(
            '127.0.0.1','root','123456','maoyandb',charset='utf8'
        )
        self.cursor = self.db.cursor()

    # 获取html函数(因为两个页面都需要发请求)
    def get_page(self,url):
        req = request.Request(
            url=url,
            headers={'User-Agent':random.choice(ua_list)}
        )
        res = request.urlopen(req)
        # ignore参数,实在处理不了的编码错误忽略
        # 查看网页源码,发现网页编码为 gb2312,不是 utf-8
        html = res.read().decode('gbk','ignore')

        return html

    # 解析提取数据(把名称和下载链接一次性拿到)
    # html为一级页面响应内容
    def parse_page(self,html):
        # 1. 先解析一级页面(电影名称 和 详情链接)
        pattern = re.compile('<table width="100%".*?<td height="26">.*?<a href="(.*?)".*?>(.*?)</a>',re.S)
        # film_list: [('详情链接','名称'),()]
        film_list = pattern.findall(html)
        # print(film_list)
        ins = 'insert into filmsky values(%s,%s)'
        for film in film_list:
            film_name = film[1]
            film_link = 'https://www.dytt8.net' + film[0]
            # 2. 拿到详情链接后,再去获取详情链接html,提取下载链接
            download_link = self.parse_two_html(film_link)

            self.cursor.execute(ins,[film_name,film_link])
            self.db.commit()

            # 打印测试
            d = {
                '电影名称':film_name,
                '下载链接':download_link
            }
            print(d)

    # 解析二级页面,获取下载链接
    def parse_two_html(self,film_link):
        two_html = self.get_page(film_link)
        pattern = re.compile('<td style="WORD-WRAP.*?>.*?>(.*?)</a>',re.S)
        download_link = pattern.findall(two_html)[0]

        return download_link


    # 主函数
    def main(self):
        for page in range(1,11):
            url = self.url.format(page)
            html = self.get_page(url)
            self.parse_page(html)
            time.sleep(random.randint(1,3))
            print('第%d页完成' % page)


if __name__ == '__main__':
    start = time.time()
    spider = FilmSky()
    spider.main()
    end = time.time()
    print('执行时间:%.2f' % (end-start))


















