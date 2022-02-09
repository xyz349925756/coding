#!/usr/bin/python3
# -*-coding:utf-8-*-
# Time    :2022/1/19  23:33
# Author  :xyz34
# Email   :xyz349925756@hotmail.com
# File    :内置函数.py
# Project :coding

#https://docs.python.org/zh-cn/3/library/functions.html
# print(abs(-5))   #绝对值
# print(all([1,2,3,4]))
# print(all((1,)))
# print(all(()))
# print(all([]))      #判断迭代参数中的所有元素是否为true，除 0 null none false 其他都是true
# print(all((0,1,2,3,4,5)))  #包含0
# print(all(['a','','b']))   #有空字符
# print(any([]))       #判断里面是否有元素，如果是没有则返回False
# print(any(()))
# print(any((1,2,0)))   #判断里面是否有元素，有就是true
# print(any(['a','']))

# print(ascii('中国'),ascii('zhong'))  #如果参数中有非ascii字符，会用 \u,\U,\x 来替代
# print(bin(128))  #转成二进制
# print(type(bin(128)))
# print(bin(128)[2:])  #去除前面的0b

# print(bool(),bool(2>1),bool('a' in 'abc'),bool(0),bool(1),bool(()),bool([]))
#bool值，0，空为false，判断条件，判断列表，元组里面是否有元素

# print(breakpoint()) #调试函数
# print(bytearray(255))  #返回一个可变序列
# print(bytes(1)) #返回一个不可变序列
# def __call__ ():
#     print('a')
# b = 2
# print(callable(__call__()),callable(b)) #返回参数是否可以调用,可以调用返回true

# print(chr(97),chr(65)) #返回ascii编码表对应的值
# class A(object):
#     n = 10
#     def func1(self):
#         print(self)
#     @classmethod     #一直不明白
#     def func2(cls):
#         print(f'func2',cls.n)
#         cls().func1()
# A.func2()