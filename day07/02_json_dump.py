import json

app_info = {'应用名称':'呵呵列表','link':'http://hehe.com'}

# 把app_info存到xiaomi.json文件中
with open('xiaomi.json','a') as f:
    json.dump(app_info,f,ensure_ascii=False)