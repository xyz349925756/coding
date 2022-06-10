#!/usr/bin/python3
# -*-coding:utf-8-*-
# Auth: xyz34
# File: 批量解压.py
# TIME: 5月  星期四

import os
# os.chdir("E:\\test")
# print(os.listdir())
# for f in os.listdir():
#     os.system('C:\PROGRA~1\WinRAR\Rar.exe x -pwww.itjc8.com@6"^"*#5xIS3XZK ' + f)
    # os.system('ping '+ 'baidu.com')


os.chdir("E:\教程\python29")
# for i in os.listdir():
#     paths = os.path.abspath(i)
#     p1 = os.path.basename(paths)
#     print(os.listdir(p1))

# for i in os.walk("E:\教程\python29"):
#     print(i)

for pwd,dirs,files in os.walk("E:\教程\python29"):
    # print("当前文件夹路径:",pwd)
    # print("当前文夹下的子目录:",dirs)
    # print("当前文件:",files)

    os.chdir(pwd)
    print("".center(60,"-"))
    for f in files:
        suffix = os.path.join(pwd, f).split(".")[-1]
        if ('rar' in suffix) or ('zip' in suffix):
            os.system('C:\PROGRA~1\WinRAR\Rar.exe x -pwww.itjc8.com@6"^"*#5xIS3XZK ' + f)
            # print(os.path.join(pwd,f))


