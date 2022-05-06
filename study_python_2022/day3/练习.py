#!/usr/bin/python3
# -*-coding:utf-8-*-
# Time    :{DAY_NAME_FULL}
# Author  :xyz34
# Email   :xyz349925756@hotmail.com
# File    :练习
# Project :coding

# 编程实现对一个元素全是数字的列表求最大值最小值
# l = []
# for i in range(10):
#     l.append(i)
# print(l)
# print("列表l中最大的元素是:%d" % max(l))
# print("列表l中最小的元素是:%d" % min(l))

# 统计字符串中各个元素的个数
# str = "hello world!"
# d = {}
# s1 = str.replace(" ","")
# # print(s1)
# for i in s1:
#     d[i] = s1.count(i)
#     # print(d)
# for key,value in d.items():
#     print("%s 出现了 %d 次" % (key,value))

# 名片管理器
"""
1.添加名片
2.删除名片
3.修改名片
4.查询名片
5.退出系统
"""
# 没有选择退出系统一直循环

d = {"张三":['男',29,'北京'],"李四":['女',26,'云南'],"王五":['男',37,'江苏']}

mes = f"""
    1.添加名片
    2.删除名片
    3.修改名片
    4.查询名片
    5.退出系统
"""
while True:
    print(mes)
    r = input("请输入你的选择：")
    if r.isdigit()==True:
        r1 = int(r)
        if r1 == 1:
            name,sex,age,addr = map(str,input("请输入姓名,性别,年龄,所属省，使用空格分隔:").split())
            d[name] = [sex,age,addr]
            print("您所输入的信息:",name,d[name])
        elif r1 == 2:
            name = input("请输入您要删除的姓名：")
            if name in d.keys():
                d.pop(name)
                print("已删除指定用户")
            else:
                print("您输入的用户不存在，返回主菜单")
        elif r1 == 3:
            name,sex,age,addr = map(str,input("请输入需要修改的姓名、性别、年龄、所属省，以空格分隔").split())
            d[name] = [sex,age,addr]
            print("您所输入的信息:", name, d[name])
        elif r1 == 4:
            name = input("请输入需要查询人的姓名：")
            if name in d.keys():
                d.get(name)
                print("您所输入的信息:",name,d[name])
            else:
                print("您输入的用户不存在，返回主菜单！")
        elif r1 == 5:
            print("退出系统")
            break
    else:
        print("请输入数字！")









