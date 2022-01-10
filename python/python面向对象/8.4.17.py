#！/usr/bin/python
# -*- coding:utf-8 -*-
#多态性
class Fruit:      #父类
    def __init__(self,color = None):
        self.color = color
class Apple(Fruit):      #继承Fruit的子类Apple
    def __init__(self,color="red"):
        Fruit.__init__(self,color)
class Banana(Fruit):     #继承Fruit的子类Banana
    def __init__(self,color="yellow"):
        Fruit.__init__(self,color)
class FruitShop:
    def sellFruit(self,fruit):
        if isinstance(fruit,Apple):  #判断参数fruit的类型
            print("sell apple")     #根据类型做特殊的处理
        if isinstance(fruit,Banana):
            print("sell banana")
        if isinstance(fruit,Fruit):
            print("sell fruit")

if __name__ == "__main__":
    shop = FruitShop()
    apple = Apple("red")
    banana = Banana("yellow")
    shop.sellFruit(apple)
    shop.sellFruit(banana)