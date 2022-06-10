#!/usr/bin/python3
# -*-coding:utf-8-*-
# Auth: xyz34
# File: ATM.py
# TIME: 2022/5/19 周四

# AMT 取钱

# 登录login、查询query、取钱withdraw、存钱deposit、转账transfer、帮助help、退出exit

def login():
    name = input("请输入用户名：")
    passwd = input("请输入%s 的密码:"%name)
    with open('db.txt','a',encoding='utf-8') as f:
        date = name + '\t' + passwd + '\t' + '\n'
        f.write(date)

def query():
    print("查询")
    with open('db.txt','r',encoding='utf-8') as f:
        date = f.readlines()
        for i in date:
            print(i)

def withdraw():
    print("取钱")

def deposit():
    print("存钱")

def transfer():
    print("转账")

def helps():
    print("请输入对应的数字序号：")

dicts = {
    '0':['退出',None],
    '1':['登录',login],
    '2':['查询',query],
    '3':['取钱',withdraw],
    '4':['存钱',deposit],
    '5':['转帐',transfer],
    '6':['帮助',helps]
}



while True:
    for i in dicts:
        # print(''.center(50,"-"))
        print(i,dicts[i][0])
        # print(''.center(9, "-"))

    choies = input("请输入选择：").strip()
    if not choies.isdigit():
        helps()
        continue
    elif choies == '0':
        break
    elif choies in dicts:
        dicts[choies][1]()
    else:
        print('输入有误')


