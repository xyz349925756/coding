#!/usr/bin/python3
# -*-coding:utf-8-*-
# Time    :2022/1/17  14:30
# Author  :xyz34
# Email   :xyz349925756@hotmail.com
# File    :循环文件.py
# Project :coding

f = open(file='./file/联系方式',mode='r',encoding='utf-8')
# print(f.read())
# 挑选出升高170以上的体重50以下的
for line in f:
    line = line.split() #将行以空格分割成列表
    height = int(line[3])
    weight = int(line[4])
    if height >= 170 and weight <= 50:
        print(line)
f.close()