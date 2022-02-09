#!/usr/bin/python3
# -*-coding:utf-8-*-
# Time    :2022/1/19  22:26
# Author  :xyz34
# Email   :xyz349925756@hotmail.com
# File    :非固定参数.py
# Project :coding

#输入时候不确定传入多少个参数，就可以使用非固定参数

def stu_register(name,age,*args):   #*args会把传入的参数变成一个元组
    print(name,age,args)
stu_register('zhangsan',34)   #zhangsan 34 ()  这个()就是元组
stu_register('jack',22,'cn','python')    #jack 22 ('cn', 'python')


def stu_registers(name,age,*args,**kwargs):  #**kwargs 把传入的参数变成一个dict形式
    print(name,age,args,kwargs)
stu_registers('zhangsan',22)
stu_registers('李四',43,'cn','linux',sex='M',province='yunnan')