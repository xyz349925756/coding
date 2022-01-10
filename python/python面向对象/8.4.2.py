#！/usr/bin/python
# -*- coding:utf-8 -*-
#################################################################
#							类的方法           	             	#
#################################################################
class Fruit:
    price = 0

    def __init__(self):
        self.__color__ = "red"

    def getColor(self):     #定义公有方法getColor()，获取__color的值
        print(self.__color__)   #这里注意，self.__color__是上面私有的变量

    @ staticmethod   #使用@staticmethod修饰器静态方法
    def getPrice():  #定义getPrice（），该方法没有self参数。
        print(Fruit.price)

    def __getPrice():     #定义了方法__getPrice,该方法并没有提供参数self  ，定义私有函数
        Fruit.price = Fruit.price + 10
        print(Fruit.price)

    count = staticmethod(__getPrice)   #使用staticmethod方法定义静态方法

if __name__ == "__main__":
    apple = Fruit()   #实例化apple
    apple.getColor()   #使用实例调用静态方法
    Fruit.count()     #使用类名调用静态方法
    banana=Fruit()
    Fruit.count()
    Fruit.getPrice()


#类方法，是将类本身作为操作对象的方法
#把上述静态方法修改为类方法
@ classmethod
def getPrice(cls):
    print(cls.price)
def __getPrice(cls):
    cls.print = cls.price + 10
    print(cls.price)

count = classmethod(__getPrice)

