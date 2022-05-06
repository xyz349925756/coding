#!/usr/bin/python3
# -*-coding:utf-8-*-
# Time    :2022/1/15  14:34
# Author  :xyz34
# Email   :xyz349925756@hotmail.com
# File    :字典.py
# Project :coding

# info = {
#     "name": "wangwu",
#     "age": 32,
#     "address": "yunnan kunming"
# }
# print(info)
# print(type(info))
# # key:values  key是唯一，无序，查询快
#
# info["names"] = 'jack'  #添加key values
# print(info)
#
# mes = {'alex': [32, 'CEO', 70000], 'jack': [45, 'CTO', 8000], 'names': [29, 'worker', 5999]}
# print(mes)
#
# del mes['names'] #删除指定key
# print(mes)
#
# mes.pop('alex')  #删除指定key
# print(mes)
#
# mes.clear()  #清空
# print(mes)
#
# info['age'] = 44  #修改values,不存在就是添加操作了
# print(info)
#
# #print(mes['alex'])  #返回字典中key 对应的values ，不存在的key 报错
# print(mes.get('a', None)) #获取字典中key 对应的values，不存在返回默认值None，避免报错
# print('alex' in mes)  #判断key是否在字典中
# print(mes.keys())  #返回字典中所有的key list
# print(mes.values())  #返回字典中所有的values 列表
# print(mes.items())  #返回包含所有key values的list   字典转list
#
# for k,v in mes.items():  #遍历
#     print(k,v)
#
# for k in mes:     #遍历key 最快
#      print(k)
#
# print(len(mes))  #len方法同时用于列表，字符串

dict = {1:'no1','name':'wangwu','age':33,'adr':'云南'}
# print(type(dict))
# print(dict['age'])
# print(dict.get('adr'))
# dict['age']=35
# print(dict)
# dict['work'] = 'IT'
# print(dict)
# print(dict)
# del dict[1]
# print(dict)
#
# dict.pop('adr')
# print(dict)

# dict.popitem()
# print(dict)

# dict.clear()
# print(dict)
# print(dict.get(1))

# print(dict.items())
# d1 = dict.copy()
# print(d1)

# d1 = {'work':"it","公司":"xxx科技公司"}
#
# dict.update(d1)
# print(dict)

# print(dict.keys())
# print(dict.values())
# d2 = dict.fromkeys('12345','it')
# d3 = dict.fromkeys('test','none')
# print(d3)

# d4 = dict.setdefault('node')
# print(d4)
# dict.setdefault('work','It')
# dict.setdefault('work2',)
# dict.setdefault('work3')
#
# print(dict)

# print(len(dict))
# print(dict)
# print('name' in dict.keys())
# # print(dict['name'])
# print(dict['name'] not in dict.values())

# for key in dict.keys():
#     print(key)
#
# for value in dict.values():
#     print(value)
#
# for key,value in dict.items():
#     print("key : %s,value : %s"%(key,value))
# i = 0
# for key,value in dict.items():
#     print("dict[%d] = %s" % (i,value))
#     i += 1

# i = 0
# while i < len(dict):
#     for key,value in dict.items():
#         print("dict[%d] is %s = %s" % (i,key,value))
#         i += 1

#
# for i,key in enumerate(dict):
#     print("索引位置：dict[%d]  key = %s ,value = %s" % (i,key,dict[key]))

# ensurepip  encodings  enumerate

print(max('hello','world'))