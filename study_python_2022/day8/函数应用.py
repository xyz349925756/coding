#!/usr/bin/python3
# -*-coding:utf-8-*-
# Auth: xyz34
# File: 函数应用.py
# TIME: 5月  星期六

# 闭包

# def f1():
#     x = 9
#     def f2():
#         print("x的值是: %s"%x)
#     # return f2
#     f2()
# f1()
#

# def f1(a):
#     b = 5
#     def f2(c):
#         return c ** a + b
#     return f2
#
# f1(2)
# print(f1(2))
# f = f1(2)
# print(f(3))


# def f1(a):
#     b = a
#     def f2(l):
#         nonlocal b
#         b += 1
#         print(l,b)
#     return f2
#
# f1(1)
# print(f1(1))
#
# f = f1(1)
# f('第一次调用的结果是：')
# f('第二次调用的结果是：')
# f('第三次调用的结果是：')
#
# g = f1(100)
# g("创建一个新的对象调用1次：")
# g("创建一个新的对象调用2次：")
# g("创建一个新的对象调用3次：")

# def f1():
#     l = []
#     for i in range(3):
#         def f2(j = i):
#             return j * j
#         l.append(f2)
#     return l

# g1,g2,g3 = f1()
# print(g1())
# print(g2())
# print(g3())

# 闭包的应用

# def f1(func):
#     def f2(*args):
#         if len(args) >= 2:
#             func(*args)
#         else:
#             print("Error! Arguments = %s"%list(args))
#     return f2
#
# @f1
# def add(*args):
#     print(sum(args))
#
# # add = f1(add)
# args = range(1,3)
# add(*args)



# def outer(func):
#     def inner():
#         print("Right!")
#         res = func
#         print("log is ok")
#         return  res
#     return inner
#
# @outer
# def f1():
#     print("111")
#
# # print(outer(f1))
# # f = outer(f1)
# # f()
#
# f1()
#
# f2 = f1()
# f2()


# def outer(func):
#     def inner(name):
#         print("认证成功！")
#         res = func
#         print("日志添加成功")
#         return res
#     return inner
#
# @outer
# def f1(name):
#     print(" %s 正在链接业务"%name)
#
# # f = outer(f1('jack'))
# # f('jack')
# f1('jack')

# def hello(name):
#     return "Hello " + name
#
# # print(hello("jack"))
#
# f = hello
# print(f)
# print(f('Job'))

# def f1(func):
#     name = func()
#     print("Hi "+ name)
#
# def f2():
#     return "B"
#
# f1(f2)

# def hi():
#     def f1():
#         return "Hello "
#     # print(f1() + "Bob")
#     return f1() + 'Bob'
#
# print(hi())

# def f1():
#     def f2():
#         print("f2的输出")
#     return f2
#
# f = f1()
# f()
#
# def outer(func):
#     def inner():
#         print("调用func前")
#         # print(func())
#         func
#         # print(type(name),name)
#         print("调用func后")
#     return inner
#
# @outer
# def hi():
#     return  "Hi World"
#     # print("HI")
#
# # print(hi())
#
# hi()

# f = outer(hi)
# f()

# outer(hi)()

# def outer(func):
#     def inner():
#         return func()
#     return inner
# @outer
# def f():
#     return  'Hello'
#
# print(f())

# def outer(func):
#     def inner(*args,**kwargs):
#         return func(*args,**kwargs)
#     return inner
#
# @outer
# def f1(name):
#     return "欢迎光临" + name
#
# @outer
# def f2():
#     return "无参数函数"
#
# print(f1('Jack'))
# print(f2())

# def my_Func():
#     pass
#
# print(my_Func.__name__)

# def outer(func):
#     def inner(*args,**kwargs):
#         return func(*args,**kwargs)
#     return inner
#
# @outer
# def f1():
#     pass
#
# print(f1.__name__)

# import functools
#
# def outer(func):
#     @functools.wraps(func)
#     def inner(*args,**kwargs):
#         return func(*args,**kwargs)
#     return  inner
#
# @outer
# def f1():
#     pass
#
# print(f1.__name__)

# import functools
#
# def decorator(func):
#     @functools.wraps(func):
#     def wrapper(*args,**kwargs):
#         # 原函数运行前
#         value = func(*args,**kwargs)
#         # 原函数运行后
#         return value
#     return wrapper


# import functools
# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args,**kwargs):
#         print('Calling: '+ func.__name__)
#         return func(*args,**kwargs)
#     return wrapper
#
# @log
# def some():
#     pass
#
# some()

