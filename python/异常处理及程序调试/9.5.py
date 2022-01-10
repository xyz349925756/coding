#！/usr/bin/python
# -*- coding:utf-8 -*-
#自定义异常
from __future__ import division
class DivisionException(Exception):
    def __init__(self,x,y):
        Exception.__init__(self,x,y)
        self.x = x
        self.y = y
if __name__ == "__main__":
    try:
        x = 3
        y = 2
        if x % y > 0:
            print(x/y)
            raise DivisionException(x,y)
    except DivisionException as div:
        print("DivisionException:x / y = %.2f" % (div.x/div.y))