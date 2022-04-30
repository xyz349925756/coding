#!/usr/bin/python3
# -*-coding:utf-8-*-
# AUTH: google
# FILE: 1.py
# TIME: 2022/3/13 周日

# 循环打印1-10
#for i in range(10):
#    msg = f'''
#    输出：{i}
#    '''
#    print(msg)

name = input("请输入姓名：")
qq = input("请输入QQ号码：")
tel = input("请输入手机号：")
address = input("请输入地址：")
msg = f'''
=======================
姓名：{name}
QQ:{qq}
手机号：{tel}
地址：{address}
=======================
'''
print(msg)