#！ /usr/bin/python

###################################################################
#								  #
#								  #
#			Tuple的使用				  #
#								  #
#								  #
###################################################################

list = ["apple","banana","grape","orange"]
print(list[-2])
print(list[1:3])
print(list[-3:-1])
'''遍历二元列表'''
list = [["apple","banana"],["grape","orange"],["watermelon"],["grapefruit"]]
for i in range(len(list)):
    print("list[%d] :" % i ,"",)
    for j in range(len(list[i])):
        print(list[i][j],"",)
    print()

#for...in 遍历二元列表
