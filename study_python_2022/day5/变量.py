#!/usr/bin/python3
# -*-coding:utf-8-*-
# Time    :2022/1/19  23:04
# Author  :xyz34
# Email   :xyz349925756@hotmail.com
# File    :变量.py
# Project :coding

#局部变量和全局变量
name = 'alex'

def change_name():
    name = "gogogo"
    print("change:",name)

change_name()
print("在外看看name改了？",name)    #没有改变，这里调用的还是全局变量，也就是最上面定义的那个

#在局部变量和全局变量同名时候，局部变量起作用。其他地方全局变量
# 如果在函数里面添加全局变量可以使用global 全局变量，这种做法不可取，非必要时候不能使用，调试非常困难


#传递列表，字典产生的现象
d = {"name":"alex","age":23,"hobbie":"大保健"}
l = ["zhangsan","lisi","jack","lucy"]

def change_data(info,girls):
    info["hobbie"] = "学习"  #字典value修改
    girls.append("xiao")    #列表添加元素

change_data(d,l)  #把字典，列表当作参数传给函数修改
print(d,l)
