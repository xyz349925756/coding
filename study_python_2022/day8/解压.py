#!/usr/bin/python3
# -*-coding:utf-8-*-
# Auth: xyz34
# File: 解压.py
# TIME: 5月  星期五

import os
os.chdir("E:\\test")
print(os.listdir())
for f in os.listdir():
    os.system('C:\PROGRA~1\WinRAR\Rar.exe x -y -pwww.itjc8.com@6"^"*#5xIS3XZK ' + f)
    os.system('del '+ f)
    # os.system('ping '+ 'baidu.com')