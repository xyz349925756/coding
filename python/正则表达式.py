#！ /usr/bin/python
##################################################################
#				正则表达式				#			
##################################################################
 
import re
#^与$的使用
s = "HELLO WORLD"
print(re.findall(r"^hello",s))   #匹配以hello开始的字符串，s里面的 HELLO是大写 所以结果为[]
print(re.findall(r"^hello",s,re.I))#这行添加了匹配参数re.I意思是匹配的时候忽略大小写。
print(re.findall("WORLD$",s))#匹配以WORLD结尾的字符串。
print(re.findall(r"wORld$",s,re.I))#匹配wORld 结尾的字符串且不区分大小写。
print(re.findall(r"\b\w+\b",s))#\b匹配单词的开始和结束,\w匹配字母、数字、下划线、+ 匹配一次或多次
#这里是匹配每个英文单词

print("##############################\n")
"""sub（）替换字符串的功能"""
import re
s = "hello world"
print(re.sub("hello","hi",s))#把hello 替换为hi
print(re.sub("hello","hi",s[-4:]))#把切片后四位提取出来，并替换里面hello为hi，里面没有hello所以输出切片
print(re.sub("world","china",s[-5:]))#提取切片后5位，并替换里面world为china
print(s)#输出原字符串。
print("###############################\n")


#subn()函数的功能
import re
s = "你好 world2"
print("匹配字母数字："+re.sub(r"\w","hi",s))#\w不能匹配汉字，汉字算1个字符结果：hihi,hihihihihihi
print("替换次数:"+ str(re.subn(r"\w","hi",s)[1]))#替换的次数
print("匹配非字母数字的字符："+re.sub(r"\W","hi",s))#\W 匹配不是字母，数字，下划线的字符。
#这里不知道为什么结果是 :你好hiworld2这里不知道是不是 python 3的原因。
########后面回来再看这里############
print("替换次数:"+str(re.subn(r"\W","hi",s)[1]))
print("\n")
print("匹配空白字符："+re.sub(r"\s","*",s)) #\s匹配空白字符,把空白字符替换成*
print("替换次数："+str(re.subn(r"\s","*",s)[1]))
print("匹配非空白字符:"+re.sub(r"\S","hi",s))#\S匹配不是空白的字符，把不是空白字符替换成hi
print("替换次数:"+str(re.subn(r"\S","hi",s)[1]))
print("\n")
print("匹配数字："+re.sub(r"\d","2.0",s))#\d 匹配数字
print("替换次数："+str(re.subn("r\d","2.0",s)[1]))
print("匹配非数字:"+re.sub(r"\D","hi",s))#\D匹配非数字
print("替换次数:"+str(re.subn(r"\D","hi",s)[1]))
print("\n")
print("匹配任意字符:"+re.sub(r".","hi",s))#.匹配任意字符
print("替换次数："+str(re.subn(r".","hi",s)[1]))

print("\n")
print("匹配电话号码的正则表达式")
import re
#限定符的使用
tel1= "0871-1234567"
print(re.findall(r"\d{3}-\d{8}|\d{4}-\d{7}",tel1))
tel2 = "087-12345679"
print(re.findall(r"\d{3}-\d{8}|\d{4}-\d{7}",tel2))
###########################################
print("\n 这里是电话号码实例")
tel3 = "(0101)-1111123"
print(re.findall(r"[\(]?\d{3}[\)]?-\d{8}|[\(]?\d{4}[\)]?-\d{7}",tel3))
#print(re.findall(r"[\(]?\d{3}[\)]?\d{8}|[\(]?\d{4}[\)]?\d{7}",tel3))

tel4 = "(011)11111238"
print(re.findall(r"[\(]?\d{3}[\)]?\d{8}|[\(]?\d{4}[\)]?\d{7}",tel4))

print("############################\n")
print("使用compile提高查找效率")
import re
#compile（）预编译
s = "1abc23def45"
p = re.compile(r"\d+")
print(p.findall(s))  #代码调用p的findall方法匹配数字结果
print(p.pattern)  #输出当前使用的正则表达式

print("\n#######################################")

#正则表达式分组的解析
import re
#分组
p = re.compile(r"(abc)\1")#定义了一个分组(abc)，在后面使用\1，再次调用该分组
m = p.match("abcabcabc")#p.match()对字符串abcabcabc进行搜索，返回一个match对象m
print(m.group(0))#调用match对象的group(0)方法，匹配0号组，结果abcabc
print(m.group(1))#调用match对象的group(1)方法，匹配1号组，结果abc
print(m.group())#默认情况下返回group(0)方法,匹配group(0)，即0号组结果:abcabc

p = re.compile(r"(?P<one>abc)(?P=one)")
#给分组命名，?P<one>abc 中的one 表示分组的名称，（?P=one）调用分组one 相当与\1
m = p.search("abcabcabc")

print(m.group("one")) #调用group(one)分组的结果 abc
print(m.groupdict().keys())#获取正则表达式中分组的名称【one】
print(m.groupdict().values())#获取正则表达式中分组的内容[abc]
print(m.re.pattern)#获取当前正则表达式。

































