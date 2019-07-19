"""
http 发送网页给浏览器
"""
from socket import *
# 处理客户端请求
def handle(connfd):
    request=connfd.recv(4096)
    #防止客户端断开request为空
    if not request:
        return
    request_line=request.splitlines()[0]
    # print(request_line)
    info=request_line.decode().split(' ')[1]
    # print(info)
    if info =='/':
        with open('index.html') as f:
            response = 'HTTP/1.1 200 OK\r\n'
            response+="Content-Type:text/html\r\n"
            response+="\r\n"
            response+=f.read()
    else:
        response = 'HTTP/1.1 404NOT FOUND\r\n'
        response += "Content-Type:text/html\r\n"
        response += "\r\n"
        response += "<h1>Sorry.....</h>\r\n"
    #发送给浏览器
    connfd.send(response.encode())
#搭建tcp网络
sockfd=socket()
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sockfd.bind(('0.0.0.0',8000))
sockfd.listen(3)
while True:
    connfd,addr=sockfd.accept()
    handle(connfd)  #处理客户端（浏览器）请求








