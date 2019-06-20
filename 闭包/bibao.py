# def func(a, b):
#     def line(x):
#         return a * x - b
#
#     return line
#
#
# line = func(2, 3)
# print(line(5))
#在这个案例中，外函数func有接收参数 a=2，b=3，内函数line接收参数x=5，在内函数体中计算了a*x-b 即 2×5-3的值作为返回值，外函数返回内函数的引用，这里的引用指的是内函数line在内存中的起始地址，最终调用内函数line()得到返回值7


# def func(a, b):
#     def line(x):
#         nonlocal a
#         a = 3
#         return a * x - b
#
#     return line
#
#
# line = func(2, 3)
# print(line(5))

# def mul():
#     return [lambda x : i*x for i in range(4)]
#
# print([m(2) for m in mul()])

# def foo1(n):
#     def foo2(m):
#         return n + m
#     return foo2
#
# a = foo1(2)
# print(a(3))
#
# def foo1():
#     var = 'hello'
#     def foo2():
#         print(var)
#     return foo2
# a = foo1()
# a()
#
# def mul():
#     func_list = []
#     for i in range(4):
#         def lam(x):
#             return x*i
#         func_list.append(lam)
#     return func_list
#
# print([m(2) for m in mul()])


# 闭包定义：
# 1、闭包是一个嵌套函数
# 2、闭包必须返回嵌套函数
# 3、嵌套函数必须引用一个外部的非全局的局部自由变量

def multiples():
    return [lambda x : i*x for i in range(4)]
print([m(2) for m in  multiples()])


def mul():
    list_=[]
    for i in range(4):
        def lam(x):
            return x*i
#相对而言局部变量绑定的是值，非局部变量绑定的是空间， 而不是值本身，所以，for循环生成的i，相对于函数lam来说，是全局变量，所以绑定的是i所在的内存地址，但i最后变成了3，lam绑定的是3。
        list_.append(lam)
    return list_
print([m(2) for m in  mul()])

def mul():
    list_=[]
    for i in range(4):
        def lam(x,n=i):
            #这时候因为 n 是局部变量，所以绑定的是 n 的值
            return x*n
        list_.append(lam)
    return list_
print([m(2) for m in mul()])

