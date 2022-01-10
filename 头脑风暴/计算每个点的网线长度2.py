#!/usr/bin/python
quantity = input("请输入学生机数量(位)：")
num = int(quantity)
###################桌子规格####################
desk_long = input("请输入桌子的长(M)：")
desk_width = input("请输入桌子的宽(M)：")
desk_high = input("请输入桌子的高(M)：")
####################房间规格###################
room_long = input("请输入教室的长(M)：")
room_width = input("请输入教室的宽(M)：")
#####################判断教室的类型############
ter = input("请输入教师机台数：")
###############################################
input_y = input("是否需要打印教室选型表Y 打印 ,N 不打印：")
if input_y == "Y" or input_y == "y":
    print("*********************教室选型表******************")
    print("------------------------------------------------|")
    print("|      I 型      |      II型      |     III型   |")
    print("|-----------------------------------------------|")
    print("|     =====      |      =====     |  0      0   |")
    print("|  ==   ==   ==  |   ||  ||  ||   |0 0 0  0 0 0 |")
    print("|  ==   ==   ==  |   ||  ||  ||   |  0      0   |")
    print("|  ==   ==   ==  |   ||  ||  ||   |  0      0   |")
    print("|  ==   ==   ==  |   ||  ||  ||   |0 0 0  0 0 0 |")
    print("|  ==   ==   ==  |   ||  ||  ||   |  0      0   |")
    print("-------------------------------------------------")
else:
    print("您选择的【不打印】")
##################推荐教室选型####################
if room_long != room_width:
    if room_long < 2 * room_width:
        print("此教室长：",room_long,"M，宽：",room_width,"M，推荐【I型】")
        ser = input("请输入服务器需要几个网口：")        
####################计算过道及宽度##################
        aisles = input("请输入过道条数：")      
        aisle_width = input("请输入过道的宽(单位：M)：")       
        if int(aisles) <= 6:
            n = int((float(room_width) - float(aisles) * float(aisle_width)) / float(desk_long))
            print("每行可以摆放",n,"张桌子")
        else:
            print("过道超出实际情况！")
###################计算所需桌子#########################            
        if int(quantity) % 2 != 0:
            a = int(((int(quantity)/2)+1)/(int((float(room_width) - float(aisles) * float(aisle_width)) / float(desk_long))))
            d = int(int(quantity)/2)+1
            print("共",d,"张桌子.列数是：",a)
            if d != n * a:
                print("剩下的",d - n * a,"桌子根据顺序摆放！")
        else:
            b = int(int(quantity)/2/(int((float(room_width) - float(aisles) * float(aisle_width)) / float(desk_long))))
            e = int(int(quantity)/2)
            print("共",e,"张桌子.列数是：",b)
            if e != n * b:
                print("剩下的",e - n * b,"桌子根据顺序摆放！")
        #
#############################################################
                        
############################################################
    else:
        print("此教室长：",room_long,"M，宽：",room_width,"M，推荐【II型】")

##########################################################    
else:
    print("此教室长：",room_long,"M，宽：",room_width,"M，首选【III型】，其次【I型】、【II型】")
    
###########################################################
###计算网线总长度和需要多少根网线.






print("需要",int(ter) + 1,"根教师机网线")

