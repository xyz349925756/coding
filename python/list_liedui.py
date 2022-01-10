#！ /usr/bin/python

###################################################################
#								 	  #
#									  #
#			队列的实现					  #
#									  #
#									  #
###################################################################

list = ["apple","banana","grape"]               #用列表来创建一个队列
list.append("orange")       #添加一个队列元素，orange
print(list)                 #['apple', 'banana', 'grape', 'orange']
print("弹出的元素：",list.pop(0))  #弹出一个队列元素并输出【弹出的元素： apple】
print(list)                    #['banana', 'grape', 'orange']
#由上面实例得出。在列队队尾添加orange元素，之后再弹出pop（0）这个元素。
#发现是0号元素被移除，
#list.pop(0)  这里 不加0  默认是弹出队尾的元素。注意队列必须是pop(0)  才是队列，不然就是列表了。
