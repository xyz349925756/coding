#!/usr/bin/python3
# -*-coding:utf-8-*-
# Auth: xyz34
# File: 1.py
# TIME: 2022/5/7 周六

# class Car:
#     # 行驶
#     def move(self):
#         print("正在行驶...")
#
#     # 鸣笛
#     def toot(self):
#         print("嘀嘀嘀...")
#
# # 创建一个对象，并用变量CQ来保存它的引用
# CQ = Car()
# CQ.color = '白色'
# CQ.wheelNum = 4
# CQ.move()
# CQ.toot()
# print(CQ.color)
# print(CQ.wheelNum)
#
# AD = Car()
# AD.color = '黑色'
# AD.wheelNum = 5
# AD.move()
# AD.toot()
# print(AD.color)
# print(AD.wheelNum)

# def regedit(name,age,country):
#     """
#     注册信息
#     :param name: str
#     :param age:  int
#     :param country:   str
#     :return:
#     """

# def get_abs(n):
#     if n < 0:
#         n = int(str(n).strip("-"))
#     return n
#
# def add(x,y,f):
#     return f(x) + f(y)
#
# re = add(3,-7,get_abs)
# print(re)

# name = "嵌套函数"
#
# def change():
#     name = "嵌套函数中的局部变量"
#     def change2():
#         name = "函数中的函数中的局部变量"
#         print("第三个name,函数中的函数")
#     change2()
#     print("第二层 函数中的name")
# change()
# print("没有经过函数")

# c = lambda x,y:x**y
# print(c(2,3))
# def calc(x):
#     return  x ** 2

# c = map(lambda x:x**2 if x > 10 else x**3,[1,3,4,6,9,12])
# for i in c:
#     print(i)

# def ab(x,y):
#     if x > 1:
#         return x ** y
#     else:
#         return x + y
#
# print(ab(2,4))
# print(ab(0,2))
#
#
# c = lambda x,y:x**y if x>1 else x+y
# print(c(2,4))
# print(c(0,2))

# 求任意两数与2的余数之和

# def remainder(a):
#     return a % 2
#
# def sum(x,y,f):
#     return f(x) + f(y)
#
# re = sum(3,7,remainder)
# print(re)

# def calc(n):
#     print(n)
#     n = int(n/2)
#     if n>0:
#         calc(n)
#
# calc(100)

# 2分法查找某个数字位置 [1,2,4,6,9,11,12,15,17,22,35,41,53,57,69,77,102]
# l = [1,2,4,6,9,11,12,15,17,22,35,41,53,57,69,77,102]
#
# def e2(n):
#     x = int(len(l)/2)
#     # print(x)
#     if n > x:
#         print(l[x:])
#         print(l.index(n))
#     else:
#         print(l[:n])
#         print(l.index(n))
#
#
# e2(35)
# e2(4)

# def outer():
#     name = "闭包"
#
#     def inter():
#         print("里面")
#     return inter   #
# f = outer()
# f()
# a = []
# for i in range(10):
#     a.append(i)
# print(a)
#
# a = [i+1 for i in a]
# print(a)

# g = (x**2 for x in range(10))
# for i in g:
#     print(i)

#斐波那契数列
# 1 1 2 3 5 8 13 21 34....

# def f_B():
#     a = 1
#     b = 1
#     count = 0
#     l=[1,1]
#     while  count < 20:
#         tmp = a
#         a = b
#         b = tmp + b
#         count += 1
#         yield b
#     #     l.append(b)
#     # yield l
#
# f = f_B()
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))

# def g_test():
#     while True:
#         n = yield
#         print("返回函数内",n)
# g = g_test()
# g.__next__()  # 第一次不能为空，这里使用next给他跳过
#
# for i in range(10):
#     g.send(i)   # 把这个值发送给函数里面的n



