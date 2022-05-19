#!/usr/bin/python3
# -*-coding:utf-8-*-
# Auth: xyz34
# File: 多线程.py
# TIME: 2022/5/17 周二


# 比赛吃包子

# def games(name):
#     print("参赛选手：%s"%name)
#     while True:
#         bun = yield
#         print("选手%s吃了%d个"%(name,bun))
#
# p1 = games("P1")
# p2 = games("P2")
# p3 = games("P3")
#
# p1.__next__()
# p2.__next__()
# p3.__next__()
#
# for i in range(10):
#     print("第%d次".center(60,"-")%i)
#     p1.send(i)
#     p2.send(i)
#     p3.send(i)

# from collections.abc import Iterable
# print(isinstance((i**2 for i in range(10)),Iterable))
# print(isinstance({},Iterable))
# print(isinstance((),Iterable))
# print(isinstance([],Iterable))

import sys,os,time
# for i in dir(sys):
#     print(i)
# print(os.path)
# print(sys.path)
# for i in sys.path:
#     print(i)

# print(os.path.split(__file__))
print(sys.platform)
print(time.time())  # 获取当前时间戳从1970-1-1 0：0：0开始

