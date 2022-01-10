#！/usr/bin/python
# -*- coding:utf-8 -*-
class Fruit:
    def __init__(self):
        self.__color = "red"

class Apple(Fruit):
    """this is doc"""
    pass

if __name__ =="__main__":
    fruit = Fruit()
    apple = Apple()
    print(Apple.__bases__)    #代码输出Apple类的父类组成的元组。由于python 支持多重父类，所以可能存在多个父类。
    print(apple.__dict__)     #输出apple对象中属性组成的字典
    print(apple.__module__)   #输出类所在的模块
    print(apple.__doc__)      #输出doc文档