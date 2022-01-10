#！ /usr/bin/python
##################################################################
#				lambda函数				#			
##################################################################
"""
lambda函数用于创建一个匿名函数，函数名没有和标识符绑定。使用lambda函数可以返回一些简单的
运算结果
lambda 变量1，变量2......:表达式

#赋值
func = lambda 变量1，变量2......：表达式
#调用
func()
lambda也称为表达式，lambda只能使用表达式，不能使用判断，循环等多重语句
"""
def func():
    x = 1
    y = 2
    m = 3
    n = 4
    sum = lambda x,y:x+y
    print(sum)
    sub = lambda m,n:m - n
    print(sub)
    return sum(x,y) * sub(m,n)
print(func(),"\n")

#把lambda直接作为函数使用
print((lambda x:-x)(-2))
"""lambdax:-x 是定义了一个匿名函数，-2是赋值"""
