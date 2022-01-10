#！/usr/bin/python
# -*- coding:utf-8 -*-
#内部类的使用
class Car:
    class Door:       #定义内部类
        def open(self):    #定义了Door类的方法
            print("open door")
    class Wheel:        #定义内部类
        def run(self):      #定义了内部类wheel的方法
            print("car run")

if __name__ == "__main__":
    car = Car()          #实例化Car
    backDoor = Car.Door()     #内部实例化方法一：创建了Door类的实例backDoor。这里使用类名前导的方式创建。
    frontDoor = Car.Door()    #内部实例化二：创建了Door类的实例frontDoor。这里使用对象名前导的方式创建。
    backDoor.open()
    frontDoor.open()
    wheel = Car.Wheel()
    wheel.run()