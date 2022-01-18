#!/usr/bin/python3
# -*-coding:utf-8-*-
# Time    :2022/1/17  18:31
# Author  :xyz34
# Email   :xyz349925756@hotmail.com
# File    :文件其他功能.py
# Project :coding

f = open(file='./file/2.txt', mode='r+', encoding='utf-8')
f.write("这是一个测试文件\n")
f.write("this is a test file\n")
print(f.read())
print(f.mode)  # 返回文件打开的模式，w r a wb rb ab r+ w+ a+
print(f.name)  # 返回文件名
print(f.fileno())  # 返回文件句柄再内核中的索引值，IO多路复用使用
print(f.flush())  # 把文件从内存刷新到硬盘中
print(f.readable())  # 判断文件是否可读
print(f.readline())  # 只读一行，遍历的时候使用遇到\r \n停止
f.seek(6)  # utf-8汉字是3个字节，这里6个字节，光标返回到‘是’后面
f.write('----')  # 接着下入的字符将覆盖6字符以后的字符
print(f.seekable())  # 判断文件是否可以seek操作
f.seek(16)
print(f.tell())  # 返回当前光标所在位置
f.seek(26)
print(f.truncate())  # 按指定长度截取，默认是从头截取到设置的位置,不指定默认从当前光标去除到文件尾部
print(f.writable())  # 判断文件是否可写

f.close()
