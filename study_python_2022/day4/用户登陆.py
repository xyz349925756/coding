#!/usr/bin/python3
# -*-coding:utf-8-*-
# Time    :2022/1/17  22:57
# Author  :xyz34
# Email   :xyz349925756@hotmail.com
# File    :用户登陆.py
# Project :coding

"""
用户输入账号密码进行登陆
用户信息保存在文件内
用户输入错误三次之后锁定用户，下次在登陆，检测到这个用户是被锁定的，依然不允许登陆，提示被锁。
可以添加解锁方法！！
"""
f = open('./file/user','r',encoding='utf-8')

dis = {}
count = 0
while count <= 3:  # 3次机会
    user = input("请输入用户名：")
    for line in f:
        lines = line.split()  #转成列表
        print(lines)
    count += 1


