# -*- coding:utf-8 -*-
#!/usr/bin/python
#类的创建
class Fruit:     #定义了Fruit的类
    def __init__(self): #构造函数，定义name,color
        self.name = name
        self.color = color
    def grow(self):     #定义grow，类中的函数称为方法
        print("Fruit grow...")

#类的方法必须有一个self参数，但是在方法调用时，可以不传递这个参数

    if __name__ == "__main__":
        fruit = Fruit()
        fruit.grow()
'''这里有问题！！！'''