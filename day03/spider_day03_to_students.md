# *Day02回顾**

## **爬取网站思路**

```python
1、先确定是否为动态加载网站
2、找URL规律
3、正则表达式
4、定义程序框架，补全并测试代码
```

## **存入csv文件**

```python
 import csv
 with open('xxx.csv','w') as f:
 	writer = csv.writer(f)
 	writer.writerow([])
    writer.writerows([(),(),()])
```

## **持久化存储之MySQL**

```mysql
db = pymysql.connect('IP',...)
cursor = db.cursor()
# cursor.execute('SQL',[])
# cursor.executemany('SQL',[(),(),()])
db.commit()
cursor.close()
db.close()
```

## **requests模块**

- get()

```python
 1、发请求并获取响应对象
 2、res = requests.get(url,headers=headers)
```

- 响应对象res属性

```python
res.text ：字符串
res.content ：bytes
res.encoding：字符编码 res.encoding='utf-8'
res.status_code ：HTTP响应码
res.url ：实际数据URL地址

# 方式一 
res = requests.get(url,headers=headers)
res.encoding = 'utf-8'
html = res.text
# 方式二
res = requests.get(url,headers=headers)
html = res.content.decode('utf-8')
```

- 非结构化数据保存

```python
with open('xxx.jpg','wb') as f:
	f.write(res.content)
```

## **多级页面数据抓取**

```python
 1、先爬去一级页面,提取链接,继续跟进
 2、爬取二级页面,提取数据
 3、... ... 
```

## **Chrome浏览器安装插件**

- 安装方法

```python
1、把下载的相关插件（对应操作系统浏览器）后缀改为 .zip
2、打开Chrome浏览器 -> 右上角设置 -> 更多工具 -> 扩展程序 -> 点开开发者模式
3、把相关插件 拖拽 到浏览器中，释放鼠标即可安装
4、重启浏览器，使插件生效
```

- 需要安装插件

```python
1、Xpath Helper: 轻松获取HTML元素的xPath路径
   打开/关闭 : Ctrl + Shift + x
2、Proxy SwitchyOmega: Chrome浏览器中的代理管理扩展程序
3、JsonView: 格式化输出json格式数据
```

# **Day03笔记**



## ==**xpath解析**==

- 定义

```python
XPath即为XML路径语言，它是一种用来确定XML文档中某部分位置的语言，同样适用于HTML文档的检索
```

- 示例HTML代码

```html
<ul class="book_list">
    <li>
        <title class="book_001">Harry Potter</title>
        <author>J K. Rowling</author>
        <year>2005</year>
        <price>69.99</price>
    </li>

    <li>
        <title class="book_002">Spider</title>
        <author>Forever</author>
        <year>2019</year>
        <price>49.99</price>
    </li>
</ul>
```

- 匹配演示

```python
1、查找所有的li节点
   //li
2、查找li节点下的title子节点中,class属性值为'book_001'的节点
   //li/title[@class="book_001"]
3、查找li节点下所有title节点的,class属性的值
   //li//title/@class

# 只要涉及到条件,加 []
# 只要获取属性值,加 @
```

- 选取节点

```python
1、// ：从所有节点中查找（包括子节点和后代节点）
2、@  ：获取属性值
   # 使用场景1（属性值作为条件）- 如下xpath表达式含义？
     //div[@class="movie"]
   # 使用场景2（直接获取属性值）- 如下xpath表达式含义？
     //div/a/@src
```

- 匹配多路径（或）

```
xpath表达式1 | xpath表达式2 | xpath表达式3
```

- 常用函数

```python
1、contains() ：匹配属性值中包含某些字符串节点
   # 查找class属性值中包含"book_"的title节点
     //title[contains(@class,"book_")]
   # 匹配所有段子的 div 节点
     //div[contains(@id,"qiushi_tag_")]
    
     <div class="article block untagged mb15   typs_long" id="qiushi_tag_122044339">
     </div>

     <div class="article block untagged mb15 typs_long" id="qiushi_tag_122044339">
     </div>
2、text() ：获取节点的文本内容
   # 查找所有书籍的名称
     //ul[@class="book_list"]/li/title 
        #结果:<element title at xxxx>
     //ul[@class="book_list"]/li/title/text()
        #结果:'Harry Potter'
     
```

练习

```python
1、获取猫眼电影中电影信息的 dd 节点
   //dl[@class="board-wrapper"]/dd
2、获取电影名称的xpath://dl[@class="board-wrapper"]/dd//p[@class="name"]/a/text()
  获取电影主演的xpath://dl[@class="board-wrapper"]/dd//p[@class="star"]/text()
  获取上映商检的xpath: 
```



## **lxml解析库**

- 安装

```python
 
```

- 使用流程

```python
1、导模块
   from lxml import etree
2、创建解析对象
   parse_html = etree.HTML(html)
3、解析对象调用xpath
   r_list = parse_html.xpath('xpath表达式')
   # 只要调用xpath，结果一定为列表
```

- 练习

