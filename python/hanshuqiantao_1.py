#！ /usr/bin/python
##################################################################
#			      函数的嵌套					#			
##################################################################
"""
函数的嵌套是指在函数内部调用其它函数
"""
def sum(a, b):
    return a + b
def sub(a,b):
    return a - b
def func():
    x = 1
    y = 2
    m = 3
    n = 4
    return sum(x,y)*sub(m,n)
print(func(),"\n")    


"""\n 是换行，函数的嵌套层数不宜过多，会造成代码的可读性差，不易维护，一般在3层即可。"""

def func():
    x = 1
    y =2
    m =3
    n =4
    def sum(a,b):
        return a + b
    def sub(a,b):
        return a - b
    return sum(x,y)*sub(m,n)
print(func(),"\n")

"""内部函数调用外部函数"""
def func():
    x = 1
    y = 2
    m = 3
    n = 4
    def sum():
        return x + y
    def sub():
        return m - n
    return sum()*sub()
print(func(),"\n")













