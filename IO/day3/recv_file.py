from socket import *
s=socket()
s.bind(('127.0.0.1',8888))
s.listen(3)
c,addr=s.accept()
# print("waiting for connect..........")
print("connect from",addr)
#以二进制方式写入
f=open('dmm.jpg','wb')
# 循环接收内容，写入文件
while True:
    data=c.recv(1024)
    if not data:
        break
    f.write(data)

f.close()
c.close()
s.close()