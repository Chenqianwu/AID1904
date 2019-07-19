"""空洞文件"""

f = open('test','wb')

f.write(b'start')
f.seek(1000,2) # 结尾位置向后移动１０００字节
f.write(b'end')

f.close()