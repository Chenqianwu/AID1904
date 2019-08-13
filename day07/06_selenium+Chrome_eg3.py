from selenium import webdriver

# 创建浏览器对象
browser = webdriver.PhantomJS()
# 打开百度
browser.get('http://www.baidu.com/')
browser.save_screenshot('baidu.png')
# 打印响应内容(page_source属性)
html = browser.page_source

# -1　没有这个字符串
result = browser.page_source.find('su')
print(result)




















