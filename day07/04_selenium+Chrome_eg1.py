# 导入selenium中的webdriver接口
from selenium import webdriver

# 添加无界面参数
options = webdriver.ChromeOptions()
options.add_argument('--headless')

# 创建浏览器对象
browser = webdriver.Chrome(options=options)
# 地址栏中输入百度URL
browser.get('http://www.baidu.com/')
# 获取屏幕截图
browser.save_screenshot('baidu.png')
# 关闭浏览器
browser.quit()


















