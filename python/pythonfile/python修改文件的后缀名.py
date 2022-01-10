#！ /usr/bin/python
##################################################################
#				修改文件后缀名				#			
##################################################################

import os
files = os.listdir(".")
print(files)
for filename in files:
    pos = filename.find(".")
    if filename [pos + 1:] == "html":
        newname = filename[:pos + 1] + "htm"
        os.rename(filename,newname)

"""
为获取文件的后缀名，先查找”.“所在的位置，然后通过分片filename[pos + 1:]获取后缀名。

"""
#上面的也可以用splitext()
import os
files = os.listdir(".")
for filename in files:
    li = os.path.splitext(filename)#这里调用splitext（）对文件名进行解析，返回文件名和后缀名的列表。
    if li[1] == ".htm":
        newname = li[0] + ".html"
        os.rename(filename,newname)

#glob也可以实现上面的功能
