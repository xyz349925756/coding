#！ /usr/bin/python
##################################################################
#				Generator函数				#			
##################################################################
"""
生成器generator的作用是一次生产一个数据项，并输出
def 函数名(参数列表)：
      ...
      yield 表达式
"""
def func(n):
    for i in range(n):
        yield i  #yield关键字的返回值和return关键字d返回值和执行原理都不相同。
for i in func(4):
    print(i,"\n")

    
r = func(4)
print(r.next())
print(r.next())
print(r.next())
print(r.next())#这行数据是没有数据生成，所以会报错。



