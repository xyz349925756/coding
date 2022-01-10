#!/usr/bin/python   
#例：randrange(start,stop,step)start开始数字、stop结束数字（但不包括结束数字）、step步数
#生成随机数模块，生成的随机数字第一位是start数字，以后的是start+step，以此类推。
#函数命名规则

import random     #导入生成随机数模块random

def compareNum(num1,num2):  #定义了一个函数compareNum(),参数num1,num2为待比较的两个变量。


    if(num1 > num2):    #
        return 1         #  
    elif(num1 == num2):  #
        return 0         #
    else:               #
        return -1       #这段是比较两个数的大小，返回不同结果。
    num1 = random.randrange(1,9)
    num2 = random.randrange(2,10)  #调用random模块的randrange（）函数，返回2个随机数

    print("num1=",num1)    #输出随机数，不同的机器，不同的执行时间返回的随机数不一样。
    print("num2=",num2)
    print(compareNum(num1,num2)) #调用compareNum()函数，并把产生的两个随机数作为参数传入
    
