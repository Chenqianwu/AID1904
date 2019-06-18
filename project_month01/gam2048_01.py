"""
  2048 游戏核心算法
"""


# 1. 定义函数,将列表中0元素移至末尾.
#    [2,0,2,0]  --> [2,2,0,0]
#    [2,0,0,2] -->  [2,2,0,0]
#    [2,4,0,2] -->  [2,4,2,0]
def zero_to_end(list_target):
  # 思路:删除0元素,再末尾增加.
  for i in range(len(list_target) - 1, -1, -1):
    if list_target[i] == 0:
      del list_target[i]
      list_target.append(0)
  return list_target


# ---------测试-----------
# list01 = [0, 4, 0, 2]
# zero_to_end(list01)
# print(list01)


# 2. 定义函数,合并列表中相同元素  14:43
#    [2,2,0,0]  --> [4,0,0,0]
#    [2,0,0,2] -->  [2,2,0,0] --> [4,0,0,0]
#    [2,2,0,2] -->  [4,2,0,0]
#    [2,2,0,4] -->  [4,4,0,0]
def merge(list_target):
  zero_to_end(list_target)  # [2,0,0,2] -->  [2,2,0,0]
  # 如果相邻且相同
  for i in range(len(list_target) - 1):
    if list_target[i] == list_target[i + 1]:
      # 合并[2,2,2,0] ->[4,2,2,0] --> [4,2,0,0]
      list_target[i] += list_target[i + 1]
      del list_target[i + 1]
      list_target.append(0)


# 测试
# list01 = [0, 2, 2, 2]
# merge(list01)
# print(list01)
""" 3. 定义函数,向左移动二维列表.
[
  [2,2,0,2], 
  [0,2,0,4],
  [2,0,4,2],
  [0,4,2,2],
]
"""


def move_left(map):
  # 思想:将每行(从左向右获取行数据)传递给合并函数
  for row in map:
    # 传递给merge函数的是二维列表中的元素(一维列表对象地址)
    # 函数都是操作对象,所以无需通过返回值拿到操作结果.
    merge(row)


# 测试
# double_list= [
#   [2,2,0,2],
#   [0,2,0,4],
#   [2,0,4,2],
#   [0,4,2,2],
# ]
# move_left(double_list)
# print(double_list)

# 4.定义函数,向右移动.
""" 4. 定义函数,向左移动二维列表.
[
  [2,2,0,2],       -->  [0,0,2,4],
  [0,2,0,4],       -->  [0,0,2,4],
  [2,0,4,2],
  [0,4,2,2],        --> [0,0,4,4],
]
"""


def move_right(map):
  # 思想:将每行(从右向左获取行数据)传递给合并函数
  for i in range(len(map)):
    # map[0][::-1] 从右向左获取行数据(新列表)
    list_merge = map[i][::-1]
    merge(list_merge)
    # 将合并后的结果,从右向左获还给二维列表
    map[i][::-1] = list_merge


# 测试
double_list = [
  [2, 2, 0, 2],
  [0, 2, 0, 4],
  [2, 0, 4, 2],
  [0, 4, 2, 2],
]


# move_right(double_list)
# print(double_list)

# 作业1:向上移动(核心思想:从上到下获取列数据,形成一维列表,交给合并方法,最后恢复)
def move_up(map):
  # 00  10  20  30
  # 01  11  21  31
  for c in range(4):
    list_merge = []
    for r in range(4):
      list_merge.append(map[r][c])

    merge(list_merge)

    for r in range(4):
      map[r][c] = list_merge[r]


# move_up(double_list)
# print(double_list)

# 作业2:向下移动(核心思想:从下到上获取列数据,形成一维列表,交给合并方法,最后恢复)
def move_down(map):
  # 30  20  10  00
  for c in range(4):
    list_merge = []
    for r in range(3, -1, -1):
      list_merge.append(map[r][c])

    merge(list_merge)

    # list_merge(从左到右) 赋值给 二维列表(从下到上)
    for r in range(3, -1, -1):  # 3 2 1 0
      map[r][c] = list_merge[3 - r]


move_down(double_list)
print(double_list)
