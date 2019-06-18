"""
  学生管理器系统
"""


class StudentModel:
  """
    学生数据模型
  """

  def __init__(self, name="", age=0, score=0, id=0):
    self.name = name
    self.age = age
    self.score = score
    self.id = id

  @property
  def name(self):
    return self.__name

  @name.setter
  def name(self, value):
    self.__name = value

  @property
  def age(self):
    return self.__age

  @age.setter
  def age(self, value):
    self.__age = value

  @property
  def score(self):
    return self.__score

  @score.setter
  def score(self, value):
    self.__score = value

  @property
  def id(self):
    return self.__id

  @id.setter
  def id(self, value):
    self.__id = value


class StudentManagerController:
  """
    逻辑控制类
  """

  def __init__(self):
    # 数据结果:[StudentModel(...),StudentModel(...)]
    self.__stu_list = []

  @property
  def stu_list(self):
    # 缺点:返回列表地址,外部还能修改列表元素
    return self.__stu_list
    # 缺点:每次返回新列表(复制一份新列表),占用内存.
    # return self.__stu_list[:]

  def add_student(self, new_stu):
    """
      添加学生
    :param new_stu: 没有id的新学生
    """
    new_stu.id = self.__generate_id()
    self.__stu_list.append(new_stu)

  def __generate_id(self):
    # 最后一个学生编号+1
    return self.__stu_list[-1].id + 1 if len(self.__stu_list) > 0 else 1

  def remove_student(self, id):
    """
      根据编号删除学生
    :param id: 学生编号
    :return: 是否删除成功
    """
    for item in self.__stu_list:
      if item.id == id:
        self.__stu_list.remove(item)
        return True  # 删除成功
    return False  # 删除失败

  # 15:40 上课
  def update_student(self, stu_info):
    """
      根据编号,修改其余信息.
    :param stu_info: 学生信息
    :return:是否修改成功
    """
    # 根据 stu_info.id 查找学生对象
    for item in self.__stu_list:
      if item.id == stu_info.id:
        # 修改学生对象
        item.name = stu_info.name
        item.age = stu_info.age
        item.score = stu_info.score
        return True
    return False

# --------测试添加---------------
# controller = StudentManagerController()
# controller.add_student(StudentModel("无极", 25, 100))
# controller.add_student(StudentModel("无极", 25, 100))

# 因为只读,所以不能修改stu_list
# controller.stu_list = []

# 从语法上看,没有修改属性,而是修改学生列表的第一个元素
# 如果连列表都不能修改,则需要属性返回列表的切片
# controller.stu_list[0] = StudentModel()

# --------测试删除---------------
# re = controller.remove_student(1)
# print(re)
# --------测试修改---------------
# stu = StudentModel("赵敏",30,80,2)
# controller.update_student(stu)
# for item in controller.stu_list:
#   print(item.name)

# 17:10
class StudentManagerView:
  """
    学生管理器视图
  """

  def __init__(self):
    # 创建控制器对象
    self.__manager = StudentManagerController()

  def __display_menu(self):
    """
    显示菜单
    :return:
    """
    print("1) 添加学生")
    print("2) 显示学生")
    print("3) 删除学生")
    print("4) 修改学生")
    print("5) 按照成绩升序显示")

  def __select_menu_item(self):
    """
      选择菜单项
    :return:
    """
    number = input("请输入选项:")
    if number == "1":
      self.__input_student()
    elif number == "2":
      self.__output_students(self.__manager.stu_list)
    elif number == "3":
      self.__delete_student()
    elif number == "4":
      self.__modify_student()

  def main(self):
    """
      入口逻辑
    """
    while True:
      self.__display_menu()
      self.__select_menu_item()

  def __input_student(self):
    """
      输入学生
    """
    name = input("请输入姓名:")
    age = int(input("请输入年龄:"))
    score = int(input("请输入成绩:"))
    stu = StudentModel(name, age, score)
    self.__manager.add_student(stu)

  def __output_students(self, list_stu):
    """
      显示所有学生
    """
    for item in list_stu:
      print("%d---%s---%d---%d" % (item.id, item.name, item.age, item.score))

  def __delete_student(self):
    """
      删除学生
    """
    id = int(input("请输入需要删除的学生编号:"))
    if self.__manager.remove_student(id):
      print("删除成功")
    else:
      print("删除失败")

  def __modify_student(self):
    """
     修改学生信息
    :return:
    """
    stu = StudentModel()
    stu.id = int(input("请输入需要修改的学生编号:"))
    stu.name = input("请输入姓名:")
    stu.age = int(input("请输入年龄:"))
    stu.score = int(input("请输入成绩:"))
    if self.__manager.update_student(stu):
      print("修改成功")
    else:
      print("修改失败")


view = StudentManagerView()
view.main()
