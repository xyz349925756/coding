#!/usr/bin/python3
# -*-coding:utf-8-*-
# Time    :2022/1/1423:36
# Author  :xyz34
# Email   :xyz349925756@hotmail.com
# File    :test.py
# Project :coding
#coding=utf-8
list=[]
for i in range(1,101):
    list.append(i)

# print(list)

tempList=[]
newList=[]

while True:
    num=0
    for temp in list:
        tempList.append(temp)
        num+=1
        if num==3:
            newList.append(tempList)
            tempList=[]
            num=0
            continue
    if temp==100:
        newList.append(tempList)
        break

print(newList)