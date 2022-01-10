#!/usr/bin/python
num = input("请输入教室学生机点数：")

l = input("请输入桌子高度(单位：m)：")
de = input("请输入桌子的长度(单位：m)：")
ser = input("服务器需要几个网口：")
b = 2  #教师机网线
###################################
sh = input("请输入列数(横排一张桌子有2列即2个座位/竖排即一张桌子算一列)：")

if int(num)%2 != 0:    
    print("共",int(int(num)/2) + 1,"张桌子.行数是",int(int(num)/int(sh)) + 1 )
else:
    print("共",int(int(num)/2) ,"张桌子.行数是",int(int(num)/int(sh)) )

###################################
#单排台式机数量

c = int(num) + b + int(ser) #总数
d = int(c / 24)+1 #交换机跳线数量
su = 0   # 
st = 0   #初始化总和。
ss = 0   #
count = 0
t = input("机柜在教室中间请输入【0】，在侧面或前面请输入【1】：")
if t == "0":
    o = int(input("请输入桌子到机柜预留网线米数："))
    for n in range(0,(int(int(num)/int(sh))+1)):  
        sum = (o + float(l) + float(de) / 2 * n)
        su += sum
        print("第",n,"点的网线总长度：",int(sum)+1,"米")
    q = 4 * su 
    print("总网线长度",int(q),"米. 需要",int(q / 300) + 1 ,"箱网线")
          
elif t == "1":
    while count < int(int(int(sh) / 2)):
        p = int(input("请输入桌子到机柜预留网线米数："))
        for n in range(0,(int(int(num)/int(sh))+1)):
            sum = (p + float(l) + float(de) / 2 * n)
            st += sum
            print("第",n,"组，第",n,"点的网线总长度：",round(sum),"米")
        print("*****************************************************")
        count += 1
#        s = int(input("请输最远那组桌子到机柜预留网线米数："))
#        for n in range(1,(int(int(num)/int(sh))+1)):
#            sum = (s + float(l) + float(de) / 2 * n)
#            ss += sum
#            print("最远那组，第",n,"点的网线总长度：",round(sum),"米")
#        print("*****************************************************") 
        q =  4 * st 
        print("总网线长度",int(q),"米. 需要",int(q / 300) + 1 ,"箱网线")
################################################################################                     
else:
    print("【SORRY】输入错误，无法为您提供服务！")
    
print("教师机网线需要 【",b,"根】")
print("所需交换机数量[交换机是24口] ：【",d,"台】")
print("所需网口总计【",c + (d - 1),"个网口】，交换机跳线【",d-1,"根】")


