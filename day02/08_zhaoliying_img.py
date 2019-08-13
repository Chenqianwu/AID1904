import requests

url = 'http://dingyue.nosdn.127.net/lL1JH2YdpAWrzEhfp8BrJ8lTHa1602AEX9E7qpTpH5NzW1535203788506compressflag.jpg'
headers = {'User-Agent':'Mozilla/5.0'}

html = requests.get(url,headers=headers).content

# 把图片保存到本地
with open('赵丽颖.jpg','wb') as f:
    f.write(html)












