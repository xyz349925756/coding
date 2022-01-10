#!/usr/bin/python
#-*-coding:utf-8-*-
"""
设计一个验证用户密码程序，用户只有三次机会输入错误，不过如果用户输入的内容中包含"*"则不计算在内
"""

user = ['user00','user01','user02']
password =['password0','password1','password2']
username = input("请输入用户名：")
list = []
for i in username:
    list.append(i)
if '*' in list:
    print("检测到您的用户名中包含*!")
    username = input("请重新输入用户名：")
    if username.isalnum() == True:
        passwd = input("请输入密码：")
    for i in passwd:
            list.append(i)
    if '*' in list:
        print("检测到您输入的密码中包含*!")
        passwd = input("请重新输入密码：")
    print("欢迎光临！%s"%username) if username in user else print("用户名不存在，请与管理员联系！")   
else:
    if username.isalnum() == True:
        passwd = input("请输入密码：")
    for i in passwd:
        list.append(i)
    if '*' in list:
        print("检测到您输入的密码中包含*!")
        passwd = input("请重新输入密码：")
    print("欢迎光临！%s"%username) if username in user else print("用户名不存在，请与管理员联系！")
                        








