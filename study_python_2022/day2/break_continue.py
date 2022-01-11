# /usr/bin/python
# coding --utf-8--

for i in range(1,6):
    if i == 3 :
        continue  #直接跳过打印3层
    print(f"-----{i} 层----")

    for j in range(1,9):
        if i == 4 and j == 4:
            print("OVER!!!")
            break      #这个循环是跳过当前整个循环
        print(f"L{i}-{i}0{j} 室",end="  ")
    print()