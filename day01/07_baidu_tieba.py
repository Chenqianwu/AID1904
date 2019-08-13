from urllib import request,parse
import time
import random

class BaiduSpider(object):
    def __init__(self):
        self.url = 'http://tieba.baidu.com/f?kw={}&pn={}'
        self.headers = {'User-Agent':'Mozilla/5.0'}

    # 获取响应
    def get_page(self,url):
        req = request.Request(url=url,headers=self.headers)
        res = request.urlopen(req)
        html = res.read().decode('utf-8')

        return html

    # 提取数据
    def parse_page(self,html):
        pass

    # 保存数据
    def write_page(self,filename,html):
        with open(filename,'w') as f:
            f.write(html)

    # 主函数
    def main(self):
        name = input('请输入贴吧名:')
        start = int(input('请输入起始页:'))
        end = int(input('请输入终止页:'))

        # 拼接URL地址,发请求
        for page in range(start,end+1):
            pn = (page-1)*50
            kw = parse.quote(name)
            url = self.url.format(kw,pn)
            # 获取响应,并保存
            html = self.get_page(url)
            filename = '{}-第{}页.html'.format(name,page)
            self.write_page(filename,html)
            # 提示
            print('第{}页爬取成功'.format(page))
            # 控制爬取速度
            time.sleep(random.randint(1,3))

if __name__ == '__main__':
    spider = BaiduSpider()
    spider.main()





















