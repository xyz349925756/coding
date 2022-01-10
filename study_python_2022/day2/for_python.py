# /usr/bin/python
# coding --utf-8--
# for i in range(10):   #ctrl+?
#     print(i)
# for a in range(5,10):
#     print(a)

#可以自定义开始

#也可以跳过取数据
# for a in range(5,10,2):
#     print(a)

# for i in range(0,100,1):
#     print(i)

# 这里1是奇数 2是偶数

for i in range(100):
    if i % 2 == 0:
        print(i,"偶数")
    else:
        print(i,"奇数")

exit("good bye!")  #退出循环