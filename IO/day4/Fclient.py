from socket import *
from day04.find_word import *
sockfd=socket(AF_INET,SOCK_DGRAM)
ADDR=('127.0.0.1',8888)

while True:
    # 循环发送消息
    data = input("Msg>>")
    if not data:
        break
    sockfd.sendto(data.encode(), ADDR)
    msg, addr = sockfd.recvfrom(1024)
    print("from server:", msg.decode())

