# /usr/bin/python
# coding --utf-8--

for i in range(1,10):
    for j in range(1,i+1):
        print(f"{i} X {j} = {i*j}",end="  ")
    print()