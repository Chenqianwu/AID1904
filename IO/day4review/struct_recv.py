from socket import *
# import struct
sockfd=socket(AF_INET,SOCK_DGRAM)
server_addr=('127.0.0.1',8888)
sockfd.bind(server_addr)
while True:
    # data=struct.unpack()
    data,addr=sockfd.recvfrom(1024)
    print("收到的信息",data.decode())
    sockfd.sendto(b'Receive',addr)
#关闭套接字
sockfd.close()