#!/usr/bin/python3
# -*-coding:utf-8-*-
# Auth: xyz34
# File: 递归.py
# TIME: 5月  星期二
#
# def f1():
#     print("111")
#     print("222")
#     print("".center(30,"-"))
#     f1()
# f1()

# 递归应用 提取下面元素
# l = [1,[2,[3,[4,[5,[6,[7,8,9,[10,[11]]]]]]]]]
#
# def re_func(list1):
#     for item in list1:
#         if type(item) is list:
#             """if item is list,need for"""
#             re_func(item)
#         else:
#             print(item)
#
# re_func(l)

# l = [1,2,4,6,9,11,12,15,17,22,35,41,53,57,69,77,102]
# l1 = l.sort()

# def binary_search(input_num,new_l):
#     mid_num = int(len(new_l) / 2)  # len(new_l) // 2 整除
#     print(mid_num)
#     print(new_l)
#     if input_num > new_l[-1]:
#         print("您需要找的值%d大于列表最大值"%input_num)
#         if  input_num not in new_l:
#             print("Error ,%d is not in list"%input_num)
#             return 3
#         return 2
#     elif input_num < new_l[0]:
#         print("你查找的数值%d小于范围的最小值"%input_num)
#         return 1
#
#     if input_num > new_l[mid_num]:
#         # print("在列表的右边")
#         new_l = new_l[mid_num:]
#         # print(new_l)
#         binary_search(input_num,new_l)
#     elif input_num < new_l[mid_num]:
#         # print("在列表的左边")
#         new_l = new_l[:mid_num]
#         # print(new_l)
#         binary_search(input_num, new_l)
#     else:
#         print("Find It")
#
# def p():
#     print("".center(60,"-"))
#
# binary_search(22,l)
# p()
# binary_search(35,l)
# p()
# binary_search(999,l)
# p()
# binary_search(-3,l)
# p()
# binary_search(102,l)
# p()

# d = {
#     '张三':5000,
#     '李四':7000,
#     '王五':9000,
#     '小七':3500
# }
#
# res = max(d,key=lambda k:d[k])
# print(res)
#
# l = ['alex_dsb','jack','bob_dsb','deal']
# # res = map(lambda name:name+'_dsb',l)
# # print(res.__next__())
# # print(res.__next__())
# # print(res.__next__())
# # print(res.__next__())
# # res = [name for name in l if name.endswith("_dsb")]
# res = filter(lambda name:name.endswitch('_dsb'),l)
# # print(type(res))
# # print(res)
# print(res.__iter__())

# def f(x):
#     return x % 2 == 0
# l = [1,3,4,5,6,9]
#
# res = filter(f,[1,2,3,4,6])
# print(res)
# res1 = list(res)
# print(res1)

# import math
# def is_sqr(x):
#     return math.sqrt(x) % 1 == 0
#
# tmpl = filter(is_sqr,range(1,101))
# l1 = list(tmpl)
# print(l1)


# l = [1,3,5,8,9]
# res = filter(lambda i:i%2==1,l)
# print(res)
# print(list(res))

# 过滤1-100以内的偶数
# res=filter(lambda i:i%2==0,range(1,100))
# # print(list(res))
# l = list(res)
#
# from functools import reduce
# sums = reduce(lambda x,y:x+y,l)
# print(sums)
#
# sum1 = reduce(lambda x,y:x*y,[1,2,3,4])
# print(sum1)
#
# sum2 = reduce(lambda x,y:x+y,range(1,101))
# print(sum2)
#
# str = reduce(lambda x,y:x+y,['a','b','1','c','d'])
# print(str)

# a = [1,5,3,4,7,9,2]
# print(sorted(a))

# d = {
#     '张三':5000,
#     '李四':7000,
#     '王五':9000,
#     '小七':3500
# }
#
# print(sorted(d.items(),reverse=True))

chars=[
    'https://github.com',
    'http://cloudb.pub',
    'taobao.com',
    'https://www.52pojie.com'
]
print(sorted(chars,key=lambda x:len(x)))