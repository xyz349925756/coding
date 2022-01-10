#!/usr/bin/python
#-*-coding:utf-8-*-

empty = []
for i in range(1,100):
    empty.append(i)   
print("empty =",empty)
print(empty[::2])
print(empty[::-1])

empty2 = []
for j in range(10,20):
    empty2.append(j)    
print("empty2 =",empty2)

empty.extend(empty2)
print("empty =",empty)

d = ['a','b','c','d','e','f']
c = 0
for b in d:
#    print(b,end="")
    empty.insert(c,b)
    c += 1
    print("empty =",empty)

for i in range(0,5):
    print(d[i],end=" ")
    
d[0] , d[1] = d[4] , d[3]
print(d)

    