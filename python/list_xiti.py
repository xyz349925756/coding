#！ /usr/bin/python

###################################################################
#								 	  #
#									  #
#			习题4						  #
#									  #
#									  #
###################################################################

L = [2,5,3,8,10,1]
print(L)
L.sort()
print("正序",L)
L.reverse()
print("反序",L)


print("################")

s = "123456"
print(s)
l = list(s)
print("把字符串转成列表",l[:6])
l.reverse()
print(l[:6])

print("#######################")
d = {"a":"1","b":"2","c":"3"}
for k in d:
    print("d[%s] ="%k ,d[k])
d["d"]="4"
print(d)

print("#######")

#100以内的素数







