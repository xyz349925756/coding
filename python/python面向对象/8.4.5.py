#！/usr/bin/python
# -*- coding:utf-8 -*-
##################################################################
#				              __del__方法       				 #
##################################################################
class Fruit:
    def __init__(self,color):   #初始化__color属性
        self.__color = color
        print(self.__color)
    def __del__(self):    #析构函数
        self.__color = ""
        print("free...")
    def grow(self):
        print("grow...")
if __name__ =="__main__":
    color = "red"
    fruit = Fruit(color)  #带参数的构造函数
    fruit.grow()
