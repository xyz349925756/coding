#!/usr/bin/python3
# -*-coding:utf-8-*-
# Auth: xyz34
# File: 存放家具.py
# TIME: 2022/5/9 周一

# 存放家具，存放房间的大小和房间里的所有家具，并且要能够添加新家具
# 拿到需求先分析，家具是按平面堆放还是可以立体堆放，这里就按平面算，
# 家具有哪些？沙发sofa ，床bed，茶几tea table，书桌desk，电视柜tv_cabinet，等等。。。
# 可以随时存取。房间面积多大，每个家具都有一个占地面积
# 家具的共有属性就是：面积 area
# 取出家具：take out
# 添加家具：add to
# 家具：furnishing

class Room:
    """定义存储类"""

    def __init__(self):
        self.areas = 100
        self.string = ""
        self.furnishing = {'书桌':'1.4'}

    def __str__(self):
        msg = """
        1、查看已有家具
        2、存入家具
        3、取出家具
        4、退出
        """
        return msg

    def add_Furnishing(self):
        while True:
            print("".center(60, "-"))
            print(home)
            print("".center(60,"-"))
            ins = int(input("请输入菜单选项："))
            if ins == 1:
                for i,key in enumerate(self.furnishing):
                    i += 1
                    print("序号：%d"%i,"家具名称: %s"%key,"占地面积%s平方"%self.furnishing[key])
            elif ins == 2:
                name = input("请输入需要存入的家具名称:")
                arae = input("请输入%s占地面积:"%name)
                self.furnishing[name] = arae
                print("已存入家具：%s"%name,"占地面积：%s"%arae)
            elif ins == 3:
                name = input("请输入需要取出的家具名称：")
                self.furnishing.pop(name)
                print("已经取出家具：%s"%name)
            elif ins == 4:
                break
            else:
                print("输入错误请输入菜单对应的选项！")

home = Room()
# print(home)
home.add_Furnishing()

# class Home:
#
#     def __init__(self,area):
#         self.area = area
#         self.containsItem = []
#
#     def __str__(self):
#         msg = "当前可用面积:" + str(self.area)
#
#         if len(self.containsItem) > 0:
#             msg = msg + "已有物品："
#             for temp in self.containsItem:
#                 msg = msg + temp.getName() + " ,"
#             msg = msg.strip(",")
#         return msg
#
#     def accommodateItem(self,item):
#         needArea = item.getUsedArea()
#         if self.area > needArea:
#             self.containsItem.append(item)
#             self.area -= needArea
#             print("已存放")
#         else:
#             print("Error:房间可用面积为：%d，需要面积为%d："%(self.area,needArea))
#
# class Bed:
#
#     def __init__(self,area,name="床"):
#         self.name = name
#         self.area = area
#
#     def __str__(self):
#         msg = "床的面积为：" + str(self.area)
#         return msg
#
#     def getUsedArea(self):
#         return self.area
#
#     def getName(self):
#         return self.name
#
#
# newHome = Home(100)
# print(newHome)
#
# newBed = Bed(20)
# print(newBed)
#
# newHome.accommodateItem(newBed)
# print(newHome)
#
# newBed2 = Bed(30,'希摩斯')
# print(newBed2)
#
# newHome.accommodateItem(newBed2)
# print(newHome)
