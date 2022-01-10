# -*- coding:utf-8 -*-
#__str__()
class Fruit:
    '''Fruit类'''
    def __str__(self):   #定义对象的字符串表示
        return self.__doc__  #返回hearedoc

if __name__ == "__main__":
    fruit = Fruit()
    print(str(fruit))   #调用__str__
    print(fruit)        #与第8行代码结果相同
