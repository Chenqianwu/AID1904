
# w原有内容被清除,a则追加
f = open('student_info','a')

#　如果是ｗｂ打开要转换为字节串写入
# f.write("hello 死鬼\n".encode())
# f.write("哎呀，干啥呀".encode())

f.writelines(['name:Bob  age:30  score: 90\n','name:Lucy age:25  score: 99\n'])

f.close()