#！/usr/bin/python
# -*- coding:utf-8 -*-
##################################################################
#						__init__方法                             #
##################################################################
class Fruit:
    def __init__(self,color):  #__init__是Fruit的初始化函数，即构造函数，该函数根据参数color的值初始化属性__color
        self.__color = color #对Fruit类的属性__color进行赋值，需要前缀self，否则python默认会将__color认为是__init__的变量
        print(self.__color) #输出赋值后的属性__color。
    def getColor(self):
        print(self.__color)
    def setColor(self,color):  #定义方法setColor设置属性__color的值。如果初始化后需要改变属性__color的值，则调用setColor（）方法
        self.__color = color
        print(self.__color)

if __name__ == "__main__":
    color = "red"
    fruit = Fruit(color)  #生成fruit对象，这里调用函数__init__()，并传递变量color的值
    fruit.getColor()      #调用方法，返回__color的值
    fruit.setColor("blue") #调用setColor，重新设置属性__color的值