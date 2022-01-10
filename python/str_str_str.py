#！ /usr/bin/python
##################################################################
#			字符串的合并					#			
##################################################################
str1 = "hello,"
str2 = "world!"
str3 = "this\f"
str4 = "is\t"
str5 = "python\n"
result = str1+ str2 + str3 + str4
result += str5
print(result)

strs = ["hello ","world ","this ","is ","python "]
result = "".join(strs)
print(result)

from functools import reduce
import operator
strs = ["hello ","world ","this ","is ","python! "]
result = reduce(operator.add,strs,"")
print(result)
