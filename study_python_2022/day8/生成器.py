#!/usr/bin/python3
# -*-coding:utf-8-*-
# Auth: xyz34
# File: 生成器.py
# TIME: 5月  星期二

# def func(x):
#     yield x ** 2
#
#
# print(type(func(2)))
#
# for i in range(10):
#     print(func(i).__next__())

# for i in range(12):
#     f = i ** 2 if i < 6 else i ** 3
#     print(f)

# g = (x**2 for x in range(100) if x<5)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

# l = ['a_xxx','b','c_xxx','c','d_xxx']
# new_l = [i.split("_")[0] for i in l]
# print(new_l)
#
# new_l2 = [name.replace("_xxx","") for name in l]
# print(new_l2)

# d = {
#     'name':'张三',
#     'age':'66',
#     'job':'IT'
# }
#
# new_d = {key:value for key,value in d.items() if key != 'job'}
# print(new_d)

s = ['a_xxx','b','c_xxx','c','d_xxx']
new_s = {name.replace("_xxx","") for name in s}
print(new_s)
print(type(new_s))