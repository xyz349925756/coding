#!/usr/bin/python
#-*-coding:utf-8-*-
"""
在之前的小游戏中，用户只能输入数字，输入其他则报错。
"""
import random
num = random.randint(1,10)
i = input("请输入您猜想的数字：")
if i.isdigit() == True:
    s = int(i)
    count = 0
    t = 3
    print("你猜对了") if s == num else print("输入数值小了") if s < num else print("输入数值大了")
    while count < t and s != num:
        i = input("请重新输入：")
        if i.isdigit() == True:
            s = int(i)
            count += 1
            print("恭喜您！") if  s ==num  else print("您只有【 ",t - count," 】次机会")
            print("你猜对了！") if s == num else print("输入数值小了") if s < num else print("输入数值大了")
        else:
            print("输入类型错误！")
            break
else:
    print("输入类型错误！")
   

    

        