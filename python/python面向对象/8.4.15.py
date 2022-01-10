#！/usr/bin/python
# -*- coding:utf-8 -*-
#使用到super()调用父类
class Fruit(object):   #定义基类，继承自object,python3.x中这不是必须的
    def __init__(self):
        print("parent")
class Apple(Fruit):
    def __init__(self):
        super(Apple,self).__init__()  #使用super()调用父类，更直观
        print("child")

if __name__ == "__main__":
    Apple()

