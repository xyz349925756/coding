#!/usr/bin/python3
# -*-coding:utf-8-*-
# Time    :2022/1/17  20:32
# Author  :xyz34
# Email   :xyz349925756@hotmail.com
# File    :占硬盘文件修改.py
# Project :coding

f_name = './file/3.txt'
f_new_name = "%s.new" % f_name
old_str = "⻢纤⽻"
new_str = "黑牛"
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

#上面的代码会生成一个修改后的文件，源文件不动