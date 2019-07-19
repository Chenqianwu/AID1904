"""
创建udp套接字
设置套接字可以接收广播
选择接收端口
"""

from socket import *
s=socket(AF_INET,SOCK_DGRAM)
#让套接字可以接收广播
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

s.bind(('0.0.0.0',8080))

while True:
    msg,addr=s.recvfrom(1024)
    print(msg.decode())
s.close()




