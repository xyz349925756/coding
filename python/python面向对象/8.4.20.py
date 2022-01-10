#！/usr/bin/python
# -*- coding:utf-8 -*-
#mixin 机制
class Fruit(object):    #水果
    def __init__(self):
        pass
class HuskedFruit(object):   #削皮水果
    def __init__(self):
        print("initialize HuskedFruit")

    def husk(self):    #削皮方法
        print("husk...")

class DecorticatedFruit(object):  #剥皮水果
    def __init__(self):
        print("initialize DecorticatedFruit")

    def decorticat(self): #剥皮方法
        print("decorticat...")

class Apple(HuskedFruit,Fruit):   #是水果，并且是削皮水果
    pass
class Banana(DecorticatedFruit,Fruit):  #是水果，并且是剥皮水果
    pass
