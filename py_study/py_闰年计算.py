#!/usr/bin/python
#-*-coding:utf-8-*-
"""闰年计算,年份能被4整除；年份能被100整除而不被400整除的年份是平年。"""
i = input("请输入年份:")
if i.isdigit() == True:
    s = int(i)
    if s % 4 ==0:
        s % 100 != 0
        if s % 400 == 0:
            print("是闰年")
        else:
            print("%d 不是闰年"%s)    
    else:
        print("%d 不是闰年"%s)
else:
    print("你输入的不是数字类型，程序终止！")