"""
match对象使用示例
"""

import  re

pattern = r"(ab)cd(?P<pig>ef)"
regex = re.compile(pattern)
obj = regex.search('abcdefghi') # match对象

# 属性变量
# print(obj.pos) # 目标字符串开头位置
# print(obj.endpos) # 目标字符串结尾位置
# print(obj.re)   # 正则
# print(obj.string) # 目标字符串
# print(obj.lastgroup) # 最后一组组名
# print(obj.lastindex) # 最后一组序列号

# 属性方法
print(obj.span())  #匹配内容在目标字符串中位置
print(obj.start())
print(obj.end())
print(obj.groupdict())  # 捕获组字典
print(obj.groups()) # 子组内容
print(obj.group('pig')) #获取匹配内容