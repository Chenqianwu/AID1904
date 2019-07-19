
word = input("Word:")

#　默认ｒ打开
f = open("dict.txt")

for line in f:
  tmp = line.split(' ')[0]
  #　遍历的单词已经大于目标
  if tmp > word:
    print("没有找到该单词")
    break
  elif tmp == word:
    print(line)
    break
else:
  print("没有找到该单词")

f.close()