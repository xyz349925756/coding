#!/usr/bin/python3
# -*-coding:utf-8-*-
# Auth: xyz34
# File: 重写.py
# TIME: 2022/5/14 周六

# class Cat(object):
#
#     def sayHello(self):
#         print("hello -A".center(60,"-"))
#
# class Bosi(Cat):
#     def sayHello(self):
#         print("hello -B".center(60,"-"))
#
# bosi = Bosi()
#
# bosi.sayHello()

# class Cat(object):
#
#     def __init__(self,name):
#         self.name = name
#         self.color = "yellow"
#
# class Bosi(Cat):
#
#     def __init__(self,name):
#         # Cat.__init__(self,name)
#
#         # super(Bosi, self).__init__(name)
#
#         super().__init__(name)
#
#     def getName(self):
#         return self.name
#
#
# bosi = Bosi('xxx')
#
# print(bosi.name)
# print(bosi.color)


# 多态


class F1(object):
    def show(self):
        print(F1.show)

class S1(F1):
    def show(self):
        print(S1.show)

class S2(F1):
    def show(self):
        print(S2.show)

def Func(obj):
    print(obj.show())

s1_obj = S1()
Func(s1_obj)


s2_obj = S2()
Func(s2_obj)