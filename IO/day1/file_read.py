"""
file_read.py  文件读取演示
"""

# 打开文件
f = open('test','r')

# #　ｒｅａｄ循环读取文件
# while True:
#   #　一次最多读取１０２４字节
#   data = f.read(1024)
#   #　读到文件结尾得到空字符串，此时跳出循环
#   if not data:
#     break
#   print("读取的内容:",data)

#　读取一行内容
# data = f.readline()
# print("读取的内容:",data)
# data = f.readline()
# print("读取的内容:",data)

#　读取所有内容，每行作为列表中一个元素
# data = f.readlines()
# print("读取的内容:",data)

#　每次获取文件一行
for line in f:
  print(line)

f.close()







