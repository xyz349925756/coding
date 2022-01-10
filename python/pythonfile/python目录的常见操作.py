#！ /usr/bin/python
##################################################################
#			目录的常见操作					#			
##################################################################
import os
os.mkdir("hello")
os.rmdir("hello")
os.makedirs("hello/world")
os.removedirs("hello/world")

print("\n")
#创建和删除

#目录的遍历
import os
def VisitDir(path):   #定义了名为VisitDir（）的函数，该函数以目录路径作为参数
    li = os.listdir(path)   #调用listdir函数返回路径存储到li中
    for p in li:
        pathname = os.path.join(path,p)#调用os.path模块的函数join（）获取文件的完整路径，并保存到pathname
        
        if not os.path.isfile(pathname):   #遍历。
            VisitDir(pathname)
        else:
            print(pathname)

if __name__ == "__main__":
    path = r"D:\python"
    VisitDir(path)   #遍历 路径下的所有目录。
print("\n")
########
#os.walk()

import os
def VisitDir(path):
    for root,dirs,files in os.walk(path):
        for filepath in files:
            print(os.path.join(root,filepath))

if __name__ == "__main__":
    path = r"d:\python"
    VisitDir(path)

















