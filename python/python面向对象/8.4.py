#！/usr/bin/python
# -*- coding:utf-8 -*-
#访问私有属性
class Fruit:
    def __init__(self):
    self.__color = "red"    #私有变量使用下划线开始的名称
#定义了私有属性__color
if __name__ == "__main__":
    apple = Fruit()         #实例化apple
    print(apple._Fruit__color)     #调用类的变量
#输出私有属性__color的值

