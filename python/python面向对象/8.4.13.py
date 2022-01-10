#！/usr/bin/python
# -*- coding:utf-8 -*-
#动态更新方法
class Fruit:
    def grow(self):
        print("grow...")

def update():
    print("grow...")

if __name__ == "__main__":
    fruit = Fruit()
    fruit.grow()
    fruit.grow = update #将grow方法更新为update()
    fruit.grow()
