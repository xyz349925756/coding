#!/usr/bin/python3
# -*-coding:utf-8-*-
# Auth: xyz34
# File: 1.py
# TIME: 5月  星期四
def login():
    print('登录功能')


def transfer():
    print('转账功能')


def check_banlance():
    print('查询余额')


def withdraw():
    print('提现')


def register():
    print('注册')

func_dic = {
    '0': ['退出', None],
    '1': ['登录', login],
    '2': ['转账', transfer],
    '3': ['查询余额', check_banlance],
    '4': ['提现', withdraw],
    '5': ['注册', register]
}
# func_dic['1']()


while True:
    for k in func_dic:
        print(k, func_dic[k][0])

    choice = input('请输入命令编号：').strip()
    if not choice.isdigit():
        print('必须输入编号，傻叉')
        continue

    if choice == '0':
        break

    # choice='1'
    if choice in func_dic:
        func_dic[choice][1]()
    else:
        print('输入的指令不存在')



