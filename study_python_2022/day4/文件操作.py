#!/usr/bin/python3
# -*-coding:utf-8-*-
# Time    :2022/1/17  14:06
# Author  :xyz34
# Email   :xyz349925756@hotmail.com
# File    :文件操作.py
# Project :coding

#创建文件
# f = open(file='./file/1.txt',mode='w')  #以写入权限写入
# f.write("my name is xxxx")
# # f.read()    #这里不能读取了
# f.close()

# 只读文件
f = open(file='./file/1.txt',mode='r')
print(f.read())
print(f.readline())  #逐行读取
f.close()

#追加
# f = open(file='./file/1.txt',mode='a')
# f.write("我是一个野生程序员\n")
# f.write("hello ,world!\n")
# f.close()