#!/usr/bin/python3
# -*-coding:utf-8-*-
# Auth: xyz34
# File: 异常.py
# TIME: 5月  星期日

a = 1
b = 'a'
c = 3
try:
    print(a+b)
    # raise
except TypeError as typeError:
    print("数据类型不一致，不能做运算！",typeError)
else:
    pass
