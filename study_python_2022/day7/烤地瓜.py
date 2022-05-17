#!/usr/bin/python3
# -*-coding:utf-8-*-
# Auth: xyz34
# File: 烤地瓜.py
# TIME: 2022/5/8 周日

class SweetPotato:
    "定义烤地瓜的类"

    # 定义初始化方法
    def __init__(self):
        self.cookedLevel = 0
        self.cookedString = "生的"
        self.condiments = []

    # 定义print时显示的内容
    def __str__(self):
        msg = self.cookedString + "地瓜"
        if len(self.condiments) > 0:
            msg = msg + "("   # 烤熟了，可以吃了！地瓜(辣椒酱)  就是这样的显示

            for temp in self.condiments:
                msg = msg + temp + ','
            msg = msg.strip(",")

            msg = msg + ")"  # 烤熟了，可以吃了！地瓜(辣椒酱)  就是这样的显示
        return  msg

    # 添加配料
    def addCondiments(self,condiments):
        self.condiments.append(condiments)

    # 烤地瓜方法
    def cook(self,time):
        self.cookedLevel += time
        if self.cookedLevel > 8:
            self.cookedString = "烤糊了..."
        elif 8 > self.cookedLevel > 5:
            self.cookedString = "烤熟了，可以吃了！"
        elif 5> self.cookedLevel > 3:
            self.cookedString = "半生不熟，还需要几分钟"
        else:
            self.cookedString = "生的"

# 测试
mySweetPotato = SweetPotato()

print("有了一个地瓜，还没有烤".center(60,"-"))
print(mySweetPotato.cookedLevel)
print(mySweetPotato.cookedString)
print(mySweetPotato.condiments)

print("开始烤地瓜".center(60,"-"))

print("4分钟过去了".center(60,"-"))
mySweetPotato.cook(4)
print(mySweetPotato)

print("又过去2分钟".center(60,"-"))
mySweetPotato.cook(2)
print(mySweetPotato)

print("添加辣椒酱".center(60,"-"))
mySweetPotato.addCondiments("辣椒酱")
print(mySweetPotato)

print("又过去5分钟".center(60,"-"))
mySweetPotato.cook(5)
print(mySweetPotato)

print("添加番茄酱".center(60,"-"))
mySweetPotato.addCondiments("番茄酱")
print(mySweetPotato)


# mySweetPotato.cook(4)
# print(mySweetPotato.cookedLevel)
# print(mySweetPotato.cookedString)
# print(mySweetPotato.condiments)
