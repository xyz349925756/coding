# 文件的查找
import re

f1 = file("hello.txt", "r")
count = 0
for s in f1.readlines():    
    li = re.findall("hello", s)
    if len(li) > 0:
        count = count + li.count("hello")
print ("查找到" + str(count) + "个hello")
f1.close()
