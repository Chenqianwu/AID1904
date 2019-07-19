import re

s = """2008-08-08北京奥运会,
2008-05-12汶川地震,
2019-10-01建国70周年
"""
pattern = r"\d{4}-\d{2}-\d{2}"
l = re.findall(pattern,s)

for i in l:
  print(re.sub(r'-','/',i))


