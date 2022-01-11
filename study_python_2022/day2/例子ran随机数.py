# /usr/bin/python
# coding --utf-8--
# >>> "-".join(["a","b","c"])
# 'a-b-c'

# >>> import random
# >>> random.choice("abcdefghijlk")
# 'b'
# >>> random.choice("abcdefghijlk")
# 'c'
# >>> s = "abcdefghijk"
# >>> random.sample(s,3)
# ['j', 'c', 'a']
# >>> random.sample(s,5)
# ['k', 'b', 'g', 'a', 'c']
import  random
n = random.randint(1,100)
print(n)