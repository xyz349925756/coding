#！/usr/bin/python
# -*- coding:utf-8 -*-
#使用raise抛出异常
try:
    s = None
    if s in None:
        print("s是空对象")
        raise NameError
    print(len(s))
except TypeError:
    print("空对象没有长度")