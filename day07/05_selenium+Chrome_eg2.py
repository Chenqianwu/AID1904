from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('http://www.baidu.com/')
# 向搜索框输入　赵丽颖
# word = input('请输入要搜索的内容:')
browser.find_element_by_xpath('//*[@id="kw"]').send_keys('赵丽颖')
# 点击百度一下
browser.find_element_by_id('su').click()
# 给出时间加载页面
time.sleep(2)
browser.find_element_by_class_name('n').click()






