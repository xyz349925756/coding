#!/usr/bin/python
#-*-coding:utf-8-*-
"""if ...else..."""
"""
i = int(input("请输入一个数字："))
a = 0

if i == a:
    print("你输入了:",i)
else:
    print("你输入了一个正数") if i > 0 else print("你输入了一个负数")

print("你输入了0") if i == 0 else print("你输入了一个正数") if i > 0 else print("你输入了一个负数")
 """   

def num():
     print("你猜对了！") if i == secret else print("输入数值小了") if i < secret else print("输入数值大了")
     