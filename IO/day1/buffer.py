"""
buffer.py 缓冲区
"""
import os
#　１表示行缓冲
f = open('test','w',1)

while True:
  s = input(">>")
  f.write("nihao\n")
  f.flush() # 将缓冲内容写入磁盘

f.close()
