#！ /usr/bin/python
##################################################################
#			yield和return 的区别				#			
##################################################################
def func(n):
    for i in range(n):
        return i   #直接返回i的值，循环结束
def func2(n):
    for i in range(n):
        yield i  #循环生成n个数字，语句不会被终止

print(func(3),"\n")  # 结果为0
f = func2(3)
print(f,"\n")  #返回了 函数func2()的地址
print(f.next()) #yield没有返回值.
print(f.next())
