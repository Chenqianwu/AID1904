# 3.
# 向一个文件写入日志, 写入格式:
#
# 1.
# 2019 - 1 - 1 12: 12:12
# 2.
# 2019 - 1 - 1 12: 12:13
# 3.
# 2019 - 1 - 1 12: 12:24
#
# 要求每隔1秒写入一次, 每条时间占一行.程序死循环, crtl - c退出.如果程序退出重新启动时内容能跟上次内容衔接(序列号)
import time
f = open('log.txt', 'a+')
n = 0
f.seek(0, 0)
for line in f:
    #将偏移量移动到开始然后计数
    n += 1
while True:
    n += 1
    time.sleep(1)
    f.write(('%d %s\n' % (n, time.ctime())))#ctime获取当前时间
    #随时看到文件变化
    # f.seek(2)
f.close()
