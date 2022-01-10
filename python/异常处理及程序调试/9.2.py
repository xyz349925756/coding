#！/usr/bin/python
# -*- coding:utf-8 -*-
try:
    s = "hello"
    try:
        print(s[0]+s[1])
        print(s[0]-s[1])
    except TypeError:
        print("字符串不支持减法运算")
except:
    print("异常")