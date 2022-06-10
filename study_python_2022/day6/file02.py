#!/usr/bin/python3
# -*-coding:utf-8-*-
# Auth: xyz34
# File: file2.py
# TIME: 2022/5/6 周五

# import os
# os.rename("txt/2.txt","txt/操作文件.txt")
# os.remove('操作文件.txt')
# os.mkdir("doc")
# os.getcwd()
# print(os.getcwd())
# print(os.listdir("."))
# os.chdir("../day5")
# os.rmdir('doc')
# print(os.listdir("."))
# os.cpu_count()
# print(os.cpu_count())
# print(os.linesep)
# s = os.walk(top='', topdown=True, onerror=None)
# print(s)

import os
os.chdir("txt")
rename_Dir=os.listdir()
for i,n in enumerate(rename_Dir):
    file_Suffix = n[-4:]
    old_FileName = n[:-4]
    # print(n)
    # if n[-4:] == '.txt':
    #     new_File_Name = 'test' + str(i)+file_Suffix
    #     # print(n)
    #     os.rename(n,new_File_Name)
    # else:
    s = n.split(".")
    file_Suffix_1 = s[-1]
    old_FileName_1 = '[盗版]-cloudb.pub'
    new_File_Name = old_FileName_1 + str(i) + '.' + file_Suffix_1
    os.rename(n, new_File_Name)
    # print(old_FileName_1 in n)
    # print(n)
    # print(old_FileName_1 in os.path.basename(n))
    # if old_FileName_1 in os.path.basename(n) == True:
    #     print("%s 文件名存在不必重命名！" % n)
    # else:
    #     new_File_Name = old_FileName_1 + str(i) + '.' + file_Suffix_1
    #     os.rename(n,new_File_Name)


print(''.center(60, '-'))
for i in rename_Dir:
    print(i)

# import os
# os.chdir('txt')
# for i in os.listdir():
#     os.remove(i)
# print(os.listdir())