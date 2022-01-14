# /usr/bin/python
# coding --utf-8--
import string
s = "hello, world!"
s1 = "这个一个字符串测试"
s2 = "Hellow,World!"
s3 = "HELOW"
print(s[2:5],s[6:],s[:-7],s[-7:-1]) #包含头，不含尾
print(s.center(60,"-"))  #在字符串两边按照指定符号补全
print(s.count('l'),s.count('l',0,7)) #指定字符在字符串中出现几次，或者指定范围内出现几次
print(s2.casefold(),s3.casefold())   #小写显示所有字符
print(s.capitalize())  #字符串第一个字母大写
print(s1.encode('GBK')) #字符编码输出
print(s.endswith('l'),s.endswith("!"),s.endswith('o',0,5)) #检查指定范围是否以某个字符结束
print(s.startswith('h'),s.startswith("w",-6,-1)) #查看指定字符串是否是指定字符开头

s4 = "\ttable   test"
print(s4.expandtabs(tabsize=4))  #把字符串中的\t 符号转为设置的空格，默认是8个空格
print(s.find('o'),s.find('o',0,5),s.find('f',0,len(s))) #查找字符在字符串中的位置，指定起点或终点,-1为找不到
s5 = "我是{}，今年{}岁"
print(s5.format("主席",60))  #更多用法 https://blog.csdn.net/jpch89/article/details/84099277
s6 = "学生姓名{name},年龄{age}"
dic = {'name':'zhangsan','age':32,}
print(s6.format_map(dic))
print(s6.format(**dic))

s7 = '123456'
s8 = 'hell5'
print(s.index('o'),s.index('w',0,len(s))) #不存在的index报错
print(s.isalnum(),s7.isalnum(),s8.isalnum()) #判断字符串中是否含有数字，带一个数字字符都是true
print(s.isalpha(),s3.isalpha(),s7.isalpha(),s8.isalpha())  #字符串中全是字母则为真
print(s4.isascii())  #字符串中的字符是否是ascii
print(s7.isdigit(),s.isdigit())  #判断是否是数字
print(s7.isdecimal(),s8.isdecimal(),s.isdecimal())  #判断字符串中是不是包含十进制数
s9 = "or"
print(s9.isidentifier())    #检查python标识符
print(s.islower(),s2.islower())  #判断是否全部是小写
print(s.isnumeric(),s7.isnumeric()) #字符串全为数字true，false
print(s.isprintable(),s4.isprintable(),s7.isprintable())  #检查是否能打印
s10 = "   "
print(s10.isspace())  #字符串是否只包含空格
print(s.title()) #标题，首单词字母大写
s11 = s.title()
print(s11.istitle())  #如果字符串是标题化的则返回 true
print(s.isupper(),s3.isupper())  #检查字符串是否是大写
print(s.join(s7))  #以s字符串为分隔，将s7中所有的元素合并为一个新的字符串
print('---'.join('12345'))
s12 = "hello,world!"
s13 = "hi                      hello,world!"
print(s12.ljust(20),s13.ljust(60))  #返回原字符串左对齐，如果不满足使用空格填充
print(s3.lower())  #大写改小写
s14 = "   hello   "
print(s14.lstrip(),s12.lstrip())  #去掉左边的空格
s15 = "a123456"
s16 = "a234567"
print(s15.maketrans(s16,s15))  #字符转换表，字符串必须一样长 acssi编码 第一个参数是需要转换的字符，第二个是字符串转换的目标
print(max(s15),min(s15))   #字符串中最大的，最小的
print(s.partition(','))   #以指定字符为分隔符，
print(s.partition("s"))   #如果指定的字符不在，那么默认字符串是第一个，第二个是空，第三个也是空
print(s.rfind('l')) #查找指定字符最后一次出现的位置，没有匹配返回-1
print(s15.rjust(30),s14.ljust(30))  #右对齐，左对齐，不够空格补充
print(s.rindex('l'))  #返回最后一个索引位置
print(s.rsplit(","),s.rsplit('l'))  #以指定字符分隔,有多少纠纷各多少
print(s.replace('l','w',3))  #替换指定被替换字符，为替换字符，次数为n次
print(s.removeprefix('h')) #移除字符串首字母
print(s.removesuffix('!'))  #移除字符串字尾
print(s14.rstrip(),s.rstrip())  #移除字符串末尾空格
print(s.rpartition(',')) #指定分隔字符
print(s14.strip(),s15)  #移除字符串末尾空格
print(s.split(','))  #以指定字符分隔，num有指定最多分隔n+1次
print(s.splitlines()) #按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。
print(s.swapcase(),s2.swapcase()) #大小写互换
print(s15.translate(s.maketrans(s15,s16)),'34')  #不清楚用法
print(s.zfill(30)) #返回字符串为指定长度，0补全










