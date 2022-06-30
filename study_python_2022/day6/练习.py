#!/usr/bin/python3
# -*-coding:utf-8-*-
# Auth: xyz34
# File: 练习.py
# TIME: 2022/5/7 周六

# 读取一个文件，显示除了#号开头行的所有行
# import os
# os.chdir('txt')
# # print(os.listdir())
# f = open('nginx.conf','r',encoding='utf-8')
# for i in f.readlines():
#     if i[0] != '#' and i != '\n':
#         # i.split()
#         # i.rsplit()
#         print(i)
# # content = f.readlines()
# # print(content)
# f.close()

# 创建一个密码薄，可以增删改查
import os
os.chdir('txt')
def write():
    with open('passwd.txt','a',encoding='utf-8') as f:
        url,name,passwd = map(str,input("输入网址，用户名，密码：以空格分隔:").split())
        date = url + "\t" + name + "\t" + passwd + "\n"
        f.write(date)

# f = open('password_books','a',encoding='utf-8')
# url,name,passwd = map(str,input("请输入你的网址，以及该网站的用户名，密码，以空格分割 >>> ").split())
# date = url + "|"+ name + "|" + passwd + "\n"
# f.write(date)
# f.close()

def read():
    with open('passwd.txt','r',encoding='utf-8') as f1:
        content = f1.readlines()
        for i in  content:
            print(i,type(i))
# f1 = open('password_books','r')
# content = f1.readlines()
# for i in content:
#     print(i)
# f1.close()

if __name__ == '__main__':
    write()
    read()
