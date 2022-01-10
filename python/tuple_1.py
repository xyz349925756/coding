#！ /usr/bin/python

###################################################################
#								  #
#								  #
#		        tuple索引分片、负数索引			  #
#								  #
#								  #
###################################################################

tuple = ("apple","yellow","orage","banana","blue")
print(tuple[-1])
print(tuple[-2])
tuple2 = tuple[1:3]   #分片，第二个元素到第三个（不包括第四个元素）
tuple3 = tuple[0:-2]   #分片，第一个元素到倒数第二个元素，不包括倒数第二个元素
tuple4 = tuple[2:-2]   #分片，从第三个元素到倒数第二个元素。
print(tuple2)
print(tuple3)
print(tuple4)



fruit1 = ("apple","yellow")
fruit2 = ("blue","orange")
tuple = (fruit1,fruit2)  #创建复合元组tuple
print(tuple)  
print("tuple[0][1] = ",tuple[0][1]) #访问tuple复合元组中第1个元素中的第2个元素 yellow。
print("tuple[1][1] = ",tuple[1][1]) #访问tuple复合元组中第2个元素中的第二个元素 orange。
#print("tuple[1][1] = ",tuple[1][2])  #访问tuple复合元组中第2个元素中的第三个元素，这里没有第三个元素。提示错误
#tuple index out of range

#元组打包
tuple = ("apple","banana","grape","orange")
#元组解包
a,b,c,d = tuple
print(a,b,c,d)
