"""
flags扩展功能展示
"""
import  re

s = """Hello
北京
"""
# 自能匹配ASCII
# regex = re.compile(r'\w+',flags=re.A)

# 不区分大小写
# regex = re.compile(r'[a-z]+',flags=re.I)

# 让.匹配换行
# regex = re.compile(r'.+',flags=re.S)


# ^ $匹配每行开头结尾
# regex = re.compile(r'Hello$',flags=re.M)

pattern = """\w+  # hello
\s+  # 匹配换行
\w+ # 北京
"""
regex = re.compile(pattern,flags=re.X|re.I)
l = regex.findall(s)
print(l)
