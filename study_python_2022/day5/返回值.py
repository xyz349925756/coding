#!/usr/bin/python3
# -*-coding:utf-8-*-
# Time    :2022/1/19  22:55
# Author  :xyz34
# Email   :xyz349925756@hotmail.com
# File    :返回值.py
# Project :coding

#返回值就是返回执行结果，linu中的 $? 判断是否成功运行
def stu_register(name,age,coures='py',country='CN'):
    print("学生信息".center(50,'='))
    print('name:\t',name)
    print('age\t',age)
    print('country\t',country)
    print('coures\t',coures)

    if age > 22:
        return False    #函数的结束
    else:
        return True

registration_status = stu_register('赵四',23,coures='python',country='JP')

if registration_status:
    print("注册成功")
else:
    print("超龄！")