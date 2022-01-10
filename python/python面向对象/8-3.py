# -*- coding:utf-8 -*-
##############################################################################################################
#                                                                                                            #
#                                    类的属性                                                                #
#                                                                                                            #
##############################################################################################################
class Fruit:
    price = 0       #类属性
    def __init__(self):
        self.color = "red"     #实例属性
        zone = "China"         #局部变量
if __name__ == "__main__":
    print(Fruit.price)          #使用类名调用类变量
    apple = Fruit()             #实例化apple
    print(apple.color)          #打印apple实例的颜色
    Fruit.price = Fruit.price + 10              #将类变量加10
    print("apple's price:" + str(apple.price))          #打印apple实例的price
    banana = Fruit()                #实例化banana
    print("banana's price:" + str(banana.price) )    #打印banana实例的price
#python的类和对象都可以访问类属性。