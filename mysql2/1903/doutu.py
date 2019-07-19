import requests
import re

#获取图片列表
def getImagesList():
    # 获取斗图网源代码
    html=requests.get('http://www.doutula.com/photo/list/?page=3').text
    # print(html)
    """
 data-original="http://img.doutula.com/production/uploads/image//2019/07/03/20190703106840_CltuGQ.jpg" alt="鸭鸭发呆" 
    """
    #正则表达式 .*? 通配符匹配所有
    reg=r'data-original="(.*?)".*?alt="(.*?)"'
getImagesList()