#!/usr/bin/python
#-*-coding:utf-8-*-
"""列表的方法
 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
"""
from filecmp import clear_cache

list = [1,2,3,4,5,6,7,8,9,10]
for i in range(1,5):
    list.append(i)
print("LIST =",list)
"""
向列表中添加元素，每次一个,
"""
list.clear() #删除列表所有的元素。
print("LIST =",list)

list1 = [1,2,3,4,5,6,7,8,9,10,1]
list2 = []
list2 = list1.copy()
print("list2 =",list2)

print("list1 =",list1.count(1))

list3 = [7,8]
list1.extend(list3)
print("list1 =",list1)

start = list1.index(1) + 1
stop = len(list1)
list1.index(1,start,stop)
print("list1.index =",list1.index(1,start,stop))

list1.reverse()
print("list1 =",list1)

list1.sort()
print("list1 =",list1)

list1.sort(key=None, reverse=True)
print("list1 =",list1)

list4 = list1[:]
print("list4 =",list4)