# 嵌套函数
def sum(a, b):
    return a + b
def sub(a, b):
    return a - b
def func():
    x = 1
    y = 2
    m= 3
    n = 4
    return sum(x, y) * sub(m, n)

print (func())
