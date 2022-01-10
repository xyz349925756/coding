#!/usr/bin/python

import mymodules
print("count = ",mymodules.func())
mymodules.count = 10
print("count = ",mymodules.count)

import mymodules
print("count = ",mymodules.func())


if mymodules.count > 1:
    mymodules.count = 1
else:
    import mymodules
print("count = ",mymodules.count)
#这里结果是1，因为上面的if 如果count >1 那么就重新赋值count =1
#所以这里是1
print("count = ",mymodules.func())
#这里是再次调用函数func() 所以自动+1了。结果为2.

"""导入模块module 查看count的结果
结果是：
count = 2   为什么这里会是2 ，因为count +=1 所以导入之后的mymodule已经执行了
一次运算即1 +1 =2
count = 10   这里是对count 赋值
count = 11    再次导入模块mymodule 这里又执行过count +=1
所以结果就是11
"""
