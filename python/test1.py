#/usr/bin/python
#输入姓和名字输出欢迎语
""" 
firename = input("请输入你的姓氏，按回车继续：")
lastname = input("请输入你的名字，按回车继续：")
print("你好，"+ firename + lastname +"欢迎光临本站")
"""
#输入一个数字，如果在1，100之间那么输出：你很聪明，其他输出：加油
""" 
num = int(input("请输入一个数字："))
print("你很聪明") if (1 <= num < 100) else print("加油")
"""
#计算一年中有多少秒
"""
def year():
    y = 365
    d = 24
    h = 60
    m = 60
    s = y * d * h * m
    print("一年总共有:",s,"秒")

year()
"""
#输入一个数字跟已有范围内的数字对比，有3次机会。
import random
num = random.randint(1,9)
i = int(input("请输入您猜测的数字："))
view = 3
count = 0
while count < 3:
    count += 1
    
    print(count)

    
