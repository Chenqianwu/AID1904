# 从终端输入一个文件名称(包含路径), 如果该文件存在则将该文件复制到当前目录下, 命名为1904(要求文件可以是任意类型), 如果文件不存在则打印该文件不存在
# *文件的打开方式
file_name=input("请输入文件名：")
try:
    fr=open(file_name,'rb')
except FileExistsError as e:
    print(e)
else:
    fw=open('file.jpg','wb')
    #循环复制
    while True:
        data=fr.read(1024)
        if not data:
            break
        fw.write(data)

    fr.close()
    fw.close()


