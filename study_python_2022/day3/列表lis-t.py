#!/usr/bin/python3
# -*-coding:utf-8-*-
# Time    :2022/1/1412:56
# Author  :xyz34
# Email   :xyz349925756@hotmail.com
# File    :列表lis-t.py
# Project :coding

lis = [] #定义一个空列表
for i in range(10):
    lis.append(i)
print(lis,len(lis))

lis.insert(2,3)
print(lis)

lis1 = []
for i in 'abcdefghijklmnopqrstuvwxyz':
    lis1.append(i)
print(lis1,len(lis1))

lis2 = ['a','b','c','d']
lis3 = ['1','2','3']
lis2.extend(lis3)
print(lis2,lis3)

lis2.insert(2,['e','f'])   #列表嵌套
print(lis2)

del lis[2]
print(lis)

print(lis2.pop(2))
print(lis2)
lis2.remove('1')
print(lis2)
lis4 = lis2.copy()
print(lis4)
print(lis2.count('c'))
lis2.clear()
print(lis2)
lis4[0] = 'A'
print(lis4)
lis4[-1]='4'
print(lis4)

print(lis4.index('2'),lis4.count('2'))

#不知道一个元素在列表的那个位置，怎么取修改，先判断是否在列表，然后查找索引位置，再去修改即可
print('b' in lis4)
print(lis4.index('b'))
lis4[1] = 'B'
print(lis4)

print(lis4[0::2])
lis4.sort()  #正序
print(lis4)
lis4.reverse()   #倒序
print(lis4)
for i in lis4:   #循环
    print(i)

for i in enumerate(lis4):  #打印索引
     print(i[0],i[1])

