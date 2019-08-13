import requests
from lxml import etree
import random
import time

class BaiduImageSpider(object):
    def __init__(self):
        self.headers = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)'}

    # 简化代码,url和xpath在变
    def get_parse_page(self,url,xpath):
        html = requests.get(
            url=url,
            headers=self.headers
        ).content.decode('utf-8')
        parse_html = etree.HTML(html)
        r_list = parse_html.xpath(xpath)

        return r_list


    # 获取帖子链接
    def get_tlink(self,url):

        xpath = '//*[@id="thread_list"]/li//div[@class="t_con cleafix"]/div/div/div/a/@href'
        t_list = self.get_parse_page(url,xpath)
        # 有的页面出现51个链接（最后１个链接不是帖子链接）
        if len(t_list) == 51:
            t_list = t_list[0:50]

        for t in t_list:
            t_link = 'http://tieba.baidu.com' + t
            # 把这1个帖子中所有图片保存到本地
            self.write_image(t_link)

    # 把1个帖子中所有图片保存到本地
    def write_image(self,t_link):

        # img_list: ['https://xxx.jpg','http://xxx.jpg']
        # 图片和视频链接（中间加　| )
        # 视频百度做了反爬,对响应内容做了处理,解决方法(查看网页源码,看结构)
        xpath = '//div[@class="d_post_content_main d_post_content_firstfloor"]//div[@class="d_post_content j_d_post_content  clearfix"]/img[@class="BDE_Image"]/@src | //div[@class="video_src_wrapper"]/embed/@data-video'
        img_list = self.get_parse_page(t_link,xpath)

        for img_link in img_list:
            html = requests.get(
                url=img_link,
                headers=self.headers
            ).content
            filename = img_link[-10:]
            with open(filename,'wb') as f:
                f.write(html)
                print('%s下载成功' % filename)
                time.sleep(random.randint(1,3))


if __name__ == '__main__':
    spider = BaiduImageSpider()
    spider.get_tlink('http://tieba.baidu.com/f?kw=%D5%D4%C0%F6%D3%B1&pn=0')

















