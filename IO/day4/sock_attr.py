"""
套接字属性演示
"""
from socket import *
#创建套接字
sockfd=socket()
#设置套接字端口立即重用
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sockfd.connect(("127.0.0.1",8888))
sockfd.listen(3)
c,addr=sockfd.accept()
print("套接字类型：",sockfd.type)
print("地址类型：",sockfd.family)
print("绑定的地址：",sockfd.getsockname())
print("获取文件描述符：",sockfd.fileno())
# print("获取连接的客户端地址:",sockfd.getpeername())
print("获取选项值:",sockfd.getsockopt(SOL_SOCKET,SO_REUSEADDR))
# c.recv(1024)




































