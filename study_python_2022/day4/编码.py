#!/usr/bin/python3
# -*-coding:utf-8-*-
# Time    :2022/1/15 9:25
# Author  :xyz34
# Email   :xyz349925756@hotmail.com
# File    :编码.py
# Project :coding

s = "路飞"  #转换为gbk报错，乱码
# print(s)
# print(s.encode('gbk'),s.encode('utf-8'))  #gbk 一个中文2字节   utf-8 3个字节 #没有解码的字节输出
# print(s.encode('utf-8').decode('utf-8'))
# print(s.encode('gbk').decode('gbk'))  #把gbk编码字符再解码成unicode

f = open('./file/1.txt','wb')  #二进制写
f.write(s.encode('utf-8'))  #编码转为二进制
f.close()
