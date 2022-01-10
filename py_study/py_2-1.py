#!/usr/bin/python
#-*-coding:utf-8-*-

"""猜数字游戏"""
i =int(input("不妨猜想下小编心中所想的数字："))
if i == 6:
    print("对了")
else:
    print("错误")

i = int(input("请输入猜想的数字："))
print("你猜对了！") if i == 6 else print("你猜错了！")