#!/usr/bin/python3
# -*-coding:utf-8-*-
# Auth: xyz34
# File: 作业.py
# TIME: 5月  星期四

# 登录login、查询query、取钱withdraw、存钱deposit、转账transfer、帮助help、退出exit

# ====================周末作业====================
# 编写ATM程序实现下述功能，数据来源于文件db.txt
# 0、注册功能：用户输入账号名、密码、金额amount，按照固定的格式存入文件db.txt
# 1、登录功能：用户名不存在，要求必须先注册，用户名存在&输错三次锁定，登录成功后记录下登录状态（提示：可以使用全局变量来记录）

# 下述操作，要求登录后才能操作
# 1、充值功能：用户输入充值钱数，db.txt中该账号钱数完成修改
# 2、转账功能：用户A向用户B转账1000元，db.txt中完成用户A账号减钱，用户B账号加钱
# 3、提现功能：用户输入提现金额，db.txt中该账号钱数减少
# 4、查询余额功能：输入账号查询余额


def login():
    c = input("登录请输入【y】,注册请输入【r】，退出请输入【n】:").strip()
    if c == 'y':
        name = input("请输入用户名：").strip()
        with open('db.txt','r',encoding='utf-8') as f:
            for i in f.readlines():
                if (name in i) == True:
                    p = input("请输入%s的密码："%name).strip()
                    p = list(p)
                    count = 0
                    while count < 3:
                        if p == p[1]:
                            print("欢迎登录")
                        else:
                            print("请重试")





    elif c == 'r':
        name = input("请输入用户名：").split()
        passwd = input("请输入密码：").split()
        with open('db.txt','a',encoding='utf-8') as f:
            date = f.writelines(name+'\t'+passwd+'\t')
    else:
        return

def query():
    print("query")

def withdraw():
    print("withdraw")

def deposit():
    print("deposit")

def transfer():
    print("transfer")

def helps():
    print("helps")

meun = {
    '0':['退出',None],
    '1':['登录',login],
    '2':['查询',query],
    '3':['取钱',withdraw],
    '4':['存钱',deposit],
    '5':['转账',transfer],
    '6':['帮助',helps]
}



while True:
    for i, k in meun.items():
        print(i, k[0])

    choise = input("请输入选择的序号：").strip()
    if not choise.isdigit():
        helps()
        continue
    elif choise == '0':
        break
    elif choise in meun:
        meun[choise][1]()
    else:
        print("输入错误。")
