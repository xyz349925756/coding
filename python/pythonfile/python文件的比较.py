#！ /usr/bin/python
##################################################################
#			文件的比较					#			
##################################################################
import difflib
f1 = open("hello.txt","r")
f2 = open("hello3.txt","r")
src = f1.read()
dst = f2.read()
print(src)
print(dst)
s = difflib.SequenceMatcher(lambda x: x == "",src,dst)
for tag,i1,i2,j1,j2 in s.get_opcodes():
    print("%s src[%d:%d]=%s dst[%d:%d]=%s"%(tag,i1,i2,src[i1:i2],j1,j2,dst[j1:j2]))
