import requests
from lxml import etree
import time
import random

class LianjiaSpider(object):
  def __init__(self):
    self.url = 'https://bj.lianjia.com/ershoufang/pg{}/'
    self.headers = {'User-Agent':'Mozilla/5.0'}

  def get_page(self,url):
    res = requests.get(url,headers=self.headers)
    res.encoding = 'utf-8'
    html = res.text
    # 调用解析函数
    self.parse_page(html)

  def parse_page(self,html):
    # 创建解析对象
    parse_html = etree.HTML(html)
    # 基准xpath
    li_list = parse_html.xpath('//ul[@class="sellListContent"]/li[@class="clear LOGCLICKDATA"] | //ul[@class="sellListContent"]/li[@class="clear LOGVIEWDATA LOGCLICKDATA"]')
    house_dict = {}
    # 依次遍历
    for li in li_list:
        # 名称
        house_dict['house_name'] = li.xpath('.//a[@data-el="region"]/text()')[0].strip()
        # 总价
        total_price = li.xpath('.//div[@class="totalPrice"]/span/text()')[0].strip()
        total_price = float(total_price) * 10000
        house_dict['total_price'] = total_price
        # 单价
        house_dict['unit_price'] = li.xpath('.//div[@class="unitPrice"]/@data-price')[0].strip()

        print(house_dict)

  def main(self):
    for pg in range(1,5):
        url = self.url.format(pg)
        self.get_page(url)
        time.sleep(random.uniform(0,2))

if __name__ == '__main__':
  start = time.time()
  spider = LianjiaSpider()
  spider.main()
  end = time.time()
  print('执行时间:%.2f' % (end-start))