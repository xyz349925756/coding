#！ /usr/bin/python
##################################################################
#				python文件读取				#			
##################################################################
#按行读取方式
f = open("hello.txt")
while True:
    line = f.readline()#这里如果是f.readline（2）意思是每行每次读取2个字节
    if line:
        print(line)
    else:
        break
f.close()
print("##########")
#多行读取方式
f = open("hello.txt")
lines = f.readlines()
for line in lines:
    print(line)
f.close()
print("##########")
#一次性读取方式
f = open("hello.txt")
context = f.read()
print(context)
f.close()
print("##########")
#可以通过控制read()参数的值，返回指定字节的内容
f = open("hello.txt")
context = f.read(5)  #读取文件前5个字节内容
print(context) 
print(f.tell())    #返回文件对象当前指针位置
context = f.read(5) #继续取5个字节内容
print(context)   
print(f.tell())#输出文件当前指针位置
f.close()









