# coding --utf-8--
# /usr/bin/python
"""数字排雷，选取指定的一个数字，然后让第一个玩家猜，猜中结束，猜错给出范围重新猜"""
import random
num = random.randint(1,101)
print("数字:",num)
while (num>0):
    A=int(input("请输入你猜测的数字:"))
    if (num > A ):
        print("范围：",A,100,"A")
        B = A
    elif (num < A):
        print("范围",B,A,"b")





