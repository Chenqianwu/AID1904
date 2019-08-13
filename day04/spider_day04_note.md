# **Day03回顾**

## **目前反爬总结**

- 基于User-Agent反爬

```python
1、发送请求携带请求头: headers={'User-Agent' : 'Mozilla/5.0 xxxxxx'}
2、多个请求随机切换User-Agent
   1、定义列表存放大量User-Agent，使用random.choice()每次随机选择
   2、定义py文件存放大量User-Agent，使用random.choice()每次随机选择
   3、使用fake_useragent每次访问随机生成User-Agent
      # sudo pip3 install fake_useragent
      * from fake_useragent import UserAgent
      * ua = UserAgent()
      * user_agent = ua.random
      * print(user_agent)
```

- 响应内容前端做处理反爬

```python
1、html页面中可匹配出内容，程序中匹配结果为空
   * 响应内容中嵌入js，对页面结构做了一定调整导致，通过查看网页源代码，格式化输出查看结构，更改xpath或者正则测试
2、如果数据出不来可考虑更换 IE 的User-Agent尝试，数据返回最标准
```

- 基于IP反爬

```python
1、控制爬取速度，每爬取页面后随机休眠一定时间，再继续爬取下一个页面
2、代理IP
```

## **请求模块总结**

- urllib库使用流程

```python
# 编码
params = {
    '':'',
    '':''
}
params = urllib.parse.urlencode(params)
url = baseurl + params

# 请求
request = urllib.request.Request(url,headers=headers)
response = urllib.request.urlopen(request)
html = response.read().decode('utf-8')
```

- requests模块使用流程

```python
url = baseurl + urllib.parse.urlencode({dict})
html = requests.get(url,headers=headers).text
```

## **解析模块总结**

- 正则解析re模块

```python
import re 

pattern = re.compile('正则表达式',re.S)
r_list = pattern.findall(html)
```

- lxml解析库

```python
from lxml import etree

parse_html = etree.HTML(res.text)
r_list = parse_html.xpath('xpath表达式')
```

## **xpath表达式**

- 匹配规则

```python
1、节点对象列表
   # xpath示例: //div、//div[@class="student"]、//div/a[@title="stu"]/span
2、字符串列表
   # xpath表达式中末尾为: @src、@href、text()
```

- xpath高级

```python
1、基准xpath表达式: 得到节点对象列表
2、for r in [节点对象列表]:
       username = r.xpath('./xxxxxx')  
       # 此处注意遍历后继续xpath一定要以: . 开头，代表当前节点
```

# **Day04笔记**

## **requests.get()参数**

### **查询参数-params**

- 参数类型

```python
字典,字典中键值对作为查询参数
{
    'kw':'赵丽颖吧',
    'pn':'50'
}
```

- 使用方法

```python
1、res = requests.get(url,params=params,headers=headers)
2、特点: 
   * url为基准的url地址，不包含查询参数
   * 该方法会自动对params字典编码,然后和url拼接
```

- 示例

```python
# http://tieba.baidu.com/f?kw=%E8%D3&pn=50
import requests

baseurl = 'http://tieba.baidu.com/f?'
params = {
  'kw' : '赵丽颖吧',
  'pn' : '50'
}
headers = {'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)'}
# 自动对params进行编码,然后自动和url进行拼接,去发请求
res = requests.get(baseurl,params=params,headers=headers)
res.encoding = 'utf-8'
print(res.text)
```

**练习**

把课程第1天中的 百度贴吧 抓取案例改为使用requests模块的params参数实现？

```python
def get_page(self,params):
    res = requests.get(self.url,params=params,headxxxx)
```

### **Web客户端验证 参数-auth**

- 作用及类型

```python
1、针对于需要web客户端用户名密码认证的网站
2、auth = ('tarenacode','code_2013')
```

- 达内code课程方向案例

```python

```

**思考：爬取具体的笔记文件？（把今天的笔记抓取下来）**

