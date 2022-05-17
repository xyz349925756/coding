#!/usr/bin/python3
# -*-coding:utf-8-*-
# Auth: xyz34
# File: self.py
# TIME: 2022/5/8 周日

class Animal:

    def __init__(self,name):
        self.name = name

    def printName(self):
        print("名字为: %s"%self.name)

def myPrint(animal):
    animal.printName()

dog1 = Animal("旺财-习近平")
myPrint(dog1)

dog2 = Animal("旺财-毛泽东")
myPrint(dog2)