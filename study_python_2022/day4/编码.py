#!/usr/bin/python3
# -*-coding:utf-8-*-
# Time    :2022/1/15 9:25
# Author  :xyz34
# Email   :xyz349925756@hotmail.com
# File    :编码.py
# Project :coding

s = "路飞"  #转换为gbk报错，乱码
print(s)
print(s.encode('gbk'),s.encode('utf-8'))  #gbk 一个中文2字节   utf-8 3个字节