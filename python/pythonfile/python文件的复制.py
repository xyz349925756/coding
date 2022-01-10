#！ /usr/bin/python
##################################################################
#			文件的复制					#			
##################################################################
src = open("hello.txt","w")
li = ["hello world\n","hello china\n"]
src.writelines(li)
src.close()
#创建一个hello.txt文件，并写入数据
src = open("hello.txt","r")
dst = open("hello1.txt","w")
dst.write(src.read())
src.close()
dst.close()
print("\n")
#copyfile(src,dst)
#shutil模块实现文件的复制
import shutil
shutil.copyfile("hello.txt","hello2.txt")#把hello.txt非内容复制到hello2.txt
shutil.move("hello2.txt","../")#把hello2.txt剪切到上一级目录
shutil.move("hello.txt","hello3.txt")#把hello.txt移动到当前目录，并命名为hell3.txt.hello.txt被删除

