"""
tcp_client.py  tcp客户端流程
重点代码
"""

from socket import *

#　创建ｔｃｐ套接字
sockfd = socket() #　参数默认即ｔｃｐ套接字

# 连接服务端程序
server_addr = ("127.0.0.1",8888)  #　服务端地址
sockfd.connect(server_addr)

while True:
  #　消息发送接收
  data = input("Msg>>")
  #　如果直接回车，则跳出循环
  if not data:
    break
  sockfd.send(data.encode()) #　转换字节串发送
  data = sockfd.recv(1024)
  print("Server:",data.decode())

sockfd.close()


