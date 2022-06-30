#!/usr/bin/python3
# -*-coding:utf-8-*-
# Auth: xyz34
# File: oop_2.py
# TIME: 2022/6/16 星期四  周四

# class Stu(object):
#
#     school = "湘北高中"
#
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         msg = f"""{self.name} 正在接受训练"""
#         print(msg)
#
#     @classmethod
#     def sport(cls):
#         print(f"{cls.school} 篮球部的同学都在接受训练!")
#
#     @staticmethod
#     def clean():
#         print("观众")
#
#
# stu = Stu('流川枫',17)
# stu.__str__()   # 通过实例调用实例方法
# Stu.__str__(stu)  #通过类调用实例方法
#
#
# Stu.sport()   # 通过类调用类方法
# stu.sport()   # 通过实例调用类方法
#
# Stu.clean()   # 通过类调用静态类
# stu.clean()   # 通过实例调用静态类
#
# print(stu.school)   # 通过实例访问类属性
#
# stu.school = '海南附中'   # 添加一个实例属性，类属性并不会被修改
# print(stu.school)    # 实例属性
# print(Stu.school)    # 类属性


# class Student:
#     # 类变量
#     number = 0
#
#     # 类属性
#     def __init__(self,name,score):
#         self.name = name
#         self.__score =  score
#         Student.number += 1 #
#         # self.__class__.number += 1  # 等效上面
#
#     # 定义打印方法
#     @property  # 把print_info 方法伪装成属性
#     def print_info(self):
#         print(f"""Name:{self.name}  Age:{self.__score}""")
#
#     @classmethod   # 定义类方法，打印学生数量
#     def total(cls):
#         print(f"""合计: {cls.number} 个学生""")
#
#
# st1 = Student('tom',98)  # 实例化 创建对象
# st2 = Student('bob',100)
# #
# st1.print_info()  # 实例调用类方法
# st2.print_info()
# st1.print_info  # 使用了propert 实例化调用就不需要加()
#
# Student.total()

# 创建父类 学校成员
class SchoolMember:
    num = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age
        SchoolMember.num += 1

    def print_info(self):
        print( f"""Name:{self.name} Age:{self.age}""")

    @staticmethod
    def sum_i():
        print("静态装饰器")

    @classmethod
    def sum_s(cls):
        print(cls.num)

# 创建教师子类
class Teacher(SchoolMember):

    def __init__(self,name,age,salary):
        # SchoolMember.__init__(self,name,age)  # 利用父类初始化
        super().__init__(name,age)
        self.salary = salary

    def print_info(self):
        # SchoolMember.print_info(self)
        super().print_info()
        print(f"""salary:{self.salary}""")

# 创建学生子类
class Student(SchoolMember):

    def __init__(self,name,age,score):
        SchoolMember.__init__(self,name,age)
        self.score = score

    def print_info(self):
        SchoolMember.print_info(self)
        print(f"""score:{self.score}""")

teacher1 = Teacher('李四',55,20000)
student1 = Student('张三',15,98)

teacher1.print_info()
student1.print_info()

SchoolMember.sum_i() # 静态方法
SchoolMember.sum_s() # 类方法

# print(Teacher.mro())
# print(SchoolMember.mro())