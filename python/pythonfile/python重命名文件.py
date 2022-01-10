#！ /usr/bin/python
##################################################################
#			文件的重命名					#			
##################################################################
import os
li =  os.listdir(".")  #调用listdir（）返回当前目录的文件列表，其中"."表示当前目录
print(li)
if "hello.txt" in li:  #判断当前目录是否存在hello.txt文件
    os.rename("hello.txt","hi.txt")
elif "hi.txt" in li:
    os.rename("hi.txt","hello.txt")
print("\n")

    
