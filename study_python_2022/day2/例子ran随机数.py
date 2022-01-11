# /usr/bin/python
# coding --utf-8--
# >>> "-".join(["a","b","c"])
# 'a-b-c'

import  random
n = random.randint(1,100)
print(n)

s = "abcdefghijklmnopqrstuvwxyz"
s1 = random.choice(s)
print(s1)

s2 = random.sample(s,5)
print(s2)
print("".join(s2))   #拼接字符串
print("-".join(s2))

import string
s3 = string.ascii_letters   #所有大小写字母
print(s3)
print(len(s3))

s4 = string.ascii_uppercase #大写字母
print(s4)
print(len(s4))

s5 = string.ascii_lowercase #小写
print(s5)
print(len(s5))

s6 = string.punctuation  #特殊字符
print(s6)
print(len(s6))

s7 = string.digits  #打印数字
print(s7)
print(len(s7))