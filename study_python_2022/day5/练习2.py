#!/usr/bin/python3
# -*-coding:utf-8-*-
# Time    :{DAY_NAME_FULL}
# Author  :xyz34
# Email   :xyz349925756@hotmail.com
# File    :练习2
# Project :coding
# 99乘法口诀表

# def nineNine():
#     for i in range(1,10):
#         for j in range(1,i+1):
#             print(" %d * %d = %2d  " % (i,j,i*j),end="")
#         print("")
#
# nineNine()

# 100-200 里面所有的素数
# l = []
# def primeNumber():
#     for i in range(100,200):
#         for n in range(2,i):
#             if i % n == 0:
#                 break
#         else:
#             l.append(i)
#     print("合计：%d 个素数！\n" % len(l),"它们是：",l)
# primeNumber()

# 判断输入的年份是不是闰年
year = int(input("请输入你所查询的年份>>> "))
def years():
    if year % 100 == 0:
        print("这是世纪年份")
        if year % 400 ==0:
            print("%d 是闰年" % year)
        else:
            print("%d 不是闰年" % year)
    else:
        if ((year % 4 == 0) and (year % 100 != 0)):
            # if ((year % 4 == 0) and (year % 100 != 0)):
            print("%d 是闰年" % year)
        else:
            print("%d 不是闰年" % year)
years()