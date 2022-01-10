#！ /usr/bin/python
##################################################################
#				递归函数					#			
##################################################################
"""
递归函数可以在函数主体内直接或间接的调用自己，即函数的嵌套是函数本身
"""
def refunc(n):
    i = 1
    if n > 1:
        i = n
        n = n * refunc(n - 1)
        print("%d! ="%i,n)
    return n

print("\n")
refunc(5)
# refunc(100)  太大了这数值。
"""一般不要使用递归，需要很多存储空间，如要要实行阶乘使用reduce（）"""
print("\n")

from functools import reduce
print("*5! =",reduce(lambda x,y:x * y,range(1,6)))
