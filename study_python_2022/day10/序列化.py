#!/usr/bin/python3
# -*-coding:utf-8-*-
# Auth: xyz34
# File: 序列化.py
# TIME: 5月  星期一

# json
# import json
# json_res = json.dumps([1,'abc',True,False])   # 序列化
# print(json_res,type(json_res))
#
# l = json.loads(json_res)  # 反序列化
# print(l,type(l))
import json

d = {'a':'张三', 'c': True, 'e': 10, 'b': 11.1, 'd': None, 'f': [1, 2, 3], 'g':(4, 5, 6)}
# res = json.dumps(d,sort_keys=True)
# res = json.dumps(d,sort_keys=True,indent=4)
# res = json.dumps(d,separators=(',',':'))
# res = json.dumps(d,ensure_ascii=False)
# res = json.dumps(d)
# print(res)

# json_res = json.loads(res)
# print(json_res)


# 序列化到文件中

# with open('json_res.txt','wt',encoding='utf-8') as f1:
#     json.dump(d,f1,indent=4,ensure_ascii=False)

# with open('json_res.txt','r',encoding='utf-8') as f2:
#     print(json.load(f2))

# class Student(object):
#
#     def __init__(self,name,age,sno):
#         self.name = name
#         self.age = age
#         self.sno = sno
#
#     def __repr__(self):
#         return 'Student [name: %s, age : %d ,sno: %d]' % (self.name,self.age,self.sno)
#
#
#
#
# class MyJSONEncoder(json.JSONEncoder):
#     def default(self, obj):
#         d = {}
#         d['__class__'] = obj.__class__.__name__
#         d['__module__'] = obj.__module__
#         d.update(obj.__dict__)
#         return d
#
#
# class MyJSONDecoder(json.JSONDecoder):
#     def __init__(self):
#         json.JSONDecoder.__init__(self, object_hook=self.dict2obj)
#
#     def dict2obj(self, d):
#         if '__class__' in d:
#             class_name = d.pop('__class__')
#             module_name = d.pop('__module__')
#             module = __import__(module_name)
#             class_ = getattr(module, class_name)
#             args = dict((key.encode('ascii'), value) for key, value in d.items())
#             instance = class_(**args)
#         else:
#             instance = d
#         return instance
#
#
# stu = Student('bob',23,222)
# print(stu)
#
# # json.dumps(stu)
# #方式一：直接调用子类MyJSONEncoder的encode()方法进行序列化
# print(MyJSONEncoder().encode(stu))
# print(MyJSONEncoder(separators=(',', ':')).encode(stu))  # 去空格
#
# # 方式二：将子类MyJSONEncoder作为cls参数的值传递给json.dumps()函数
# print(json.dumps(stu, cls=MyJSONEncoder))
# print(json.dumps(stu, cls=MyJSONEncoder, separators=(',', ':')))
#
# # 反序列化
# MyJSONDecoder().decode(json.dumps() #



import pickle
var_a = {'a':'str', 'c': True, 'e': 10, 'b': 11.1, 'd': None, 'f': [1, 2, 3], 'g':(4, 5, 6)}
res = pickle.dumps(var_a)

print(res)

res1 = pickle.loads(res)
print(res1)