#！ /usr/bin/python
##################################################################
#				文件内容的搜索和替换			#			
##################################################################
import re
f1 = open("hello.txt","r") #以只读模式打开hello.txt文件
count = 0        #定义count=0 变量即用于计算hello的次数
for s in f1.readlines():   #每次从hello.txt读取一行到变量s
    li = re.findall("hello",s)#调用findall查询变量s,把结果存储到li中
    if len(li) > 0: #如果列表中的元素个数大于0，则表示找到hello元素
        count = count + li.count("hello") #调用列表的count（）统计当前hello出现的次数
print("查找到"+str(count)+"个hello")
f1.close()
print("\n")
#把hello替换为hi
f1 = open("hello.txt","r")
f2 = open("hello3.txt","w")
for s in f1.readlines():    #在hello.txt中读取每行内容到变量s中
    f2.write(s.replace("hello","hi"))#先使用replace（）把变量s中的 hello替换为hi，然后把结果写入到文件
    #hello3.txt中
f1.close()
f2.close()
