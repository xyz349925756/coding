#！ /usr/bin/python

###################################################################
#								  #
#								  #
#	三引号的另一种用法						  #
#								  #
#								  #
###################################################################

class Hello:   #定义了一个Hello的类
    '''hello class'''  #对Hello类的描述，并被存放到__doc__里面
    def printHello():  #定义printHello 这个方法
        '''print hello world''' #描述了printHello（）方法，并存入__doc__属性中
        print ("hello,world!") 
print(Hello.__doc__)
print(Hello.printHello.__doc__)
