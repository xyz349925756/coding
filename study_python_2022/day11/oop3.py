#!/usr/bin/python3
# -*-coding:utf-8-*-
# Auth: xyz34
# File: oop3.py
# TIME: 2022/6/17 星期五  周五

# class Stu:
#     '''这是一个学生信息类'''
#
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f'姓名：{self.name}  年龄：{self.age}'
#
# # print('打印说明注释：',Stu.__doc__)
# stu1 = Stu('Tom',29)
# print(stu1)


#
# # print(stu1.__module__)
# # print(stu1.__class__)
#
# del stu1


# class Foo:
#
#     def __del__(self):
#         print(f'释放{__file__}')
#
# obj = Foo()
#
# del obj

# class Foo:
#
#     def __init__(self):
#         pass
#
#     def __call__(self, *args, **kwargs):
#         print('__call__')
#
# obj = Foo()
# obj()
# print(obj)  # 内存地址
#
# print(callable(obj))  # 判断一个对象是否可以被执行


# class Stu:
#
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def fun1(self,*args,**kwargs):
#         print('fun1')
#
# print(Stu.__dict__)
#
# st1 = Stu('tom',29)
# print(st1.__dict__)
#
# st2 = Stu('jack',45)
# print(st2.__dict__)

# class Stu:
#     """stu"""
#
#     def __getitem__(self, item):
#         print('__getitem__',item)
#
#     def __setitem__(self, item, value):
#         print('__setitem__',item,value)
#
#     def __delitem__(self, item):
#         print('__delitem__',item)
#
# obj = Stu()
# res = obj['k1']   # 触发getitem
# obj['k1'] = 'tom'  # 触发setitem
# del obj['k1']   # 触发delitem

# class func1:
#
#     def __init__(self,item):
#         self.item = item
#
#     def __iter__(self):
#         return iter(self.item)
#
# obj = func1([1,4,2,7])
#
# for i in obj:
#     print(i)

# class Fun1:
#
#     def __init__(self):
#         pass
#
#     def __iter__(self):
#         yield 1
#         yield 2
#         yield 3
#
# obj = Fun1()
# for i in obj:
#     print(i)

# class F1:
#
#     def __init__(self,str):
#         self.str = str
#
#     def __len__(self):
#         return len(self.str)
#
# obj = F1('hello')
# print(len(obj))

# class Stu:
#
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     # def __str__(self):
#     #     return f"""Name:{self.name} Age:{self.age}"""
#
#     # __repr__ = __str__
#     def __repr__(self):
#         return f"""Name:{self.name} Age:{self.age}"""
#
# s = Stu('tom',33)
# print(s)

# class Operation:
#     a = 3
#     def __init__(self,a):
#         self.a = a
#
#     __annotations__ = 'vking'
#
# o = Operation(5)
# o.a = 7
# print('实例变量：',o.a,'类属性：',Operation(1).a,'类变量:',Operation.a)
# print('加',o.a.__add__(5))
# print('减',o.a.__sub__(3))
# print('乘',o.a.__mul__(2))
# print('除',o.a.__truediv__(2))
# print('求余',o.a.__mod__(3))
# print('冥',o.a.__pow__(2))
# print('等',o.a.__eq__(7))
# print('等',o.a.__eq__(17))
# print('大于',o.a.__ge__(7))  # o.a 的值大于 7 为true
# print('大于',o.a.__gt__(8))    # 反之为false
# print('小于',o.a.__le__(6),o.a.__lt__(8))  # 7 小于6   7小于8
# print('不等于',o.a.__ne__(6),o.a.__ne__(7))
# print('列出内置方法',o.a.__dir__())
# print('右侧重载',o.a.__radd__(-2))
# # 注意：__rodd_＿中的顺序与之相反：self是每的右侧，other是在左侧。每个二元运算符都有类似的右侧重载方法（例如__mul__和__rmul__）
# print('生成类变量字典',o.__dict__)
# print(o.__annotations__)

# class St:
#
#     __slots__ = ('name','age')
#
#     pass
#
#     # def __init__(self,name,age):
#     #     self.name = name
#     #     self.age = age
#
# s1 = St('tom',18)
# s1.name = 'toms'
# s1.age = 25
# # s1.x = 33

# class Hello:
#
#     def __init__(self,name):
#         self.name = name
#
#     def f_print(self):
#          print(f"Hello,{self.name}")
#
# # print(Hello.__dict__)
#
# t = Hello('张三')
# fprint = getattr(t,'f_print')
# fprint()
#
# age = getattr(t,'age',33)
# print(age)

# score = getattr(t,'score')
# print(score)


# class Person:
#
#     def __init__(self,name):
#         self.name = name
#
#     def infos(self):
#         print(self.name)
#
# for k,v in Person.__dict__.items():
#     print(k,':',v)
#
# a = Person('张三')
#
# f = getattr(a,'infos')
# f()
#
# print(hasattr(a,'name'))
# print(hasattr(a,'age'))

# class Person:
#
#     def __init__(self,name):
#         self.name = name
#
#     def hello(self):
#         print(f"你好,{self.name}")
#
# def get_info(self):
#     print(f"姓名：{self.name}   年龄：{self.age}")
#
# for k,v in Person.__dict__.items():
#     print(k,":",v)
#
# setattr(Person,'get_info',get_info)
#
# p = Person('张三')
# p.hello()
#
# setattr(p,'age',33)
# p.get_info()

# class Person:
#
#     def __init__(self,name,age):
#         self.name = name
#         self.age = 33
#
#     def hello(self):
#         print(f"Hello {self.name}")
#
#     def get_info(self):
#         print(f"name: {self.name}  age: {self.age}")
#
#
# print(Person.__dict__)
#
# p = Person('张三',33)
#
# delattr(p,'age')
# p.get_info()
#
# print(p.__dict__)


