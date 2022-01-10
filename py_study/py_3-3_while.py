#!/usr/bin/python
#-*-coding:utf-8-*-
"""while"""
i = int(input("请输入一个数字："))
count = 0
t = 3
while count < t and i != 0:
    i = int(input("请重新输入："))
    count += 1
    print("你还有",t - count,"次机会")
    print("你输入了0")  if i == 0 else print("你输入了一个正数") if i > 0 else print("你输入了一个负数")

    