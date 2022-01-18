#!/usr/bin/python3
# -*-coding:utf-8-*-
# Time    :2022/1/17  21:24
# Author  :xyz34
# Email   :xyz349925756@hotmail.com
# File    :覆盖文件的修改.py
# Project :coding

import os
f_name = './file/3.txt.new'
f_new_name = '%s.two ' % f_name
old_str = '⻢纤⽻'
new_str = '黑牛'

f = open(f_name,'r',encoding='utf-8')
f_new = open(f_new_name,'w',encoding='utf-8')

for line in f:
    if old_str in line:
        new_line = line.replace(old_str,new_str)
    else:
        new_line = line
    f_new.write(new_line)
f.close()
f_new.close()
os.remove(f_name)   #移除文件
os.rename(f_new_name,f_name)   #重命名为以前的文件

