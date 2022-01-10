#!/usr/bin/python
#-*-coding:utf-8-*-
"""格式化字符串"""
print("{0} love {1}.{2}".format("I","you","too")) #位置参数
print("{a} love {b}".format(a = "i",b = "you")) #关键参数
print("{0} love {a}.{b}".format("i",a = "cloudb",b = "pub")) #当关键参数和位置参数一起使用的时候位置参数优先。
print("{{0}}".format("aaaa")) #这里打印的是{0}  因为被{} 转义了类似“\”
print("{0}".format("aaaa"))
print("{0} : {1:.2f}".format("圆周率",3.1415926))
