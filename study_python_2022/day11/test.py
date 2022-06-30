#!/usr/bin/python3
# -*-coding:utf-8-*-
# Auth: xyz34
# File: test.py
# TIME: 2022/6/27 星期一  周一


class Parent:  # 定义父类
    parentAttr = 100

    def __init__(self):
        print("调用父类构造函数")

    def parentMethod(self):
        print('调用父类方法')

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print("父类属性 :", Parent.parentAttr)


class Child(Parent):  # 定义子类
    def __init__(self):
        print("调用子类构造方法")

    def childMethod(self):
        print('调用子类方法')

print(Child.mro())  # mro是python多继承情况，运行时搜索方法的顺序规则
print("".center(50,"-"))

c = Child()  # 实例化子类
c.childMethod()  # 调用子类的方法

print("".center(30,"-"))

c.parentMethod()  # 调用父类方法
c.setAttr(200)  # 再次调用父类的方法 - 设置属性值
c.getAttr()  # 再次调用父类的方法 - 获取属性值