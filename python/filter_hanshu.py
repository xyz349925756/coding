#！ /usr/bin/python
##################################################################
#			 模块的内置函数					#			
##################################################################

def func(x):
    if x > 0:
        return x

print(filter(func,range(-9,10)))
print(list(filter(func,range(-9,10))))


"""
filter()可以对某个序列做 过滤处理，判断自定义函数的参数返回结果是否为真来过滤，并一次性的返回处理结果
。
"""
