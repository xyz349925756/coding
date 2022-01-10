#!/usr/bin/python
"""
num1 = input("请输入第一个数字：")
num2 = input("请输入第二个数字：")
sum = int(num1) + int(num2)
print("sum =",sum)
"""


import random
num = random.randint(1,9)
i = int(input('请输入你猜想的数字:'))
count = 0
t = 3
while i != num and count < t :
    i = int(input('您猜错了，请重新输入：'))
    count += 1
    view = count
    print('你已经输入了',view,'次,你还有',(t - view),'次')
    if i == num :
        print('猜测正确，您很厉害！')
        print('游戏结束！您不去买彩票实在是可惜了！')
    else:
        if i < num :
            print('你猜测的数字小了！')
        else:
            print('你猜测的数字大了！')
print('GAME OVER!',num)
