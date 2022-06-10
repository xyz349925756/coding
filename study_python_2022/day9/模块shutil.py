#!/usr/bin/python3
# -*-coding:utf-8-*-
# Auth: xyz34
# File: 模块shutil.py
# TIME: 5月  星期一

import shutil
# with open('doc/1.txt','r',encoding='utf-8') as f1,open('doc/2.txt','a',encoding='utf-8') as f2:
    # f1.seek(5)
    # shutil.copyfileobj(f1,f2)

# shutil.copyfile('./doc/1.txt','./doc/2.txt')
# shutil.copymode('./doc/1.txt','./doc/2.txt')  # 在linux 下非常有用
# shutil.copystat('./doc/1.txt','./doc/2.txt')  # 拷贝文件状态信息
# shutil.copy('./doc/1.txt','./doc/3.txt')  # 拷贝文件
# shutil.copy2('./doc/1.txt','./doc/3.txt')  # 拷贝文件的时候还拷贝文件信息

# shutil.ignore_patterns('./doc/1.*','./doc/*.txt')
# shutil.copytree('./doc','./xx',ignore=shutil.ignore_patterns('1.*'))  # 拷贝当前目录下的doc到xx并忽略1.txt
#
# def copy_mod(*args,**kwargs):
#     shutil.copyfile(*args,**kwargs)
#     shutil.copystat(*args,**kwargs)
#     shutil.copymode(*args,**kwargs)
#
# shutil.copytree('./doc','./x',copy_function=copy_mod)  # 拷贝当前doc目录下的所有文件，拷贝函数是文件，状态信息，权限

# shutil.rmtree('./xxx') # 删除一个指定目录
# shutil.rmtree('./xx',ignore_errors=False)
# import os
# if os.path.isdir('./x'):
#     shutil.rmtree('./x')
# else:
#     print("该路径不是目录")

# def rmError(*args,**kwargs):
#     raise Exception("文件夹不存在")
#
# shutil.rmtree('./xxx',ignore_errors=False,onerror=rmError)

# shutil.move('./doc','./teest') # 将文件或文件夹移动到其他位置

# def disk_size(*args):
#     l = shutil.disk_usage(*args)# 给定路径的磁盘使用统计数据
#     msg = f"""
#       Total: {int(l[0]/1024/1024/1024)} GB
#       Used : {int(l[1]/1024/1024/1024)} GB
#       Free : {int(l[2]/1024/1024/1024)} GB
#     """
#     return msg
#
# print(disk_size('c:\windows'))
# print(disk_size('d:'))
# print(disk_size('e:'))
# print(disk_size('f:'))

# shutil.make_archive('./zip/test','zip','./teest') # 把teest文件夹打包到zip文件夹下的test.zip
# root_dir = ./teest     base_dir="-" 子文件夹下
# shutil.make_archive('./zip/pack','zip',root_dir='./pack',base_dir='test')
# shutil.make_archive('./zip/pack','zip',root_dir='./pack',base_dir='m1.py')
# shutil.unpack_archive('./zip/test.zip','./test',format='zip')

# shutil.register_archive_format()  # 归档器
# print(shutil.get_archive_formats()) # 返回支持的归档格式