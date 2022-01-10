#！/usr/bin/python
# -*- coding:utf-8 -*-
try:
    open("hello.txt","r")
    print("读文件")
except FileNotFoundError:
    print("文件不存在")
except:
    print("程序异常")


try:
    result = 10 / 0
except ZeroDivisionError:
    print("0不能被整除")
else:
    print(result)