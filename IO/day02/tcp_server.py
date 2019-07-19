"""
tcp_server.py  tcp套接字服务端流程
重点代码
"""

import socket

# 　创建流式套接字
sockfd = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)

# 绑定地址
sockfd.bind(('0.0.0.0', 8888))

# 　设置sockfd为监听套接字
sockfd.listen(3)

# 　等待处理客户端连接
while True:
  print("Waiting for connect ...")
  try:
    connfd, addr = sockfd.accept()
    print("Connect from", addr)
  except KeyboardInterrupt:
    print("Server exit")
    break
  while True:
    #　收发消息
    data = connfd.recv(1024)
    if not data:
      break
    print("Message:",data.decode())
    n = connfd.send(b'** Thanks **')
    print("Send %d bytes"%n)
  connfd.close()  # 断开连接

#　关闭套接字
sockfd.close()
