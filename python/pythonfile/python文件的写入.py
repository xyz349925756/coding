#！ /usr/bin/python
##################################################################
#			文件的写入					#			
##################################################################
#覆盖式写入，不安全。
f = open("hello.txt","w+")
li = ["hello world\n","hello china\n"]
f.writelines(li)
f.close()

#追加内容a+
f = open("hello.txt","a+")
new_context = "goodluck"
f.write(new_context)
f.close()


