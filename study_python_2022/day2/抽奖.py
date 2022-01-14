# /usr/bin/python
# coding --utf-8--
"""
张三科技有限公司有300员⼯，开年会抽奖，奖项如下：
⼀等奖 3名， 泰国5⽇游
⼆等奖6名，Iphone⼿机一部
三等奖30名，python书籍一本
规则：
1. 共抽3次，第⼀次抽3等奖，第2次抽2等奖，第3次压轴抽1等奖
2. 每个员⼯限中奖⼀次，不能重复
"""
import random
import string

worker_list = []
for i in range(1, 301):
    worker_list.append(i)  # 生成员工信息

iteam = []
for i in range(1, 31):
    iteam.append(i)

s = ""
s1 = s.center(60,"-")
count = 3
while count > 0:
    count -= 1
    co = int(input("现在开始抽几等奖，输入顺序：3，2，1："))
    if co == 3:
        tp = random.sample(worker_list, 30)
        third_prizes = f'''
                               三等奖  获奖名单
        {s1}
        {iteam[0]}  : {tp[0]}     {iteam[1]}  : {tp[1]}    {iteam[2]} : {tp[2]}    {iteam[3]} : {tp[3]}    {iteam[4]} : {tp[4]}    
        {s1}
        {iteam[5]}  : {tp[5]}     {iteam[6]}  : {tp[6]}    {iteam[7]} : {tp[7]}    {iteam[8]} : {tp[8]}    {iteam[9]} : {tp[9]}    
        {s1}
        {iteam[10]} : {tp[10]}    {iteam[11]} : {tp[11]}     {iteam[12]} : {tp[12]}    {iteam[13]} : {tp[13]}    {iteam[14]} : {tp[14]}    
        {s1}
        {iteam[15]} : {tp[15]}    {iteam[16]} : {tp[16]}    {iteam[17]} : {tp[17]}    {iteam[18]} : {tp[18]}    {iteam[19]} : {tp[19]}     
        {s1}
        {iteam[20]} : {tp[20]}    {iteam[21]} : {tp[21]}    {iteam[22]} : {tp[22]}    {iteam[23]} : {tp[23]}    {iteam[24]} : {tp[24]}    
        {s1}
        {iteam[25]} : {tp[25]}    {iteam[26]} : {tp[26]}    {iteam[27]} : {tp[27]}    {iteam[28]} : {tp[28]}    {iteam[29]} : {tp[29]}
        {s1}
        
        奖品：python书籍一本
        '''
        for a in tp:
            worker_list.remove(a)
        print(third_prizes)
    elif co == 2:
        second_prize = random.sample(worker_list, 6)
        sp = f'''
                                二等奖  获奖名单
        {s1}
         {iteam[0]} : {second_prize[0]}        {iteam[1]} : {second_prize[1]}          {iteam[2]} : {second_prize[2]}  
        {s1}
         {iteam[3]} : {second_prize[3]}        {iteam[4]} : {second_prize[4]}          {iteam[5]} : {second_prize[5]}  
        {s1}
        
        奖品：Iphone⼿机一部
        '''
        for b in second_prize:
            worker_list.remove(b)
        print(sp)
    elif co == 1:
        first_prize = random.sample(worker_list, 3)
        fp = f'''
                            一等奖  获奖名单
        {s1}
         {iteam[0]} : {first_prize[0]}          {iteam[1]} : {first_prize[1]}          {iteam[2]} : {first_prize[2]}
        {s1}
        
        奖品： 泰国5⽇游
        '''
        for c in first_prize:
            worker_list.remove(c)
        print(fp)
    else:
        exit("输入错误，程序退出!")