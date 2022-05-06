#!/usr/bin/python3
# -*-coding:utf-8-*-
# Time    :2022/1/1412:56
# Author  :xyz34
# Email   :xyz349925756@hotmail.com
# File    :列表lis-t.py
# Project :coding

# lis = [] #定义一个空列表
# for i in range(10):
#     lis.append(i)
# print(lis,len(lis))
#
# lis.insert(2,3)
# print(lis)
#
# lis1 = []
# for i in 'abcdefghijklmnopqrstuvwxyz':
#     lis1.append(i)
# print(lis1,len(lis1))
#
# lis2 = ['a','b','c','d']
# lis3 = ['1','2','3']
# lis2.extend(lis3)
# print(lis2,lis3)
#
# lis2.insert(2,['e','f'])   #列表嵌套
# print(lis2)
#
# del lis[2]
# print(lis)
#
# print(lis2.pop(2))
# print(lis2)
# lis2.remove('1')
# print(lis2)
# lis4 = lis2.copy()
# print(lis4)
# print(lis2.count('c'))
# lis2.clear()
# print(lis2)
# lis4[0] = 'A'
# print(lis4)
# lis4[-1]='4'
# print(lis4)
#
# print(lis4.index('2'),lis4.count('2'))
#
# #不知道一个元素在列表的那个位置，怎么取修改，先判断是否在列表，然后查找索引位置，再去修改即可
# print('b' in lis4)
# print(lis4.index('b'))
# lis4[1] = 'B'
# print(lis4)
#
# print(lis4[0::2])
# lis4.sort()  #正序
# print(lis4)
# lis4.reverse()   #倒序
# print(lis4)
# for i in lis4:   #循环
#     print(i)
#
# for i in enumerate(lis4):  #打印索引
#      print(i[0],i[1])

# names = ['zhangsan','lisi','wangwu']
# b = ['1','2','3','4']
# print(type(names),names)
# names.append('husan')
# print(names)
# names.extend(b)
# print(names)
# b.extend(names)
# print(b)
# b.insert(1,'1.3')
# b[1]='4'
# print(b)
# print(6 not in b)
# print(names.index('lisi'))
# print(b.index('1',1,3))
# print(b)
# print("字符串'4'在b 中有%d个; " % b.count('4') , "数字4在b中有%d个"%b.count(4))
# print("之前",b)
# del b[0]
# b.pop(1)
# print(b)
# b.remove('4')
# print("删除之后",b)
# b.reverse()
# b.clear()
# b.sort()
# print(b)

# 一个学校，有3个办公室，现在有8位老师等待工位的分配，请编写程序，完成随机的分配

# 3个办公室就是三个列表，不考虑里面有几个办公位
import random
office_room = [[],[],[]]
names = ['a','b','c','d','e','f','g','h']

# 遍历所有老师，并把遍历出来的老师，随机分配到一个办公室
# for n in names:
#     index = random.randint(0,2)   # 随机索引
#     office_room[index].append(n)  # 添加老师到列表
#     # print(index)
# # print(office_room)
# for i in range(1,4):
#     # print(i)
#     print("办公室%d有:%d 位老师,他们是: %s" % (i,len(office_room[i-1]),office_room[i-1]))
#     print("-"*50)

# for i in names:
#     print(i)

i = 0
while i <= len(names):
    print(names[i])
    i += 1
