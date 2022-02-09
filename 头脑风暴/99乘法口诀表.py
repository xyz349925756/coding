# coding --utf-8--
# /usr/bin/python

for a in range(1, 10):
    for b in range(1, a + 1):
        print("%d X %d = %2d" % (a, b, a * b), end="  ")
    print("")

print("-------法1---------")

for a in range(1, 10):
    for b in range(1, 10):
        print("%d X %d = %2d" % (a, b, a * b), end="  ")
    print("")

print("-------法2---------")

for i in range(1, 10):
    for k in range(1, i):
        print(end="            ")
    for j in range(i, 10):
        print("%d X %d = %2d " % (i, j, i * j), end=" ")
    print("")
