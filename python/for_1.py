#！ /usr/bin/python

###################################################################
#								  #
#								  #
#			for循环					  #
#								  #
#								  #
###################################################################

#class range(object)
#     range(stop) -> range object
#range(start,stop[,step]) -> range object

#range()函数声明。

for x in range(-1,2):
#range(-1,2)生成的列表返回的3个数-1.0.1每次循环变量x的值依次是-1,0,1
    if x > 0 :
        print("正数:",x)
    elif x == 0 :
        print("零：",x)
    else:
        print("负数：",x)
else:
    print("循环结束")



for x in range(0,5,2):
    print(x)


x = int(input("输入x的值："))
y = 0
for y in range(0,100):
    if x == y:
        print("找到数字:",x)
        break
    else:
        print("没有找到")
