from socket import *
def handle(connfd):
    request=connfd.recv(4096)
    if not request:
        return
    request_line=request.splitlines()[0]
    info=request_line.decode().split(' ')[1]

    if info=='/':
        with open('index.html') as f:
            response = "HTTP/1.1 200 OK\r\n"
            response+="Content-Type:text/html\r\n"
            response+="\r\n"
            response+=f.read()
    else:
        response = 'HTTP/1.1 404NOT FOUND\r\n'
        response += "Content-Type:text/html\r\n"
        response += "\r\n"
        response += "<h1>Sorry.....</h>\r\n"
    connfd.send(response.encode())
sockfd=socket()
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sockfd.bind(("0.0.0.0",8888))
sockfd.listen(3)
while  True:
    connfd,addr=sockfd.accept()
    handle(connfd)