# 简易计时器
# import time,functools
# def time_Compute(func):
#     @functools.wraps(func)
#     def wrapper(*args,**kwargs):
#         start_time = time.perf_counter()
#
#         value = func(*args,**kwargs)
#
#         end_time = time.perf_counter()
#
#         duration = end_time - start_time
#         print(f'Duration: {duration}')
#         return value
#     return wrapper
#
# @time_Compute
# def time_func():
#     time.sleep(5)
#
# time_func()

# import functools,time
#
# def slow_down(func):
#     @functools.wraps(func)
#     def wrapper(*args,**kwargs):
#         time.sleep(3)
#         value = func(*args,**kwargs)
#         print("Done.")
#         return wrapper
#     return wrapper
#
# @slow_down
# def f():
#     pass
#
# f()

#
# import functools
# def login(name):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*agre,**kwargs):
#             value = func(*agre,**kwargs)
#             print(f'{name} 是函数名:' + func.__name__)
#             return value
#         return wrapper
#     return decorator
#
# # @login(name='local')
# def f():
#     pass
#
# # f()
# f = login(name="local")(f)()

# import functools
# class Log:
#
#     def __init__(self,name):
#         self.name = name
#
#     def __call__(self, func):
#         @functools.wraps(func)
#         def wrapper(*args,**kwargs):
#             value = func(*args,**kwargs)
#             print(f'{self.name} is calling: '+ func.__name__)
#             return value
#         return wrapper
#
# @Log(name="kack")
# def f():
#     pass
#
# f()

# import functools
# def counter(func):
#     count = 0
#     @functools.wraps(func)
#     def wrapper(*args,**kwargs):
#         nonlocal  count
#         count += 1
#         print(count)
#         return func(*args,**kwargs)
#     return wrapper
#
# @counter
# def every():
#     pass
#
# every()
# every()
# every()
# every()

# import functools
#
# def counter(func):
#     @functools.wraps(func)
#     def wrapper(*args,**kwargs):
#         wrapper.count += 1
#         print(wrapper.count)
#         return func(*args,**kwargs)
#     wrapper.count = 0
#     return wrapper
#
# @counter
# def f():
#     pass
#
# f()
# f()
# f()
# f()
# f()

# import functools
# class Counter():
#
#     def __init__(self,start):
#         self.count = start
#
#     def __call__(self, func):
#         @functools.wraps(func)
#         def wrapper(*args,**kwargs):
#             self.count += 1
#             print(self.count)
#             return func(*args,**kwargs)
#         return wrapper
#
# @Counter(start=0)
# def f():
#     pass
#
# f()
# f()
# f()
# f()


# 类的装饰器
# import functools
# def logit(func):
#     @functools.wraps(func)
#     def wrapper(*args,**kwargs):
#         print("".center(20,"-"))
#         print("Calling: " + func.__name__)
#         value = func(*args,**kwargs)
#         print("".center(20,"-"))
#         return value
#     return wrapper
#
# @logit
# class Tester():
#
#     def __init__(self):
#         print('__init__ ended')
#
#     def f(self):
#         print('f ended')
#
# t = Tester()
# t.f()

# import functools
#
# def singlet(cls):
#     """使类只有一个实例"""
#     @functools.wraps(cls)
#     def wrapper(*args,**kwargs):
#         if not wrapper.instance:
#             wrapper.instance = cls(*args,**kwargs)
#         return wrapper.instance
#     wrapper.instance = None
#     return wrapper
#
# @singlet
# class F1:
#     pass
#
# first = F1()
# second = F1()
#
# print(id(first))
# print(id(second))

# import functools
#
# def logit(func):
#     @functools.wraps(func)
#     def wrapper(*args,**kwargs):
#         print("".center(40,"-"))
#         print('Calling :' + func.__name__)
#         value = func(*args,**kwargs)
#         print("".center(40,"-"))
#         return value
#     return wrapper
#
# class Tester():
#
#     def __init__(self):
#         print("__init__ ended")
#
#     @ logit
#     def f(self):
#         print('f ended')
#
# t = Tester()
# t.f()

# import functools
#
# def inc(func):
#     @functools.wraps(func)
#     def wrapper(*args,**kwargs):
#         print("".center(20,"-"))
#         value = func(*args,**kwargs)
#         print("".center(20,"-"))
#         return  value
#     return wrapper
#
# def dec(func):
#     @functools.wraps(func)
#     def wrapper(*args,**kwargs):
#         print("".center(20,"*"))
#         value = func(*args,**kwargs)
#         print("".center(20,"*"))
#         return value
#     return wrapper
#
# @dec
# @inc
# # @dec
# def f():
#     print("I am here")
#
# f()
# # inc(dec(f))()
