#!/usr/bin/python3
# -*-coding:utf-8-*-
# Auth: xyz34
# File: file_1.py
# TIME: 2022/5/6 周五

# f = open('txt/1.txt','a')
# f.write('hello world')
# f.close()

# f = open('txt/1.txt','r+')
# # f.write('\n test')
# # print(f.read())
# content = f.readlines()
#
# for b in content:  # 遍历
#     print(b)
#
# f.close()

# 文件复制 testllo world
#
#  test
#
#  test
#
#  test
# 复制文件
# oldfile_Name = input('请输入你的文件:')
# oldfile_open_file = open(oldfile_Name,'r')
# old_content = oldfile_open_file.readlines()
#
# new_File_Name = input('请输入新文件名:')
# new_file = open(new_File_Name,'w')
#
# for i in old_content:
#     new_file.write(i)
#
# new_file.close()
#
# new_file_F = open(new_File_Name)
# new_File_Content = new_file_F.read()
# print(new_File_Content)
#
# oldfile_open_file.close()
# new_file_F.close()

f=open('txt/1.txt')
s=f.read()
# print(s)

# p = f.tell()
f.seek(5,0)
p=f.tell()
print('当前位置是',p)