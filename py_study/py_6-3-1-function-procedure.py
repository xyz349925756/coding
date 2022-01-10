#!/usr/bin/python
#-*-coding:utf-8-*-
'''
Created on 2016年12月18日
@author: linux
'''

def discounts(price,rate):
    final_price = price * rate
    old_price = 50 #修改全局变量。这里是局部变量
    print("这里试图打印全局变量",old_price)
    return final_price
    
old_price = float(input("请输入价格:"))
rate = float(input("请输入折扣："))
new_price = discounts(old_price, rate)
print("全局变量 old_price 现在的值是:",old_price)
print("打折后的价格是:",new_price)