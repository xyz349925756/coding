#!/usr/bin/python
#-*-coding:utf-8-*-
"""
函数
"""
from math import atan2

def myFirstFunction():
    print("这是第一个函数！")
    print("学习简单的函数！")    
#myFirstFunction()   #调用这个函数
for i in range(3):
    myFirstFunction()
    
def mySecondFunction(name):
    print(name + " python")
mySecondFunction("i love")

mySecondFunction("1")

mySecondFunction("s")

"""多个函数参数"""

def add(num1,num2):
    s = num1 + num2
    print("s =",s)
add(1,2)

def add1(n1,n2):
    return n1 + n2
print("add1 =",add1(3,4))
