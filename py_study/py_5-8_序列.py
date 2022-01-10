#!/usr/bin/python
#-*-coding:utf-8-*-
"""
序列
"""
a = list()
b = list("Ilovepython!")
print("将字符串迭代放到列表中\na = ",b)
c = list((1,2,3,4,5,6,7,8,9))
print("将元组迭代放到列表中\nc =",c)
d = tuple(b)
print("把一个可迭代的对象转为元组：\nb =",d)
e = str(b)
print("用于把obj对象转换为字符串：\nb=",e)
print("返回sub的长度:\nb =",len(b))

list = [1,2,-45,67,99,222,45]
print("返回最大值\nlist =",max(list))
list1 = [1,2,3,4,5,6,7,3,4,5,6,89,2,66]
print("返回最大值\nlist =",max(list1))
print("返回最大值\nlist =",max(b))
print("返回最大值\nlist =",min(list1))
print("返回最大值\nlist =",min(b))
tuple = 1,2,3,4,5,6,7,8,9,10
print("求序列的总和\n sum =",sum(tuple))
print("求序列的总和\n sum =",sum(tuple,10)) #添加默认从指定参数开始加起。意思就是sum+该参数
list2 = list[ : ]
list.sort()
print("sort序列 ：",list)
print("sorted list2 =",sorted(list2))
print("list2 =",list2)
for i in reversed(list):
    print(i,end = " ")

print("生成一个二元组\nenumerate :")
for i in enumerate(b):
    print(i)

print("zip")
for i in zip(list,b):
    print(i)

s = [1,2,3,4,5,6,7,8,9,0,1,2]
str = "ilovepython!"
tuple = (2,3,4,5,6,7,8,9,0,1,2,3)
for i in zip(s,str,tuple):
    print(i)







