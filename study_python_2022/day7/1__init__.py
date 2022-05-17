#!/usr/bin/python3
# -*-coding:utf-8-*-
# Auth: xyz34
# File: 1__init__.py
# TIME: 2022/5/8 周日

# class Car:
#
#     def __init__(self):
#         self.wheelNum = 4
#         self.color = '蓝色'
#
#     def move(self):
#         print("正在行驶...")
#
# CQ = Car()
#
# print('车的颜色: %s'%CQ.color)
# print('车轮数量: %d'%CQ.wheelNum)

# class Car:
#
#     def __init__(self,color,wheelNum):
#         self.color = color
#         self.wheelNum = wheelNum
#
#     def move(self):
#         print("正在行驶...")
#
# CQ = Car('蓝色',5)
#
# print("car color 颜色：%s " % CQ.color)
# print("wheelNum 有: %d 个" % CQ.wheelNum)

class Car:

    def __init__(self,color,wheelNum):
        self.color = color
        self.wheelNum = str(wheelNum)

    def __str__(self):
        msg = "这辆车的颜色是" + self.color + "他有" + self.wheelNum +"个轮胎，其中一个是备胎！"
        return msg

    def move(self):
        print("正在行驶...")

CQ = Car('block',5)
print(CQ)