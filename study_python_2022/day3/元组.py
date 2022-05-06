#!/usr/bin/python3
# -*-coding:utf-8-*-
# Time    :2022/1/15  21:51
# Author  :xyz34
# Email   :xyz349925756@hotmail.com
# File    :元组.py
# Project :coding

#元组只读，查
# tu1 = (1,2,3)
# tu2 = (1,2,3,4,)
# print(tu1,tu2)
#
# tu3 = ([1,2])
# tu4 = ([1],)
# print(tu3,type(tu3),tu4,type(tu4))
#
# print(tu1[0],tu1[0:],tu1[-3:-1])

t1 = (1,'wangwu','26','云南','云南')
# print(type(t1),t1)
#
# print(t1[1])
#
# for i in range(len(t1)):
#     print(t1[i])
#
# t1[2] = 32  #不能修改，不能写入
# print(t1)

print(t1.index('26'))
print(t1.count('云南'))