#！ /usr/bin/python
##################################################################
#			map()的使用					#			
##################################################################
"""
map（功能强大）可以对多个序列的每个元素都执行相同的操作，并返回一个map对象。
"""
def power(x):
    return x ** x
print(map(power,range(1,5)))    #打印map对象
print(list(map(power,range(1,5))))  #转换为列表输出

def power2(x,y):
    return x ** y
print(map(power2,range(1,5),range(5,1,-1)))  #打印map对象
print(list(map(power2,range(1,5),range(5,1,-1)))) #转化为列表输出

