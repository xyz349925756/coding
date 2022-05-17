#!/usr/bin/python3
# -*-coding:utf-8-*-
# Auth: xyz34
# File: 1__new__.py
# TIME: 2022/5/14 周六

class A(object):
    def __init__(self):
        print("这是init方法")

    def __new__(cls, *args, **kwargs):
        print("这是new方法")
        return object.__new__(cls)

A()