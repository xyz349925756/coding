#!/usr/bin/python3
# -*-coding:utf-8-*-
# Time    :2022/1/19  22:42
# Author  :xyz34
# Email   :xyz349925756@hotmail.com
# File    :小练习1.py
# Project :coding

def print_info (name,age,sex='M',hobbie='大保健'):
    print("信息:\t".center(50,'-'))
    print("name:\t",name)
    print('age:\t',age)
    print('sex:\t',sex)
    print('hobbie:\t',hobbie)

print_info(name='alex',age=23,sex='w')
print_info(name='jack',age='33',hobbie='学习')
