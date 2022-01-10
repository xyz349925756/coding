#！ /usr/bin/python

###################################################################
#								  #
#								  #
#		    	元素的遍历	         		  #
#								  #
#								  #
###################################################################

tuple = (("apple","banana"),("grape","orange"),("watermelon",),("grapefruit",))
for i in range(len(tuple)):
    print("tuple[%d] :"% i,"",)
    for j in range(len(tuple[i])):
        print (tuple[i][j],"",)
    print()
#第一行代码创建了一个4个子元组组成的二元元组tuple
#2-6行代码遍历tuple元组，输出元组中各个元素的值。

#还可以用for 。。。in语句遍历

tuple = (("apple","banana"),("grape","orange"),("watermelon",),("grapefruit",))
for i in tuple:
    for j in i:
        print(j)

#1行创建了一个4个子元组组成的二元元组tuple
#第2行遍历tuple 元组
#第三行遍历tuple 子元组
#第四行 依次打印出各元素