```python
import os 
if not os.path.exists('路径'):
	os.makedirs('路径')
    # os.mkdir('路径')

# 小总结:requests.get()参数
1、url
2、params : {}
3、auth   : ()
4、headers: {}
5、timeout
```

### **证书认证参数-verify**

- 适用网站及场景

```python
1、适用网站: https类型网站但是没有经过 证书认证机构 认证的网站
2、适用场景: 抛出 SSLError 异常则考虑使用此参数
```

- 参数类型

  ```python
  1、verify=True(默认)   : 检查证书认证
  2、verify=False（常用）: 忽略证书认证
  # 示例
  response = requests.get(
  	url=url,
  	params=params,
  	headers=headers,
  	verify=False
  )
  # 如果代码抛出 SSLError ，则添加 verify=False 参数
  ```

### **代理IP参数-proxies**

- 定义

```python
1、定义: 代替你原来的IP地址去对接网络的IP地址。
2、作用: 隐藏自身真实IP,避免被封。
```

- 普通代理

**获取代理IP网站**

```python
西刺代理、快代理、全网代理、代理精灵、... ... 
```

**参数类型**

```python
1、语法结构
   	proxies = {
       	'协议':'协议://IP:端口号'
   	}
2、示例
    proxies = {
    	'http':'http://IP:端口号',
    	'https':'https://IP:端口号'
	}
  # res = requests.get(url,proxies=proxies,headers=xx)
```

**示例**

1. 使用免费普通代理IP访问测试网站: http://httpbin.org/get

   ```python
   import requests
   
   url = 'http://httpbin.org/get'
   headers = {
       'User-Agent':'Mozilla/5.0'
   }
   # 定义代理,在代理IP网站中查找免费代理IP
   proxies = {
       'http':'http://115.171.85.221:9000',
       'https':'https://115.171.85.221:9000'
   }
   html = requests.get(url,proxies=proxies,headers=headers,timeout=5).text
   print(html)
   ```

2. 思考: 建立一个自己的代理IP池，随时更新用来抓取网站数据

   fake_useragent使用示例

   ```python
   # 随机生成1个User-Agent
   from fake_useragent import UserAgent
   
   ua = UserAgent()
   print(ua.random)
   ```

   建立自己的IP代理池

```python
1、爬取代理IP网站上的免费代理IP
2、对免费代理IP做测试，找到能用的,保存起来
```

**2、写一个获取收费开放代理的接口**

```python

```

**3、使用收费开放代理IP访问测试网站: http://httpbin.org/get**

```
1、从代理网站上获取购买的普通代理的api链接
2、从api链接中提取出IP
3、随机选择代理IP访问网站进行数据抓取
```

```python

```

- 私密代理

**语法格式**

```python
1、语法结构
proxies = {
    '协议':'协议://用户名:密码@IP:端口号'
}

2、示例
proxies = {
	'http':'http://用户名:密码@IP:端口号',
    'https':'https://用户名:密码@IP:端口号'
}
```

**示例代码**

```python
import requests
url = 'http://httpbin.org/get'
proxies = {
    'http': 'http://309435365:szayclhp@122.114.67.136:16819',
    'https':'https://309435365:szayclhp@122.114.67.136:16819',
}
headers = {
    'User-Agent' : 'Mozilla/5.0',
}

html = requests.get(url,proxies=proxies,headers=headers,timeout=5).text
print(html)
```

**requests模块参数总结**

```python
1、url 
2、params : {}
3、proxies: {}
4、auth:   ()
5、verify:  True/False
6、timeout
```

## **requests.post()**

- 适用场景

```
Post类型请求的网站
```

- 参数-data

```python
response = requests.post(url,data=data,headers=headers)
# data ：post数据（Form表单数据-字典格式）
```

- 
  请求方式的特点

```python
# 一般
GET请求 : 参数在URL地址中有显示
POST请求: Form表单提交数据
```

