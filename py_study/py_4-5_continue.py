#!/usr/bin/python
#-*-coding:utf-8-*-
for i in range(10):
    if i % 2 != 0:
        print("i =",i,end="\n")
        continue
    i += 2
    print("i =",i,end="\n ")

"""
for i in range(1,10):
    if i % 2 == 0:
        print(i,end=" ")
        continue
    i += 2
"""