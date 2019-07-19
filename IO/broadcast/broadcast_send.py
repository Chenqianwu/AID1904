"""
创建udp套接字
设置套接字可以发送广播
"""
from socket import *
import time
#广播地址
dest=('176.215.55.255',8080)

s=socket(AF_INET,SOCK_DGRAM)
#让套接字可以发送广播
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
data="""
  **************
   6.3 武汉 晴天
   望冬雪，夏赏花
   执子之手，不负韶华 
  **************
"""
while True:
    time.sleep(2)
    s.sendto(data.encode(),dest)
s.close()




