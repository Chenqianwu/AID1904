import requests
from lxml import etree

url = 'http://www.mca.gov.cn/article/sj/xzqh/2019/'
headers = {'User-Agent':'Mozilla/5.0'}

html = requests.get(url=url,headers=headers).text
parse_html = etree.HTML(html)
link = 'http://www.mca.gov.cn' + parse_html.xpath('//a[@class="artitlelist"]/@href')[1]

two_html = requests.get(link,headers=headers).text
print(two_html)






