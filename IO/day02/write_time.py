import time

f = open('log.txt','a+')

n = 0
f.seek(0,0) # 将偏移量移动待开始然后计数
for line in f:
  n += 1

while True:
  n += 1
  time.sleep(1)
  s = "%d.  %s\n"%(n,time.ctime())
  f.write(s)
  f.flush()  #　随时看到文件变化