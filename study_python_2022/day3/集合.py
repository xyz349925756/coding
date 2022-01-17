#!/usr/bin/python3
# -*-coding:utf-8-*-
# Time    :2022/1/15  20:58
# Author  :xyz34
# Email   :xyz349925756@hotmail.com
# File    :集合.py
# Project :coding

set1 = {1,2,3,3,4,5,2,1}
set2 = {3,4,5,6,7}

print(set1,set2)
#交集
print(set1.intersection(set2)) #交集
print(set1 & set2)

#并集
print(set1.union(set2))
print(set1 | set2)

#反交集-除交集以外的其他元素
print(set1 ^ set2)
print(set1.symmetric_difference(set2))

#差集-前者独有的
print(set1 - set2)
print(set1.difference(set2))
print(set2 -set1)

set3 = {1,2,3,4,5,6}
set4 = {1,2,3,4,5,6,7,8,9}
#子集-set3被set4包含 set3就是set4的子集
print(set3 < set4)
print(set3.issubset(set4))

#超集-set4包含set3，set4就是set3的超集
print(set4 > set3)
print(set4.issuperset(set3))

#可变集合类型 set
s1 = set('abcdefg')
print(s1,type(s1))

#只读集合类型 frozenset 就是集合放到元组里面
s2 = frozenset('abcd')
print(s2)

#增
s1.add('opq')  #添加一个元素，不是迭代
print(s1)

s1.update('wq') #迭代添加
print(s1)

#删
s1.pop() #随机删除
print(s1)

s1.remove('opq') #删除指定的
print(s1)

# print(s1.clear()) #清空

# del s1  #删除集合

#集合是无序所以不能改

for i in s1:
    print(i)


