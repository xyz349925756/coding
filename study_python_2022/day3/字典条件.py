#!/usr/bin/python3
# -*-coding:utf-8-*-
# Time    :2022/1/15  18:47
# Author  :xyz34
# Email   :xyz349925756@hotmail.com
# File    :字典条件.py
# Project :coding

dis = {}
for i in range(10):   #生成字典
    dis[f'k{i}'] = i
# print(dis)
print(len(dis))
for k,v in dis.items():   #提取字典的值
    if v > 5:
        print(f'{k}对应的value是：',v)

for k,v in dis.items():
    if v % 2 == 0:
        dis[k] = -1
print(dis)
