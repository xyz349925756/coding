#!/usr/bin/python
#-*-coding:utf-8-*-
bingo = "hello,world!"
answer = input("请输入猜想的一句话：")
while True:
    if answer == bingo:
        break
    answer = input("抱歉，输入错误，重新输入：")
print("OK")