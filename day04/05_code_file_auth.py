import requests
import os

url = 'http://code.tarena.com.cn/AIDCode/aid1903/12-spider/spider_day04_note.zip'
auth = ('tarenacode','code_2013')
headers = {'User-Agent':'Mozilla/5.0'}

# 1. 文件下载到本地，名字：　spider_day04_note.zip
html = requests.get(
    url = url,
    auth = auth,
    headers = headers
).content
filename = url.split('/')[-1]

# os模块
# 2. 把文件抓取到: /home/tarena/AIDCode/aid1903/12-spider/
directory = '/home/tarena/'+'/'.join(url.split('/')[3:-1])\
             +'/'
# 判断路径是否存在,不存在则创建
if not os.path.exists(directory):
    # 递归创建目录
    os.makedirs(directory)

# 下载文件
filename = directory + filename
print(filename)
with open(filename,'wb') as f:
    f.write(html)
    print('{}下载成功'.format(filename))






















