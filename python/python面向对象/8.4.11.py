# -*- coding:utf-8 -*-
#__call__()
class Fruit:
    class Growth:    #内部类
        def __call__(self):   #实现了__call__()方法
            print("grow...")
    grow = Growth()     #返回__call__的内容

if __name__ == "__main__":
    fruit = Fruit()
    fruit.grow()       #使用实例调用
    Fruit.grow()       #使用类名调用