#！ /usr/bin/python

###################################################################
#								 	  #
#									  #
#			字典						  #
#									  #
#									  #
###################################################################

dict = {"a":"apple","b":"banana","g":"grape","o":"orange"}
print("字典dict :",dict)
dict["w"] = "watermlon"
print("添加键W对应键值：watermlon :",dict)
del(dict["a"])
print("删除字典键对应a的元素：",dict)
dict["g"] = "grapefruit"
print("修改键g对应的元素：",dict)
dict.pop("b")
print("弹出元素“b”:",dict)
dict.clear()
print("清除字典中所有的元素:",dict)

print("**************************************************************************")

dict = {"a":"apple","b":"banana","g":"grape","o":"orange"}
for k in dict:
    print("dict[%s] =" % k,dict[k])
#字典k变量获取的是字典key值，并没有获取到value值，因此通过dict[k]来获取value值.

print("**************************************************************************")


#还可以用items()来遍历
dict = {"a":"apple","b":"banana","g":"grape","o":"orange"}
print(dict.items())  #items()返回一个由若干元素组成的列表
for (k , v) in dict.items():  #用items来遍历字典
    print("dict[%s] = "% k ,v)

print("**************************************************************************")
#混合型字典
dict = {"a":("apple",),"bo":{"b":"banana","o":"orange"},"g":["grape","grapefruit"]}
print(dict)
print("输出嵌套的元组：",dict["a"])
print("使用双下标访问元组的第一个元素：",dict["a"][0])
print("返回嵌套的字典",dict["bo"])
print("使用双下标访问嵌套字典中key=o 对应的value值：",dict["bo"]["o"])
print("返回嵌套的列表：",dict["g"])
print("返回嵌套列表中的第二个元素：",dict["g"][1])
