#!/usr/bin/python
#-*-coding:utf-8-*-
"""元组"""

tuple1 = (1,2,3,4,5)
print("tuple1 =",tuple1)
tuple1 = tuple1[:2] + (6,) + tuple1[2:]
print("tuple1 =",tuple1)