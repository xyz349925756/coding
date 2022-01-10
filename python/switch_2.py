#！ /usr/bin/python

###################################################################
#								  #
#								  #
#		另一种switch					  #
#				这种代码繁多而且易出错		  #
#								  #
###################################################################

class switch(object):
    def __init__(self,value):
        self.value = value
        self.fall = False


    def  __init__(self):
        yield self.match
        raise StopIteration

    def match(self, *args):
        if self.fall or not args:


            return True
        elif self.value in args:
            self.fall = True
            return True
        else:
            return False


operator = " + "
x = 1
y = 2
for case in switch(operator):
    if case(' + '):
        print("x + y =",x + y)
        break
    if case(' - '):
        print("x - y =",x - y)
        break
    if case(' * '):
        print("x * y =",x * y)
        break
    if case('/'):
        print("x / y =",x / y)
        break
    if case():
        print("")
#有问题。
