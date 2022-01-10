#!/usr/bin/python
#-*-coding:utf-8-*-
s =int(input("请输入一个分数:"))
print("A") if 100 >= s >= 90  else print("B") if 90 > s >= 80 else print("C") if 80 > s >= 60 else print("D") if 60 > s >= 0 else print("输入错误!") 