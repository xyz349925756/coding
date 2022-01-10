#！/usr/bin/python
# -*- coding:utf-8 -*-
#方法的动态特性
class Fruit:
    pass
def add(self):    #定义在类外的函数
    print("grow...")
if __name__ == "__main__":
    Fruit.grow = add   #动态添加add函数
    fruit = Fruit()
    fruit.grow()
