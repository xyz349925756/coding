#！ /usr/bin/python

###################################################################
#								  #
#								  #
#			列表结构					  #
#								  #
#								  #
###################################################################


list = ["apple","banana","grape","orange"]  #创建一个list列表由4个元素构成。
print(list)   
print(list[2]) 
list.append("watermelon")  #添加一个watermelon元素到列表末尾（append（）是添加元素到列表末尾？）
list.insert(1,"grapefruit")#向列表中添加一个元素。这里是把grapefruit插入到指定位置1，也就是列表的第2个位置
print(list) 
list.remove("grape")  #删除列表中grape这个元素
print(list)
#list.remove("a")   从列表中移除"a"这个元素，因为列表中没有这个元素，所以会出现错误提示 ValueError: list.remove(x): x not in list
print(list.pop()) #这里调用了pop()取出列表最后一个元素,这里把watermelon 取出了。（显示watermelon，列表中已经没有这个元素了）
print(list)
