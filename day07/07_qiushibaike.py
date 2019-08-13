from selenium import webdriver

browser = webdriver.PhantomJS()
browser.get('https://www.qiushibaike.com/text/')

# 单元素查找
xpath = '//div[@class="content"]'
div = browser.find_element_by_xpath(xpath)
# print(div.text)

# 多元素查找
xpath = '//div[@class="content"]/span'
span_list = browser.find_elements_by_xpath(xpath)
for span in span_list:
    print(span.text)
    print('*'*50)













