#!/usr/bin/python3
# -*-coding:utf-8-*-
# Auth: xyz34
# File: 多继承.py
# TIME: 2022/5/14 周六
class A:

    def printA(self):
        print("A".center(40,"-"))

class B:

    def printB(self):
        print("B".center(40,"-"))

class C(A,B):

    def printC(self):
        print("C".center(40,"-"))


obj_C = C()

obj_C.printA()

obj_C.printB()

obj_C.printC()