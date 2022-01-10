#!/usr/bin/python
#-*-coding:utf-8-*-
"""形参和实参"""
def myFristFunction(name):  #name就是形式参数
    print(name)
    
myFristFunction("小贱人")   #小贱人就是实际参数

"""函数文档"""
def mySecondFunction(doller):
    """
    人民币对美元的汇率为6.5
    """
    return doller * 6.5
print(mySecondFunction(100))
print(mySecondFunction.__doc__)
help(mySecondFunction)

def saySomething(name,words):
    print(name + "--->" + words)
saySomething("python","love")
saySomething("love","python")
#上面就是位置参数，更改了位置意义就变了。
saySomething(name = "python",words = "love")
saySomething(words = "love",name = "python")
#这里就是关键字参数，不会随着位置改变意义而改变

def saySomething(name = "python ",words = " very good"):  #这里是默认参数，就不是关键字参数了。
    print(name + '--->' + words)    
saySomething()               #因为有默认参数所以这里调用就不需要实参。
saySomething(words = "fuck",name = "python")

def test(*params):
    print("有%d个参数"%len(params))
    print("第二个参数",params[1])
test('a','b','c','d','e','f')

def test(*params,next = 9):
    print("这是可变参数：",params)
    print("这是默认参数：",next)
    
test(1,2,3,4,5,6,7,8,9)

def test(*params):
    print("这是可变参数!!",params)
a = [1,2,3,4,5,6,7,8]
test(*a)