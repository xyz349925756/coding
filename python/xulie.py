#！ /usr/bin/python

###################################################################
#								 	  #
#									  #
#			                    序列					  #
#									  #
#									  #
###################################################################

tuple = ("apple","banana","grape","orange")
list = ["apple","banana","grape","orange"]
str = "apple"
print("这个程序是序列的索引")
print(tuple[0])
print(tuple[-1])
print(list[0])
print(list[-1])
print(str[0])
print(str[-1])
print("#####################################################")

#分片操作
tuple = ("apple","banana","grape","orange")
list = ["apple","banana","grape","orange"]
str = "apple"
print("分片操作")
print(tuple[:3])
print(tuple[3:])
print(tuple[1:-1])
print(tuple[:])
print(list[:3])
print(list[3:])
print(list[1:-1])
print(list[:])
print(str[:3])
print(str[3:])
print(str[1:-1])
print(str[:])

#这里[:3]意思是从序列第1个元素到第三个元素的值。
#这里[3:]意思是序列第3个元素到最后一个元素的值。
#【：】意思是整个序列的值
