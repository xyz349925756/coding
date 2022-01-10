#！ /usr/bin/python
##################################################################
#		                     函数的返回值					#			
##################################################################
"""
函数的返回值使用return语句，return后面可以是变量或表达式
"""
from __future__ import division
def arithmetic(x,y,operator):
    result = {
        "+":x + y,
        "-":x - y,
        "*":x - y,
        "/":x / y
        }
    return result.get(arithmetic)
print("**************************************************************")
#python可以没有返回值，编译不会报错。
def func():
    pass
print(func())
print("**************************************************************")
#return返回多个值
def func1(x,y,z):
    l = [x,y,z]   #打包3个参数到一个列表。
    l.reverse()   #反转列表
    numbers = tuple(l)  #把列表装到一个元组中
    return numbers   #返回三个数字
x,y,z = func1(0,1,2)   #解包到3个变量中
print(x,y,z)  
#上面的numbers 还可以用：a,b,c三个变量来替代

print("**************************************************************")
#多个return 语句
def func2(x):
    if x > 0:
        return "x > 0"
    elif x == 0:
        return "x = 0"
    else:
        return "x < 0"
print(func2(-3))
print(func2(0))
print(func2(2))
print("**************************************************************")

#精简上面代码
def func3(x):
    if x > 0:
        result = "x > 0"
    elif x == 0:
        result = "x == 0"
    else:
        result = "x < 0"
    return result
print(func3(1))
print(func3(0))
print(func3(-3))





















