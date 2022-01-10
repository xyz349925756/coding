#！/usr/bin/python
# -*- coding:utf-8 -*-
#抽象基类
from abc import ABCMeta,abstractclassmethod   #引入所需的module
class Fruit(metaclass=ABCMeta):    #抽象类
    @abstractclassmethod   #使用@abstractmethod修饰器定义抽象函数
    def grow(self):
        pass

class Apple(Fruit):
    def grow(self):    #子类中必须重写抽象函数
        print("Apple growing")

if __name__ == "__main__":
    apple=Apple()
    apple.grow()
