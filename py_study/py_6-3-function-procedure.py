#!/usr/bin/python
#-*-coding:utf-8-*-
'''
Created on 2016年12月17日
@author: linux
'''

def hello():
    print("hello!")
print(hello())

def he():
    return ['hello',1,2,'test']
print(he())
"""
local variable本地变量和全局变量global variable
"""
def discounts(price,rate):
    final_price = price * rate
    return final_price

old_price = float(input("请输入原价："))
rate = float(input("请输入折扣："))
new_price = discounts(old_price, rate)
print('打折后价格：',new_price)
#print("这里试图打印局部变量final_price",final_price)  #局部变量不能再次被调用。


