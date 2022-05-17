#!/usr/bin/python3
# -*-coding:utf-8-*-
# Auth: xyz34
# File: 类方法.py
# TIME: 2022/5/14 周六

# class People(object):
#     country = 'china'
#
#     @classmethod   #类方法用classmethod进行修饰
#     def getCountry(cls):
#         return cls.country
#
#     @classmethod
#     def setCountry(cls,country):
#         cls.country = country
#
# p = People()
# print(p.getCountry())    # 可以通过实例对象引用
# print(People.getCountry())   # 可以通过类对象引用
#
# p.setCountry('japan')
# print(p.getCountry())
# print(People.getCountry())


class People(object):
    country = 'china'

    @staticmethod
    def getCountry():
        return People.country

print(People.getCountry())
