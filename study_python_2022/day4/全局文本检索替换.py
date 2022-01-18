#!/usr/bin/python3
# -*-coding:utf-8-*-
# Time    :2022/1/17  21:40
# Author  :xyz34
# Email   :xyz349925756@hotmail.com
# File    :全局文本检索替换.py
# Project :coding

#引入传参
import sys
old_str = sys.argv[1]
new_str = sys.argv[2]
filename = sys.argv[3]

#打开文件
f = open(filename,'r+',encoding='utf-8')
data = f.read()

#统计出现的次数
old_str_count = data.count(old_str)
new_data = data.replace(old_str,new_str)

#光标返回开始位置清除原文本
f.seek(0)
f.truncate()

#写入替换文本
f.write(new_data)

print(f"成功替换字符{old_str} to {new_str},共{old_str_count}次……")

# PS F:\coding\study_python_2022\day4> python .\全局文本检索替换.py 路飞 这是一个测试  .\file\1.txt
# 成功替换字符路飞 to 这是一个测试,共1次……
# 这里需要在终端执行，在pycharm 执行会报错。