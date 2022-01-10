#!/usr/bin/python
#-*-coding:utf-8-*-
import random
secret = random.randint(1,9)
i = int(input("请输入一个你猜想的数字，回车继续："))
count = 0
t = 3
#print("i =",secret)
print("你猜对了") if i == secret else print("输入数值小了") if i < secret else print("输入数值大了")
while count < t and i != secret:
    i = int(input("请重新输入："))
    count += 1
    print("恭喜您！") if  i ==secret  else print("您还有",t - count,"次机会")
    print("你猜对了！") if i == secret else print("输入数值小了") if i < secret else print("输入数值大了")

    
    