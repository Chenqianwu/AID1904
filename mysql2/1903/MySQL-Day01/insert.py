import pymysql

#连接对象
db=pymysql.connect(
    'localhost','root','123456','country',
    charset='utf8')
#游标对象
cursor=db.cursor()
#执行sql命令
#定义空列表，存储2000000个名字
data_list=[]
for i in range(1,2000001):
    name='Tom{}'.format(str(i))
    data_list.append(name)
ins='insert into students(name) values(%s)'
cursor.executemany(ins,data_list)
db.commit()
#关闭
cursor.close()
db.close()
# print(data_list)