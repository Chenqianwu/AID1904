"""
file_open.py 打开文件
"""

# 打开文件
try:
  fd = open('img.jpg','ab+')
except FileNotFoundError as e:
  print(e)

# 开始你的读写

# 关闭文件
fd.close()
