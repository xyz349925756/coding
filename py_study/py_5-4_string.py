#!/usr/bin/python
#-*-coding:utf-8-*-
"""
字符串内置方法
"""
from itertools import count
s = "lift is short ,i used python!"
print("s =",s)
s = s.capitalize()
print("把字符串的第一个字符大写\ns =",s)
s=s.casefold()
print("把所有字符改为小写\ns=",s)
print("将字符串居中，并使用空格填充width的新字符串\ns =",s.center(40,'*'))
print("返回“s”在字符串里边出现的次数，start,和end参数表示范围，可选\ns =",s.count("s",0,))
print("以encoding指定的编码格式对字符串经行编码\ns=",s.encode(encoding='utf_8', errors='strict'))
print("检查字符串是否以sub子字符串结束，如果是返回True，否返回Flase,start,end参数可选\n",s.endswith('!',0,))
s = "lift is short , i used python!"
print("s =",s)
print("把字符串中的tab符号转为空格，如不指定参数，默认的空格数是tabsize=8\ns =",s.expandtabs(tabsize=8))
print("检测sub是否包含在字符串中，有则返回索引值，没有就返回-1，start,end参数可选。\ns =",s.find("s",10,))
print("跟find一样，不过字符串不存在就会提示异常\ns =",s.index("s",0,20))
s = "ilikeyou12"
print("如果字符串至少有一个字符且所有字符都是字母或数字返回true,否False\ns = ",s.isalnum())
s = "ilikeyou"
print("如果字符串至少有一个字符且所有字符都是字母返回true,否False\ns = ",s.isalpha())
s = "111111111111"
print("如果字符串只包含十进制数字则返回True,否则返回False\ns = ",s.isdecimal())
print("如果字符串只包含数字则返回true、false \ns =",s.isdigit())
s = "I like You"
print("如果字符串中至少包含一个区分大小写的字符，并且这些字符都是小写，则返回true,否则返回False \ns=",s.islower())
s = "111111111111"
print("如果字符串中只包含数字字符，则返回true，false\ns =",s.isnumeric())
s = "             "
print("如果字符串中只包含空格，则返回True,否False \ns =",s.isspace())
s = "Lift Is Short,I Used Python!"
print("如果字符串是标题化（所有的单词都是以大写开始，其余都是小写）则返回True,否则false \n s=",s.istitle())
s = "I LIKE"
print("如果字符串中至少包含一个区分大小写的字符，并且这些字符都是大写，则返回true,false \ns =",s.isupper())
s = "lift is short, i used python!"
s1 = "wa"
print("以字符串作为分隔符，插入到sub中所有的字符之间\ns=",s.join(s1))
s = "I love python"
print("返回一个左对齐的字符串，并使用空格填充至长度为width的新字符串\ns=",s.ljust(30,'u'))
s = "I LIKE PYTHON"
print("转换字符串中所有大写字符为小写\ns=",s.lower())
s = "     i like you"
print("去掉字符串左边的所有空格\ns=",s.lstrip())
s = "lift is short ,i used python!"
print("找到字符串sub把字符串分成一个3元组（pre_sub,sub,fol_sub）,如果字符串中不包含sub则返回（'原字符串',','''）\ns=",s.partition("/"))
s = "   lift is short ,i used python!     "
print("把字符串中的old字符串替换成new的字符串，如果count指定，则替换不超过count次\n s=",s.replace("is", "was", 1))
print("类似find()方法，不过是从右边查找\ns=",s.rfind("i"))
print("类似index()方法，不过是从右边查找\ns=",s.rindex("i"))
print("返回一个右对齐的字符串，并使用空格填充至长度为width的新字符串\ns=",s.rjust(0))
print("类似以partition() \ns=",s.rpartition("/"))
print("删除字符串末尾的空格\ns=",s.rstrip())
print("不带参数默认是以空格符切片字符串，如果maxsplit参数有设置，则仅分割maxsplit个子字符串，返回切片后的子字符串拼接的列表\ns=",s.split(".",1))
s = "life is \nshort ,i u\nsed python "
print("按照'\\n'分割，返回一个包含各行作为元素的列表，如果keepends参数指定，则返回前keepends行\ns=",s.splitlines())
print("检查字符串是否以prefix开头，是则返回True，否则返回False,start和end参数可以指定范围检查，可选\ns=",s.startswith("l",0,))
s = "  life is short ,i used python!   "
print("删除字符串前边和后边所有的空格，chars传参数可以定制删除的字符，可选\ns=",s.strip())
s = "Life Is Short,I Used Python!"
print("翻转字符串中的大小写\ns=",s.swapcase())
print("返回标题化（所有的单词都是以大写开始，其余字母均小写字母）的字符串\ns =",s.title())
s = "  life is short ,i used python!   "
print("根据table的规则（可以由str,maketrans('a','b')定制）转换字符串中的字符\ns=",s.translate('i')) #有问题
print("转换字符串中的所有小写字符为大写\ns=",s.upper())
print("返回长度为width的字符串，原字符串右对齐，前面用0填充\ns =",s.zfill(40))

