# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    # 爬虫名: scrapy crawl 爬虫名
    name = 'baidu'
    # 允许爬取的域名
    allowed_domains = ['www.baidu.com']
    # 起始的URL地址
    start_urls = ['http://www.baidu.com/']

    # response为http://www.baidu.com/的响应对象
    def parse(self, response):
        # 真正解析提取数据的代码
        # [<Selector xpath='/html/head/title/text()' data='百度一下，你就知道'>]
        title = response.xpath('/html/head/title/text()').get()
        print('*'*50)
        print(title)
        print('*'*50)









