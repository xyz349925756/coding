#！ /usr/bin/python
##################################################################
#			字符串的转义符					#			
##################################################################
path = "hello\tworld\n"
print(path)
print(len(path))
path= r"hello\tworld\n"
print(path)
print(len(path))
print("\n")

path = "hello\000world\\"
print(path)


print("\n")


#strip()去掉转义字符
word = "hello\tworld\n"
print("直接输出：",word)
print("strip()后输出：",word.strip())
print("lstrip()后输出：",word.lstrip())
print("rstrip()后输出：",word.rstrip())
