#!/usr/bin/python3
# -*-coding:utf-8-*-
# Auth: xyz34
# File: 模块.py
# TIME: 5月  星期六

# import pack.m1
# import pack.m2
#
# pack.m1.f1()
# pack.m2.f2()

# from pack import m1
# from pack import m2
#
# m1.f1()
# m2.f2()

# from pack import m1
# from pack import m2
#
# m1.f1()
# m2.f2()

# import pack

# import time
# print(time.time())  #从1970年1月1日到现在的时间戳
# print(time.strftime('%Y-%m-%d %H:%M:%S'))   # 按照指定格式显示时间
# print(time.strftime('%Y/%m/%d %T'))  # 同上面
# print(time.strftime('%Y/%m/%d %X')) # 同上
# time.sleep(1) # 休眠1秒
# # 结构化时间
# print(time.localtime())
# print(time.localtime().tm_yday)

# import datetime
# print(datetime.datetime.now())  # 获取当前时间
# print(datetime.datetime.now()+datetime.timedelta(days=4))   # 4天后
# print(datetime.datetime.now()+datetime.timedelta(weeks=2))  #2周后
#
# import time
# s_time = time.localtime()
# print(time.mktime(s_time))   # 结构化时间转化为时间戳
#
# tp_time = time.time()
# print(time.localtime(tp_time))   # 时间戳转化为结构化时间
#
# print(time.localtime())   # 当前时区的标准时间
# print(time.gmtime())   #世界标准时间
#
#
# print(time.strftime('%Y-%m-%d %H:%M:%S',s_time))  # 把结构化时间转成格式化
# print(time.strptime('1987-08-06 09:50:20','%Y-%m-%d %H:%M:%S'))   # 把格式化时间转结构化

# 指定日期 加7天

# import time
# s_time = time.strptime('1980-08-06 09:50:20',"%Y-%m-%d %H:%M:%S")
# print('格式时间转为结构化时间',s_time)
# t_time = time.mktime(s_time) + 7*86400
# print('结构化时间转为时间戳',t_time)
# r_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(t_time))
# print('时间戳转为格式化时间',r_time)
#
# print(time.asctime())


# import datetime
# print(datetime.datetime.fromtimestamp(564568745))

# import random
# print(random.randint(0,1))  # 0,1 随机
# print(random.random())  # 0-1之间的小数
# print(random.randrange(1,100,5))  # 0-100之间相隔5个数的数
# print(random.choices([1,2,3,4,5])) # 随机从列表选出一个数
# print(random.sample([1,2,3,4,5],2)) # 随机从列表选出n个数
# print(random.uniform(1,5))  # 指定范围里面的浮点数
#
# l = [1,4,6,8,0,2,3]
# random.shuffle(l)    # 随机洗牌打乱顺序
# print(l)

# 验证码
# import random
# def s(size):
#     res = ''
#     for i in range(size):
#         s1 = chr(random.randint(65,90))
#         s2 = chr(random.randint(97,122))
#         n1 = str(random.randint(0,9))
#         res += random.choice([s1,s2,n1])
#     return res
#
# print(s(6))


# import os,sys
# print(os.environ)
# print(sys.path)  # 显示python环境路径
# print(os.path.abspath(__file__))  # 打印当前文件的绝对路径
# print(__file__) # 同上

# import sys
# print(sys.argv) # 外部传参
# print(sys.modules.keys()) # 返回已经导入的模块
# print(sys.stdin) # 标准输入
# print(sys.stdout)  # 标准输出
# print(sys.stderr)  # 错误输出
# print(sys.argv[0])  # 文件本身
# print(sys.argv[1])   # 第一个参数
# sys.exit(0)  # 捕获退出是0 正常其他异常

# 进度条
# import time
# a = 0
# b = 100
# while a <= b:
#     # print(''.center(a,"-"),end="")
#     # print('\r %-50s'%(a*"-"),end=" ")
#
#     print('\r',end="")
#     # print("进度： {}% :".format(a),"💎"*(a//2),end="")   #→◐★■▉┇▶✈>➤
#     print("进度 {}%：".format(a),"".center(a//2,"💎"),end="")
#     time.sleep(0.1)
#     a += 1

