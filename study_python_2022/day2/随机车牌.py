# /usr/bin/python
# coding --utf-8--

import random
import string
c_nums = string.ascii_uppercase + string.digits #提取后5位
second_letter = random.choice(string.ascii_uppercase) #前两位

count = 3
while count > 0:
    cars = []
    nums = []
    for i in range(20):
        c_num = f"云{second_letter}-{''.join(random.sample(c_nums, 5))}"
        #c_num = f"云D-{''.join(random.sample(c_nums, 5))}"   #这里一般会选择归属地，或者按归属地选择前面两位
        cars.append(c_num)
        nums.append(i+1)
    car_nums = f'''
    -------------------------------------------------------------------------------------------------
               {nums[0]}  :{cars[0]}        {nums[1]}  :{cars[1]}       {nums[2]}   :{cars[2]}        {nums[3]}  :{cars[3]}
    -------------------------------------------------------------------------------------------------
               {nums[4]}  :{cars[4]}        {nums[5]}  :{cars[5]}       {nums[6]}   :{cars[6]}        {nums[7]}  :{cars[7]}
    -------------------------------------------------------------------------------------------------
               {nums[8]}  :{cars[8]}        {nums[9]} :{cars[9]}       {nums[10]}  :{cars[10]}       {nums[11]}  :{cars[11]}
    -------------------------------------------------------------------------------------------------
               {nums[12]} :{cars[12]}        {nums[13]} :{cars[13]}       {nums[14]}  :{cars[14]}       {nums[15]}  :{cars[15]}
    -------------------------------------------------------------------------------------------------
               {nums[16]} :{cars[16]}        {nums[17]} :{cars[17]}       {nums[18]}  :{cars[18]}       {nums[19]}  :{cars[19]}
    -------------------------------------------------------------------------------------------------
    '''
    print(car_nums)
    count -= 1
    #choice = input("请输入你选的车牌号码：").strip()
    choice = int(input("请输入你中意的车牌号码对应的序号："))
    if choice in nums:
        nu = choice - 1
        #print(f"{nums[nu]}:{cars[nu]}")
        exit(f"恭喜你选中{nums[nu]}号，车牌为： {cars[nu]}  ，祝你一路平安！")
    else:
        print(f"未选择,或者输入超出范围，您还有{count}次机会！")






