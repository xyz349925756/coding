#!/usr/bin/python3
# -*-coding:utf-8-*-
# Auth: xyz34
# File: 保护对象属性.py
# TIME: 2022/5/14 周六

class People(object):

    def __init__(self,name):
        self.__name = name

    def getName(self):
        return self.__name

    def setName(self,newName):
        if len(newName) >= 5:
            self.__name = newName
        else:
            print("错误：非中文名字！")

zhangsan = People("test")

zhangsan.setName("tests")
print(zhangsan.getName())

zhangsan.setName("lisi")
print(zhangsan.getName())