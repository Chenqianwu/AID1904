"""
  程序入口模块 main
  17:10 上课
"""
from ui import *

# 如果不是主模块,则不执行下列代码
# 目的:强迫程序从当前模块执行
if __name__ == "__main__":
  view = StudentManagerView()
  view.main()
  # try:
  #   view = StudentManagerView()
  #   view.main()
  # except:
  #   print("程序出错啦")



