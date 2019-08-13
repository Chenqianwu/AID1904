import csv

with open('test.csv','w') as f:
    # 初始化写入对象
    writer = csv.writer(f)
    writer.writerow(['超哥哥',20])
    writer.writerow(['步惊云',22])

with open('test.csv','a') as f:
    writer = csv.writer(f)
    data_list = [('聂风',23),('秦霜',30)]

    writer.writerows(data_list)
















