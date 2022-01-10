#！ /usr/bin/python

###################################################################
#								  #
#								  #
#			tuple列表链接				  #
#								  #
#								  #
###################################################################


list1 = ["apple","banana"]
list2 = ["grape","orange"]
list1.extend(list2)   #list1链接list2（通过extend()来实现）
print(list1)
list3 = ["watermelon"]
list1 = list1 + list3   #list1 +(链接list3)之后赋值给list1
print(list1)
list1 += ["grapefruit"]  #使用"+="给list1连接上["grapefruit"]
print(list1)
list1 = ["apple","banana"] * 2   #*运算符意思是链接两个相同的【“apple”,"banana"】元组
print(list1)
