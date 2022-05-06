#!/usr/bin/python3
# -*-coding:utf-8-*-
# Time    :{DAY_NAME_FULL}
# Author  :xyz34
# Email   :xyz349925756@hotmail.com
# File    :练习
# Project :coding

# 1-100的累计和

# i = 1
# sum = 0
# while i<=100:
#     sum += i
#     i += 1
# print("1-100的累计和为：%d" % sum)

# 求1-100 之间偶数的累计和
# i = 1
# sum = 0
# while i<=100:
#     if i % 2 == 0:
#         sum += i
#     i += 1
# print("1-100偶数的累计和为：%d" % sum)

# 1-100 奇数的累计和
# i = 1
# sum = 0
# while i<=100:
#     if i % 2 == 1:
#         sum += i
#     i += 1
# print("1-100 奇数累计和为：%d" % sum)

# 打印大三角形
# i = 1
# while i <= 10:
#     if i <= 5:
#         print("*"*i)
#     else:
#         print("*"*(10-i))
#     i += 1

# i = 1
# while i <= 5:
#     j = 1
#     while j <= i:
#         print("*",end="")
#         j += 1
#     print("")
#     i += 1

# i = 5
# while i >= 1:
#     j = i
#     while j >= 1 :
#         print("*",end="")
#         j -= 1
#     print("")
#     i -= 1

# i = 1
# while i <= 9:
#     j = 1
#     while j <= i:
#         print("%d x %d=%2d  " % (i,j,i*j),end="  ")
#         j += 1
#     print("")
#     i += 1

# for i in range(10):
#     for j in range(1,i+1):
#         print(" %d x %d = %2d " % (i,j,i*j),end=" ")
#     print("")

# string
s = "cloudb.pub123"

# print(s.find('pub'))
# print(s.find('o',0,-1))
# print(s.rindex('p',0,len(s)))
print(s[0:6])
# print(s[0::2])
print(s[::-1])  #反转字符串