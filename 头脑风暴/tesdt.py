#!/usr/bin/python3
# -*-coding:utf-8-*-
"""
@author:vking
@software: PyCharm
@file: tesdt.py
@time: 2017/8/20 21:08
"""
for a in range(1, 10):
    for b in range(1, a + 1):
        print("\033[0;31m %d * %d = %2d \033[0m" % (a, b, a * b), end=" ")
    print(" ")
