#!/usr/bin/python3
# -*-coding:utf-8-*-
# Auth: xyz34
# File: 1__del__.py
# TIME: 2022/5/14 周六

import time

class Animal(object):

    # 初始化方法
    # 创建完对象后会自动被调用
    def __init__(self,name):
        print("__init__方法被调用")
        self.__name = name

    def __del__(self):
        print("__del__方法被调用")
        print("%s对象马上被删除了" % self.__name)


dog = Animal("沙皮")

del dog

cat = Animal("非洲猫")
cat2 = cat
cat3 = cat

print("删除cat3对象".center(60, "-"))
del cat3

print("删除cat2对象".center(60, "-"))
del cat2

print("删除cat对象".center(60, "-"))
del cat

print("程序2秒钟后结束")
time.sleep(5)
