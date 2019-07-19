"""
http请求响应示例
"""
from socket import *
s=socket()
s.bind(('0.0.0.0',8088))
s.listen(3)
c,addr=s.accept()
print("connect from",addr)
data=c.recv(4096)
print(data)
data="""HTTP/1.1 200 OK
Content-Type:text/html

<h1>Hello world</>
"""
# c.send(b'OK')
c.send(data.encode())

c.close()
s.close()