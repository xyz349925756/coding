#!/usr/bin/python3
# -*-coding:utf-8-*-
# Auth: xyz34
# File: oop面向对象.py
# TIME: 2022/6/12 星期日  周日

# class Student(object):
#
#     def __init__(self,name,age,job):
#         self.name = name
#         self.age =age
#         self.job = job
#
#     def print_stu_info(self):
#         # print('姓名：{name} 年龄：{age} 职业:{job}'.format(name=self.name,age=self.age,job=self.job))
#         print('姓名：%s  年龄：%d  职业：%s'%(self.name,self.age,self.job))
#         print("类方法中的内存地址：",id(self))
#
# print(Student.__name__)
# print(__file__)
#
#
# stu = Student('张纳',33,'IT')
# print("".center(20,"-"))
# stu.print_stu_info()
#
# print("实例化的内存地址：",id(stu))

# contest = []
# with open('sco.txt','r',encoding='utf-8') as f:
#     lines = f.readlines()
#     for i in range(1,len(lines)):
#         line = lines[i].strip()  # 提取到列表
#         contest.append(line)
#
# for s in contest:
#     name = s.split()[0]
#     ch = s.split()[1]
#     ma = s.split()[2]
#     en = s.split()[3]
#     msg = f"""
#         姓名：{name} 语文：{ch}  数学：{ma}  英语：{en}
#     """
#     print(msg)

class Stu(object):

    def __init__(self,name,ch,ma,en):
        self.name = name
        self.ch = ch
        self.ma = ma
        self.en = en

    def __str__(self):
        msg = f"""
        姓名：{self.name}  语文：{self.ch}   数学:{self.ma}   英语:{self.en}
        {self.name} 的总成绩是：{self.score_sum()}
        {self.name} 最高分： {max(map(int,(self.ch,self.ma,self.en)))}
        {self.name} 最低分： {min(map(int,(self.ch,self.ma,self.en)))}
        """
        print(msg,end='')  # msg.split() 去除空格


    def score_sum(self):
        # return str(int(self.ch)+int(self.ma)+int(self.en)) + ' 分'
        return str(sum(map(int,(self.ch,self.ma,self.en)))) + ' 分' + '平均:'+ str(float('%0.2f'%(sum(map(int,(self.ch,self.ma,self.en)))/3)))+'分'

# 定义中转容器
content = []  # 内容
d = {}
yw = {}
sx = {}
en = {}

# 读取文件
with open('sco.txt','r',encoding='utf-8') as f:
    lines = f.readlines()
    for i in range(1,len(lines)):
        line = lines[i].split()
        s = Stu(line[0],line[1],line[2],line[3])  # 对应行
        content.append(s)
        d[int(line[1]),int(line[2]),int(line[3])] = line[0]
# 遍历文件并按照格式输出
for k in content:
    Stu.__str__(k)

# 把各科成绩和对应的学生封装到中转容器
for k,v in d.items():
    yw[k[0]] = v
    sx[k[1]] = v
    en[k[2]] = v

print('分割线'.center(60, '-'))

# 定义汇总输出，如果放到上面会多次循环
def max_min():
    d1 = {
        '语文':yw,
        '数学':sx,
        '英语':en,
    }
    for k,v in d1.items():
        msg = f"""
        {k} 最高分：{v[max(v.keys())]} 同学： {max(v.keys())}  分, 
        {k} 最低分：{v[min(v.keys())]} 同学： {min(v.keys())}  分, 
        """
        print(msg,end="")
max_min()
