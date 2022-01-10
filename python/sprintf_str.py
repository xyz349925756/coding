#！ /usr/bin/python
##################################################################
#			字符串与正则表达式				#			
##################################################################
"""
字符串的格式化
语法："%s" % str1   #使用一个值格式化字符串
"%s  %s"%(str1,str2)   #使用多个值格式化字符串
"""
str1 = "version"
num = 1.0
format = "%s" % str1
print(format,"\n")
format = "%s %d" % (str1,num)
print(format)
print("\n")
#带精度的格式化
x = 1.25
print("浮点型数字:%f"% x)
print("浮点型数字：%.1f"% x)
print("浮点型数字:%.2f"% x)
print("\n")
"""
python中格式化字符串的替代符及其含义
"""
x = 67  # ASCII码中67号
y = "god"   #字符串
z = -4
x1 = 9
x2 = 13
x3 = 100000000000000
print("ASCII码：%c"% x)
print("格式化字符串：%s"%y)
print("格式化整数:%d"%x)
print("无符号整型:%u"%z)
print("八进制:%o"%x1)
print("十六进制:%x"%x2)
print("十六进制大写:%X"% x2)
print("科学计算法格式化浮点数:%e"%x)
print("科学计算法格式化浮点数:%E"%x)
print("根据值的大小决定使用f或e:%g"%x3,x2)
print("作用同上:%G"%x3,x2)
#print("十六进制数据格式化变量的地址:%p"%x2)

#字典格式化字符串
print("%(version)s: %(num).1f"% {"version":"version","num":2})

#字符串对齐
print("\n")
word = "version3.0"
print(word.center(20))  #居中输出，变量2侧个输出5个空格
print(word.center(20,"*")) #居中输出，变量2测输出变量“*”
print(word.ljust(0))   #左对齐输出
print(word.rjust(20))   #右对齐输出
print("%30s"%word)   #跳过30个空格再输出word的值类似 word.rjust(30)



















