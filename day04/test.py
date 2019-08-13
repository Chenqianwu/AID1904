import requests

url = 'http://code.tarena.com.cn/AIDCode/aid1903/12-spider/spider_day04_note.zip'

res = requests.get(url)
print(res.text)