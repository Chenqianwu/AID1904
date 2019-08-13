import requests
import time
from multiprocessing import Process
from queue import Queue
import json

class XiaomiSpider(object):
    def __init__(self):
        self.url = 'http://app.mi.com/categotyAllListApi?page={}&categoryId=2&pageSize=30'
        self.headers = {'User-Agent':'Mozilla/5.0'}
        # url队列
        self.url_queue = Queue()
        self.n = 0

    # URL入队列
    def url_in(self):
        for i in range(67):
            url = self.url.format(i)
            # 入队列
            self.url_queue.put(url)

    # 线程事件函数
    def get_data(self):
        while True:
            # self.url_queue.empty() 为True,队列为空
            if self.url_queue.empty():
                break

            # get地址,请求+解析+保存
            url = self.url_queue.get()
            html = requests.get(
                url = url,
                headers = self.headers,
            ).content.decode('utf-8')
            html = json.loads(html)
            # 解析数据: html['data'] -> [{},{},{}]
            with open('xiaomi.json','a') as f:
                app_dict = {}
                for app in html['data']:
                    # 应用名称
                    app_dict['app_name'] = app['displayName']
                    # 应用链接
                    app_dict['app_link'] = 'http://app.mi.com/details?id=' \
                                    + app['packageName']
                    json.dump(app_dict,f,ensure_ascii=False)


    # 主函数
    def main(self):
        # url入队列
        self.url_in()
        # 创建多线程
        t_list = []
        for i in range(5):
            t = Process(target=self.get_data)
            t_list.append(t)
            t.start()

        for i in t_list:
            i.join()

        print('应用数量:',self.n)

if __name__ == '__main__':
    start = time.time()
    spider = XiaomiSpider()
    spider.main()
    end = time.time()
    print('执行时间:%.2f' % (end-start))


































