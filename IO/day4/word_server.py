from socket import *
DICT_TEXT='./dict.txt'

def find_word(word):
    f = open(DICT_TEXT)
    for line in f:
      tmp = line.split(' ')[0]
      #　遍历的单词已经大于目标
      if tmp > word:
        return "没有找到该单词"
      elif tmp == word:
        return line
    else:
      return "没有找到该单词"
s=socket(AF_INET,SOCK_DGRAM)
s.bind(('127.0.0.1',8888))
while True:
    data,addr=s.recvfrom(1024)
    mean=find_word(data.decode())
    s.sendto(mean.encode(),addr)
s.close()