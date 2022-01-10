#!/usr/bin/python
#-*-coding:utf-8-*-
'''
Created on 2016年12月18日
@author: linux
'''

count = 5
def myFunction():
    count = 10
    return count
print("局部变量 count = ",myFunction())
print("全局变量 count = ",count)
    
count = 20    
def second():
    global count 
    count = 15
    return ("局部变量 count = ",count)
print("全局变量 count = ",count)
print("局部变量 count = ",second())
     