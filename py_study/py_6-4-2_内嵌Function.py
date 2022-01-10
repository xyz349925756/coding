#!/usr/bin/python
#-*-coding:utf-8-*-
'''
Created on 2016年12月18日
@author: linux
'''
def firstFunction():
    count = 5
    def secondFunction():
        count = 10
        print("secondFunction = ",count)
    secondFunction()
    print("firstFunction = ",count)
firstFunction()

"""closure"""
def firstFunction(x):
     def secondFunction(y):
         return x * y
     return secondFunction
i = firstFunction(5) 
print("调用单个函数",i(8)) 
print("调用上面的函数",firstFunction(5)(8))


def funx():
    x = [5]
    def funy():
        x[0] *= x[0]
        return x[0]
    return funy 
print(funx()())


def funx():
    x = 5
    def funy():
        nonlocal x  #修改外部函数的局部变量的值。
        x *= x 
        return x
    return funy 
print(funx()())