import requests
from lxml import etree

class NoteSpider(object):
    def __init__(self):
        self.url = 'http://code.tarena.com.cn/'
        self.headers = {'User-Agent':'Mozilla/5.0'}
        # 定义web客户端验证参数auth
        self.auth = ('tarenacode','code_2013')

    # 获取+解析
    def get_code(self):
        # 获取响应内容
        html = requests.get(
            url = self.url,
            auth = self.auth,
            headers = self.headers
        ).content.decode('utf-8')
        # 解析提取数据
        parse_html = etree.HTML(html)
        r_list = parse_html.xpath('//a/@href')
        # rlist: ['../','AIDCode/']
        for r in r_list:
            if r != '../':
                print(r)

if __name__ == '__main__':
    spider = NoteSpider()
    spider.get_code()