```python
from lxml import etree

html = '''<div class="wrapper">
	<i class="iconfont icon-back" id="back"></i>
	<a href="/" id="channel">新浪社会</a>
	<ul id="nav">
		<li><a href="http://domestic.firefox.sina.com/" title="国内">国内</a></li>
		<li><a href="http://world.firefox.sina.com/" title="国际">国际</a></li>
		<li><a href="http://mil.firefox.sina.com/" title="军事">军事</a></li>
		<li><a href="http://photo.firefox.sina.com/" title="图片">图片</a></li>
		<li><a href="http://society.firefox.sina.com/" title="社会">社会</a></li>
		<li><a href="http://ent.firefox.sina.com/" title="娱乐">娱乐</a></li>
		<li><a href="http://tech.firefox.sina.com/" title="科技">科技</a></li>
		<li><a href="http://sports.firefox.sina.com/" title="体育">体育</a></li>
		<li><a href="http://finance.firefox.sina.com/" title="财经">财经</a></li>
		<li><a href="http://auto.firefox.sina.com/" title="汽车">汽车</a></li>
	</ul>
	<i class="iconfont icon-liebiao" id="menu"></i>
</div>'''

# 问题1：获取所有 a 节点的文本内容

# 问题2：获取所有 a 节点的 href 的属性值

# 问题3： 获取所有 a 节点的href的属性值, 但是不包括 / 

# 问题4： 获取 图片、军事、...,不包括新浪社会

```

## **猫眼电影（xpath）**

- 目标

```python
 1、地址: 猫眼电影 - 榜单 - top100榜
 2、目标: 电影名称、主演、上映时间
```

- 步骤

```python
1、确定是否为静态页面（右键-查看网页源代码，搜索关键字确认）
2、写xpath表达式
3、写程序框架
```

- xpath表达式

```python
1、基准xpath: 匹配所有电影信息的节点对象列表
    //dl[@class="board-wrapper"]/dd
    
2、遍历对象列表，依次获取每个电影信息
   for dd in dd_list:
	   电影名称 ：dd.xpath('./a/@title')[0].strip()
	   电影主演 ：dd.xpath('.//p[@class="star"]/text()')[0].strip()
	   上映时间 ：dd.xpath('.//p[@class="releasetime"]/text()')[0].strip()
```

- 代码实现（修改之前urllib库代码）

```python
1、将urllib库改为requests模块实现
2、改写parse_page()方法
```

```python
1、基准xpath: 节点对象列表
2、for循环依次遍历节点对象, 节点对象.path('')
```

## **链家二手房案例（xpath）**

- 实现步骤

**1. 确定是否为静态**

```python
打开二手房页面 -> 查看网页源码 -> 搜索关键字
```

2. **xpath表达式**

```python
1、基准xpath表达式(匹配每个房源信息节点列表)
   //ul[@class="sellListContent"]/li[@class="clear LOGCLICKDATA"] | //ul[@class="sellListContent"]/li[@class="clear LOGVIEWDATA LOGCLICKDATA"]
2、依次遍历后每个房源信息xpath表达式
   * 名称: .//a[@data-el="region"]/text()
   * 总价: .//div[@class="totalPrice"]/span/text()
   * 单价: .//div[@class="unitPrice"]/span/text()
```

3. **代码实现**

```python
import requests
from lxml import etree
import time

class LianjiaSpider(object):
  def __init__(self):
    pass

  def get_page(self,url):
    pass

  def parse_page(self,html):
    pass

  def main(self):
    pass

if __name__ == '__main__':
  start = time.time()
  spider = LianjiaSpider()
  spider.main()
  end = time.time()
  print('执行时间:%.2f' % (end-start))
```

## **百度贴吧图片抓取**

- 目标

```python
抓取指定贴吧所有图片
```

- 思路

```python
1、获取贴吧主页URL,下一页,找到不同页的URL规律
2、获取1页中所有帖子URL地址: [帖子链接1,帖子链接2,...]
3、对每个帖子链接发请求,获取图片URL
4、向图片的URL发请求,以wb方式写入本地文件
# 向1个帖子链接发请求后 --> 提取图片链接,把图片保存到本地
```

- 实现步骤

1.  **贴吧URL规律**

```python
http://tieba.baidu.com/f?kw=??&pn=50
```

2. **xpath表达式**

```python
1、帖子链接xpath
   //*[@id="thread_list"]/li[@class=" j_thread_list clearfix"]/div/div[2]/div[1]/div[1]/a/@href

    
//*[@id="thread_list"]/li//div[@class="t_con cleafix"]/div/div/div/a/@href
    
    
2、图片链接xpath
   //div[@class="d_post_content_main d_post_content_firstfloor"]//div[@class="d_post_content j_d_post_content  clearfix"]/img[@class="BDE_Image"]/@src

# //img[@class="BDE_Image"]/@src
3、视频链接xpath
   //div[@class="video_src_wrapper"]/embed/@data-video
   # 注意: 此处视频链接前端对响应内容做了处理,需要查看网页源代码来查看，复制HTML代码在线格式化
```

3. **==百度贴吧视频抓取反爬机制（对响应内容做处理）==**

```html
<div class="video_src_wrapper">
    <embed  data-video="http://tb-video.bdstatic.com/tieba-smallvideo-transcode-cae/2754153_8fcd225842344de9901c1489e49defbe_0_cae.mp4"
```

## **requests.get()参数**

### **查询参数-params**

- 参数类型

```python
字典,字典中键值对作为查询参数
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

### **Web客户端验证 参数-auth**

- 作用及类型

```python
1、针对于需要web客户端用户名密码认证的网站
2、auth = ('username','password')
```

- 达内code课程方向案例

```python

```

**思考：爬取具体的笔记文件？**



### **SSL证书认证参数-verify**

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
  ```

### **代理参数-proxies**

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

```python

```

# **今日作业**


**糗事百科（xpath）**

```python
1、URL地址: https://www.qiushibaike.com/text/
2、目标 ：用户昵称、段子内容、好笑数量、评论数量
```

**电影天堂（xpath和requests模块实现）**

