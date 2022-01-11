# /usr/bin/python
# coding --utf-8--
import random
ages = random.randint(0,100)
print(ages)
count = 0
while count < 6:
    count += 1
    age = int(input("please your age:"))
    num = 6 - count
    if age < ages:
        print("小了")
        print(f"你还有{num}次机会")
    elif age > ages:
        print("大了")
        print(f"你还有{num}次机会")
    elif age == ages:
        print("猜对了")
        break

print("后续")  #为了证明使用print   如果最后的可以使用exit