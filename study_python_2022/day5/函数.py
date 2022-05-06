#!/usr/bin/python3
# -*-coding:utf-8-*-
# Time    :2022/1/19  14:40
# Author  :xyz34
# Email   :xyz349925756@hotmail.com
# File    :函数.py
# Project :coding

# def sayhi ():    #函数名
#     print(f"Hello,world!")
# sayhi()  #调用函数
#
# def calc (x,y):  #形参，在函数内有效，只有在调用的时候加载到内存
#     res = x ** y
#     print(f"{x} ** {y} = {res}")
# a = 5
# b = 4
#
# calc(a,b)    #实参  可以是变量，任意数据类型，表达式，函数，实参需要提前赋值
#
# def stu_regediter(name,age,course,country='CN'):  #定义默认参数国家
#     print("学生注册信息".center(50,'-'))
#     print("姓名",name)
#     print("年龄",age)
#     print("国家",country)
#     print("课程",course)
#
# stu_regediter("zhangsan",22,'python')   #上面定义了默认国家，这里传参就没有必要再填
# stu_regediter("lisi",27,'linux','JP')
# stu_regediter("zhaosi",32,'python')
#
# #定义了默认参数，默认参数就需要移动到后面，如果调用时候没有指定就使用默认，如果指定了就是用指定，位置参数 > 默认参数
# # 关键参数（指定参数） 关键参数必须放在位置参数后面。
# stu_regediter("赵四",course='linux',age=33)   #位置参数 > 关键参数 > 默认参数
#
# #若函数不确定用户传入参数
# name = input("请输入你的姓名：")
# sex = input("请输入你的性别：")
#
# msg = f"""
# 姓名：{name}
# 性别：{sex}
# """
#
# def msgs ():
#     print(msg)
#
# msgs()

# a = int(input("请输入一个数字"))
# b = int(input("请输入一个数字"))
# def sum():
#     "两数求和"
#     print("%d + %d = %2d"%(a,b,a+b))
#
# sum()
#
# print(help(sum))


# def add2sum(a,b):
#     print("%d + %d = %d"%(a,b,a+b))
#
# add2sum(11,22)

# def thr3sum(a,b,c):
#     print("%d + %d - %d = %d"%(a,b,c,(a + b -c)))
#
# thr3sum(1,2,3)

# def sum(a,b):
#     return a+b
#
# print(sum(1,2))


# def printOneline(a):
#     s = ""
#     print(s.center(a,"-"))
#
# for i in range(5):
#     printOneline(i)

# 写一个函数求三个数的和
# a,b,c=map(int,input("请输入三个数字，以空格分隔：").split())
# def thr3Sum():
#     # print("%d + %d + %d = %d"%(a,b,c,(a+b+c)))
#     return a+b+c
# print("%d + %d + %d = %d" % (a,b,c,thr3Sum()))


# 写一个函数求三个数的平均值
# a,b,c = map(int,input("请输入三个数字，以空格分隔:").split())
#
# def three_Average():
#     return (a+b+c)/3
# print("%d %d %d 的平均值是：%f"%(a,b,c,three_Average()))

# def sum():
#     a = 2
#     print(a)
# sum()

# a = 2
# def sum():
#    print(a)
# sum()

# a = 2
# def s():
#     global a
#     a = 5
#     print("局部变量",a)
# s()
#
# print("全局变量a",a)
# import random
# i = 0
# for n in range(10):
#     print(i,n)
#     i += 1
# def s(a,b):
#     c = a+b
#     d = a*b
#     return c,d
# e,f=s(3,4)
# print("e =",e,"f =",f)

# def printinfo(name,age=35):
#     """打印传输的字符串"""
#     print("name",name)
#     print("age",age)
#
# printinfo(name='wang')
# printinfo(name='zhangsan',age=25)

# def func(a,b,*args,**kwargs):
#     """可变参数"""
#     print("a=",a,"b=",b,"args=",args,"kwargs=",kwargs)
#
# func(1,2,3,4,5,m=6,n=7)

# def selfAdd(a):
#     a += a
#
# b = 1
# selfAdd(b)
# print(b)
#
# b = [1,2]
# selfAdd(b)
# print(b)

# 计算n!=1*2*3*...*n 阶乘
# def calNum(n):   # n是形参
#     i = 1     # 局部变量
#     result = 1   # 局部变量 乘积初始化
#     while i <= n:
#         result *= i   # result = result * i
#         i += 1
#     return result    # 返回值
# ret = calNum(3)   # 7是实参
# print(ret)
#
#
# # 1 * 2 = 2 * 3 = 6

# def callNum(n):
#     if n >= 1:
#         re = n * callNum(n - 1)
#     else:
#         re = 1
#     return re
#
# ret = callNum(3)
# print(ret)

# s = lambda a,b:a+b
# print(s(10,20))

# def fun(a,b,opt):
#     print("a =",a,"b =",b,"result =",opt(a,b))
#
# fun(1,2,lambda x,y:x+y)
stus = [
    {"name":"zhangsan", "age":18},
    {"name":"lisi", "age":19},
    {"name":"wangwu", "age":17}
]
# stus.sort(key=lambda x:x['name'])
# print(stus)
#
# stus.sort(key=lambda x:x['age'])
# print(stus)

for i in range(len(stus)):
    print(stus[i])
    def key():
        print(stus[i]['name'])
    key()


# def sun(x,y):
#     print(x,y,x+y)
# sun(1,4)
#
#
# s = lambda x,y:x+y
# print(s(1,4))