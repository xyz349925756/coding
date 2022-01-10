#！ /usr/bin/python

###################################################################
#								 	  #
#									  #
#	      关于列表、堆栈、队列中	append()、pop()	中的说明			  #
#									  #
#									  #
###################################################################
#列表
list = ["apple","grape","banana"]
print("这是列表：",list)
print("这是列表第2个元素",list[1])
list.append("orange")
print("向列表末尾添加元素orange后：",list)
list.insert(1,"blue")
print("列表第2位添加blue元素",list)
list.remove("blue")
print("删除列表中的blue元素之后的列表",list)
list.pop()
print("弹出默认元素",list)
print("用index查找出指定元素grape的位置:",list.index("grape"))
print("判断元素是否在列表中",("apple" in list))
list.sort()
print("正向排序，按字母顺序排序的:",list)
list.reverse()
print("反向排序：",list)

print('*****************************列表***************************************')

    
#堆栈
list = ["apple","grape","banana"]
list.append("orange")
print("向堆栈顶部添加一个元素orange",list)
print("从堆栈中弹出最后输入的元素orange：",list.pop())
print("最终的堆栈元素",list)

print('*******************************堆栈*************************************')


#队列
list = ["apple","banana","grape"]              
list.append("orange")      
print("向队列中添加orange元素：",list)               
print("弹出的元素：",list.pop(0))  
print("最终队列：",list)

print('*******************************队列*************************************')


#由上面可以看出append() 效果是一样的都是最后添加元素，不同的是堆栈里面是顶部添加，队列是
#末尾添加。
#pop()只是在列表和堆栈中是默认没有值的。列表是最后一个元素，堆栈是最顶部元素
#pop(0) 是在队列中使用目的是移除队列0位置的元素。
