#!/usr/bin/python3
# -*-coding:utf-8-*-
# Auth: xyz34
# File: 正则表达式.py
# TIME: 6月  星期一

import re

s1='abcsdaadsa1_abds,342d-sad 2f (a3) da'
s2='ABCDDBCSAabdvsasd'
s3='     d    a    _s   2    '

# re.compile()
# result=re.search('A+',s2)
# re.fullmatch()
# result=re.match('A',s2)

s4 = 'word,hello world,wang'
# result=re.split(r'\W+',s4)
# result=re.split(r'(\W+)',s4)
# result = re.split('[0-9]+',s1)  # 把0-9的数字作为分隔符
# result = re.split('[0-9]+',s1,flags=re.IGNORECASE)  # 忽略空
# result = re.split(r'\W+',s3)
# result = re.split(r'\b',s2)
# result = re.split(r'(\W*)',s2)
# result = re.split(r'\W*',s2)
# result = re.findall(r'\bw[a-z]+',s4)
s5 = 'set width=20 and height=78'
# result = re.findall(r'(\w+)=(\d+)',s5) # 相比起下面的方法，这种方法匹配到的后去更容易提取使用
# result = re.findall(r'\w+=\d+',s5) # 匹配字符串中以str=int的形式的内容并返回列表

# result = re.finditer(r'A+',s2)
# for i in result:
#     print(i)

# result = re.sub(r'\d+[0-9]*','|',s3)
# result = re.match(r'^[a2-9tjqk]{5}$','246jjqkt')


# print(result)
# print('开始:',result.start(),'结束:',result.end(),'span:',result.span())
# print('group:',result.group(),'groups:',result.groups())
s6 = 'wadshong5220@126.com,xyz349925756@gmail.com,xyz349925756@hotmail.com'
# result = re.sub(r'[a-z0-9]+@[a-z0-9]+\.com','new_mail',s6,count=1)
# result=re.sub(r'([a-zA-Z0-9]+)@([0-9]+)\.com',r'\1@\2.net',s6)
# result = re.sub(r'(?P<local>[a-z0-9]+)@(?P<SLD>[a-z0-9]+).com',r'\g<local>@\g<SLD>.pub',s6)

# print(result)

print(re.ASCII is re.A)