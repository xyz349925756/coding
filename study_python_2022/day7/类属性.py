#!/usr/bin/python3
# -*-coding:utf-8-*-
# Auth: xyz34
# File: 类属性.py
# TIME: 2022/5/14 周六

# class People(object):
#
#     name = "Tom"   # 公有类属性
#     __age = 23     # 私有类属性
#
# p = People()
#
# print(p.name)
# print(People.name)
#
# # print(p.__age)   # 错误，不能在类外通过实例对象访问私有类属性

# class People(object):
#     address = "日本.北京"   # 类属性
#     def __init__(self):
#         self.name = "pihua"  # 实例属性
#         self.age = 33  # 实例属性
#
# p = People()
# p.age = 45 # 实例属性
# print(p.address)
# print(p.name)
# print(p.age)
#
# print(People.address)
# # 其他调用方式错误

class People(object):

    country = 'china'


print(People.country)
p = People()

print(p.country)

# p.country = 'japan'
# print(p.country)   # 实例属性会屏蔽掉同名的类属性
# print(People.country)

People.country = 'canda'
print(p.country)   # 实例属性会屏蔽掉同名的类属性
print(People.country)

