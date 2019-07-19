from socket import *
import struct
#服务端地址
ADDR = ('127.0.0.1',8888)
#创建套接字
sockfd=socket(AF_INET,SOCK_DGRAM)
while True:
    #循环发送消息
    id=input("请输入id：")
    name=input("请输入name：")
    age=input("请输入age：")
    score=input("请输入score：")
    data=struct.pack('i4si2f',id,name,age,score)
    if not data:
        break
    sockfd.sendto(data,ADDR)
    msg,addr=sockfd.recvfrom(1024)
    print("from server:",msg.decode())
