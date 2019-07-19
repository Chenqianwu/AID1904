from socket import *
sockfd=socket(AF_INET,SOCK_DGRAM)
sockfd.bind(('127.0.0.1',8888))
while True:
    fr=open('dict.txt')

    sockfd.recvfrom(1024)
    sockfd.sendto(fr.read())
fr.close()
sockfd.close()