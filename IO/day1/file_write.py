"""
file_write.py　写文件示例
"""

# w原有内容被清除,a则追加
f = open('test','a')

#　如果是ｗｂ打开要转换为字节串写入
# f.write("hello 死鬼\n".encode())
# f.write("哎呀，干啥呀".encode())

f.writelines(['abc\n','def\n'])

f.close()