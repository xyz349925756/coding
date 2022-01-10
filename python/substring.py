#！ /usr/bin/python
##################################################################
#			     字符串的截取					#			
##################################################################
"""
split()
"""
word = "world"
print(word[4])
"""通过切片截取
string[start:end:step]开始，结束，步长
"""
str1 = "hello,world"
print(str1[0:3])
print(str1[::2])
print(str1[1::2])

"""
如果要同时截取多个子串。sp;it([char][,num])  char表示用于分隔的字符，默认分隔字符是空格。
参数num表示分隔的次数。如果num等于2，将把源字符串分割为3个子串，默认情况下将根据字符串
char在字符串中出现的个数来分隔子串
"""
sentence = "Bob said: 1, 2, 3, 4"
print("使用空格取子串：",sentence.split())
print("使用逗号取子串：",sentence.split(","))
print("使用两个逗号取子串：",sentence.split(",",2))

str1 = "a"
print(id(str1))
print(id(str1+"b"))
