"""
views.py
提供复杂的逻辑数据操作处理，
包括和文件数据库的交互
逻辑算法的实现等
"""
def show_time():
    import time#模块在某些特定的地方可能只用一次
    return time.ctime()

def hello():
    return "Hello World"

def bye():
    return "Good Bye"