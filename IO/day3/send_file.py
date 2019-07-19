from socket import *
s=socket()
s.connect(('127.0.0.1',8888))

f=open('img.jpg','rb')
#读取内容将其发送
while True:
    data=f.read(1024)
    if not data:
        break
    s.send(data)
f.close()
s.close()