**有道翻译破解案例(post)**

1. 目标

```python
破解有道翻译接口，抓取翻译结果
# 结果展示
请输入要翻译的词语: elephant
翻译结果: 大象
**************************
请输入要翻译的词语: 喵喵叫
翻译结果: mews
```

2. 实现步骤

   ```python
   1、浏览器F12开启网络抓包,Network-All,页面翻译单词后找Form表单数据
   2、在页面中多翻译几个单词，观察Form表单数据变化（有数据是加密字符串）
   3、刷新有道翻译页面，抓取并分析JS代码（本地JS加密）
   4、找到JS加密算法，用Python按同样方式加密生成加密数据
   5、将Form表单数据处理为字典，通过requests.post()的data参数发送
   ```

**具体实现**

- 1、开启F12抓包，找到Form表单数据如下:

```python
i: 喵喵叫
from: AUTO
to: AUTO
smartresult: dict
client: fanyideskweb
salt: 15614112641250
sign: 94008208919faa19bd531acde36aac5d
ts: 1561411264125
bv: f4d62a2579ebb44874d7ef93ba47e822
doctype: json
version: 2.1
keyfrom: fanyi.web
action: FY_BY_REALTlME
```

- 2、在页面中多翻译几个单词，观察Form表单数据变化

```python
salt: 15614112641250
sign: 94008208919faa19bd531acde36aac5d
ts: 1561411264125
bv: f4d62a2579ebb44874d7ef93ba47e822
# 但是bv的值不变
```

- 3、一般为本地js文件加密，刷新页面，找到js文件并分析JS代码

```python
# 方法1
Network - JS选项 - 搜索关键词salt
# 方法2
控制台右上角 - Search - 搜索salt - 查看文件 - 格式化输出

# 最终找到相关JS文件 : fanyi.min.js
```

- 4、打开JS文件，分析加密算法，用Python实现

```python
# ts : 经过分析为13位的时间戳，字符串类型
js代码实现:  "" + (new Date).getTime()
python实现:  

# salt
js代码实现:  r+parseInt(10 * Math.random(), 10);
python实现:  

# sign（设置断点调试，来查看 e 的值，发现 e 为要翻译的单词）
js代码实现: n.md5("fanyideskweb" + e + salt + "n%A-rKaT5fb[Gy?;N5@Tj")
python实现:
```

-  5、代码实现

```python

```

# **今日作业**

```python
1、仔细复习并总结有道翻译案例，抓包流程，代码实现
2、通过百度翻译，来再次熟练抓包流程，分析，断点调试等操作
```

## **Ajax动态加载网站数据抓取**

**网站特点-Ajax动态加载**

```python
1、滚动鼠标滑轮时动态加载（京东商城、豆瓣电影）
2、页面局部刷新（小米应用商店、腾讯招聘）
```

**分析抓取步骤**

```python
# 最终目标: 找到json文件的URL地址
1、抓包: F12 -> Network -> XHR
2、触发动态加载（滚动鼠标、点击下一页...）
3、XHR中,点击右侧 Preview,确定有正确数据
4、点开headers
   # 1. General : Request URL(json地址)
   # 2. QueryStringParameters : 观察查询参数变化
```

**豆瓣电影数据抓取-Ajax**

```python
1、网址: 豆瓣电影 - 排行榜 - 剧情
2、目标: 电影名称、评分

'https://movie.douban.com/j/chart/top_list?type=13&interval_id=100%3A90&action=&start=0&limit={}'
```

**今日作业**

1、升级 豆瓣电影案例 

```
用户从终端输入要抓取的电影类型: (剧情|喜剧|动作|爱情)
然后再输入要抓取的数量:
```

2、腾讯招聘 一级页面 抓取

```
百度搜索：腾讯招聘 - > 工作岗位
```

3、哔哩哔哩小视频抓取

```python
http://vc.bilibili.com/p/eden/rank#/?tag=全部
```





