#!/usr/bin/python3
# -*-coding:utf-8-*-
# Auth: xyz34
# File: 继承示例.py
# TIME: 2022/5/14 周六

class Cat(object):

    def __init__(self,name,color="red"):
        self.name = name
        self.color = color

    def run(self):
        print("%s  在跑"%self.name)

class Bosi(Cat):

    def setNewName(self,newName):
        self.name

    def eat(self):
        print("%s --在吃"%self.name)

bs = Bosi("加菲猫")

print("bs的名字为：%s"%bs.name)
print("bs的颜色为：%s"%bs.color)
bs.eat()
bs.setNewName('波斯')
bs.run()