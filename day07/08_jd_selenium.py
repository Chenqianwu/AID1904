from selenium import webdriver
import time

class JdSpider(object):
    def __init__(self):
        self.browser = webdriver.Chrome()
        self.url = 'https://www.jd.com/'
        self.i = 0

    # 获取商品页面
    def get_page(self):
        # 打开京东
        self.browser.get(self.url)
        # 找两个节点
        self.browser.find_element_by_xpath('//*[@id="key"]').send_keys('爬虫书籍')
        self.browser.find_element_by_xpath('//*[@id="search"]/div/div[2]/button').click()
        # 留出时间给页面加载
        time.sleep(2)

    # 解析页面
    def parse_page(self):
        # 把进度条拉到最下面
        self.browser.execute_script(
            'window.scrollTo(0,document.body.scrollHeight)'
        )
        time.sleep(3)

        # 匹配所有商品节点对象列表
        li_list = self.browser.find_elements_by_xpath('//*[@id="J_goodsList"]/ul/li')
        for li in li_list:
            info = li.text.split('\n')
            if info[0].startswith('每满'):
                price = info[1]
                name = info[2]
                number = info[3]
                market = info[4]
            elif info[0] == '单件':
                price = info[3]
                name = info[4]
                number = info[5]
                market = info[6]
            elif info[0].startswith('￥') and info[1].startswith('￥'):
                price = info[0]
                name = info[2]
                number = info[3]
                market = info[4]
            else:
                price = info[0]
                name = info[1]
                number = info[2]
                market = info[3]

            print(price,number,market,name)
            self.i += 1

    def main(self):
        self.get_page()
        while True:
            self.parse_page()
            # 判断是否为最后1页
            # 不是最后1页,点击下一页
            if self.browser.page_source.find('pn-next disabled') == -1:
                # 不是最后1页,找到下一页按钮
                self.browser.find_element_by_class_name('pn-next').click()
                time.sleep(3)
            else:
                break
        print(self.i)



if __name__ == '__main__':
    spider = JdSpider()
    spider.main()















