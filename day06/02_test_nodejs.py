# sudo pip3 install pyexecjs
import execjs

# 先把node.js中代码读出来
with open('node.js','r') as f:
    js_data = f.read()

# 创建对象
exec_obj = execjs.compile(js_data)
sign = exec_obj.eval('e("tiger")')
print(sign)