# class Stu:
#
#     def __init__(self,name):
#         self.name = name
#
#     def __str__(self):
#         return f"Name:{self.name}"
#
#     def __del__(self):
#         print('已经回收')
#
#
# s = Stu('tom')
# print(s)
# print(s.__str__())

#
# print(type(0))     # <class 'int'>
# print(type(int))   # <class 'type'>
# print(type('abcdefg'))  # <class 'str'>
# print(type(str))   # <class 'type'>
# print(type([1,2,3]))  # <class 'list'>
# print(type(list))    # <class 'type'>
# print(type({1:'a',2:'b'}))   # <class 'dict'>
# print(type(dict))   # <class 'type'>
#
# class Stu:
#     pass
#
# s = Stu()
# print(type(s))   # <class '__main__.Stu'>
# print(type(Stu))  # <class 'type'>
# print(type(type))  # <class 'type'>


# class Stu:
#
#     def __init__(self):
#         self.name = 'Tom'
#
# print(Stu)
# s = Stu()
# print(s.name)


# Ss = type('Ss',(),{'name':'Bob'})
# print(Ss)
# s1 = Ss()
# print(Ss.name)

# class Student_info(type):
#
#     def __init__(cls,name,bases,dict):
#         super().__init__(name,bases,dict)
#
#         cls.int_attrs = {}
#
#         for k,v in dict.items():
#             if type(v) is int:
#                 cls.int_attrs[k] = v
#
# class St(metaclass=Student_info):
#
#     pass
#     def __init__(cls,name,*args,**kwargs):
#         super().__init__()
#
#
# # St = Student_info('St',(),{'name':'Tom','age':34,'level':3,'introduction':'Python全栈编程'})
# print(St)  #<class '__main__.St'>
# st = St()
# print(st.name)  # Tom
# print(st.int_attrs) #{'age': 34, 'level': 3}

# print(type(int))
# print(type(dict))
# print(type(set))
# print(type(tuple))
# print(type(list))

# class Stu:
#
#     pass
#
# def new(cls):
#     obj = object.__new__(cls)
#     obj.num = 20
#     return obj
#
# Stu.__new__ = new
#
# s = Stu()
# print(s.num)


# class StuMeta(type):
#
#     def __new__(cls, name,bases,dct):
#         obj = super().__new__(cls,name,bases,dct)
#         obj.num = 100
#         return obj
#
# class F(metaclass=StuMeta):
#     pass
#
# print(F.num)
#
# # 父类
# class Father():
#
#     def foo(self):
#         return self.bar()
#
# # 用户子类
# class Child(Father):
#
#     def bar(self):
#         return True

# class Meta(type):
#     def __new__(cls,name,bases,dct, **kwargs):
#         if name != 'Father' and 'bar' not in dct:
#             raise TypeError('Class must contain bar() method.')
#         return super().__new__(cls,name,bases,dct,**kwargs)
#
# # 添加了元类
# class Father(metaclass=Meta):
#
#     def __init__(self):
#         pass
#
#     def foo(self):
#         return self.bar()
#
# # 用户子类
# class Child(Father):
#
#     def bar(self):
#         return "bar"
#
#
# print(Child)

# 自定义一个元类
# class Meta(type): # 只有继承了type类的类才是元类
#
#     def __call__(self, *args, **kwargs):
#         obj = self.__new__(self)    # call 会先调用People的__new__方法
#         self.__init__(obj,*args,**kwargs)  # call会先调用People的__init__方法
#         # print('元类',obj.__dict__)
#         obj.__dict__['age'] =  '50'  # 初始化
#         return obj   # call返回一个初始化好的对象

# 类的产生
# People = Meta（）   -->   type.__call__ --> 3件事
# 1、type.__call__ 函数调用Meta内的__new__
# 2、type.__call__ 函数调用Meta内的__init__
# 3、type.__call__ 函数返回一个初始化好的对象


# class People(metaclass=Meta):
#
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def say(self):
#         print(f"{self.name}:{self.age}")
#
#     def __new__(cls, *args, **kwargs):
#         # 产生真正的对象
#         return object.__new__(cls)
# # obj=People（'name',age）  ->   Meta.__call__ -> 3件事
# # 1、Meta.__call__ 函数调用People内的__new__
# # 2、Meta.__call__ 调用People内的__init__
# # 3、Meta.__call__ 返回一个初始化好的对象
#
# obj1 = People('Tom',68)
# obj2 = People('bob',88)
#
# print(obj1.__dict__)
# print("".center(50,"-"))
# print(obj1)
# print("".center(50,"-"))
# print(obj2.__dict__)
# print(obj1.name,obj1.age)

class Mymeta(type):
    a = 1
    def __call__(self, *args, **kwargs):
        obj = self.__new__(self)
        print(self.__new__ is object.__new__)
        self.__init__(obj,*args,**kwargs)
        return obj

class Bar(object):
    a = 2
    # def __new__(cls, *args, **kwargs):
    #     print('Bar__new__')

    pass

class Foo(Bar):
    # a = 3
    # def __new__(cls, *args, **kwargs):
    #     print('Foo.__new__')
    pass

class Stu(Foo,metaclass=Mymeta):
    # a = 4
    def __init__(self,name,age):
        self.name = name
        self.age = age

obj = Stu('Tom',45)
print(obj.__dict__)
print(obj.a)  # 查找a的顺序就是 从对象往类，再到父类去寻找，并不会到元类去寻找。父类里面没有就抛出异常
# print(Stu.a)  # 等同于上面那条命令