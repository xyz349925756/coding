#！ /usr/bin/python
##################################################################
#				字符串的比较				#			
##################################################################
"""
python直接使用“==”“！=”来比较字符的内容
"""
str1 = 1
str2 = "1"
if str1 == str2:
    print("相同")
else:
    print("不相同")
if str(str1) == str2:
    print("相同")
else:
    print("不相同")

"""
startswith(substring,[,start[,end]]) 
"""
word = "hello,world"
print("hello"==word[0:5])
print(word.startswith("hello"))
print(word.endswith("ld",6))
print(word.endswith("ld",6,10))
print(word.endswith("ld",6,len(word)))
"""
startswith 是从左到右比较【0：5】就是从第一位到第五位包含第一位的字符串是hello
startswith（”ld“,6）是比较字符串第一个单词是hello，true
endswith（”ld“，6）从字符串变量word的结尾   到   word[6]之间搜索子串ld（逆向搜索）
endswith（”ld“,6,10）从字符串变量word的【6，10】分片中搜索id，因为最后一位10是不包含的
关系
6,len(word)是从分片6，到最后，所以是包含。
"""
