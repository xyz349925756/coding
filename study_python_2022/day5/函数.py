#!/usr/bin/python3
# -*-coding:utf-8-*-
# Time    :2022/1/19  14:40
# Author  :xyz34
# Email   :xyz349925756@hotmail.com
# File    :函数.py
# Project :coding

def sayhi ():    #函数名
    print(f"Hello,world!")
sayhi()  #调用函数

def calc (x,y):  #形参，在函数内有效，只有在调用的时候加载到内存
    res = x ** y
    print(f"{x} ** {y} = {res}")
a = 5
b = 4

calc(a,b)    #实参  可以是变量，任意数据类型，表达式，函数，实参需要提前赋值

def stu_regediter(name,age,course,country='CN'):  #定义默认参数国家
    print("学生注册信息".center(50,'-'))
    print("姓名",name)
    print("年龄",age)
    print("国家",country)
    print("课程",course)

stu_regediter("zhangsan",22,'python')   #上面定义了默认国家，这里传参就没有必要再填
stu_regediter("lisi",27,'linux','JP')
stu_regediter("zhaosi",32,'python')

#定义了默认参数，默认参数就需要移动到后面，如果调用时候没有指定就使用默认，如果指定了就是用指定，位置参数 > 默认参数
# 关键参数（指定参数） 关键参数必须放在位置参数后面。
stu_regediter("赵四",course='linux',age=33)   #位置参数 > 关键参数 > 默认参数

#若函数不确定用户传入参数
