#！ /usr/bin/python

###################################################################
#								 	  #
#									  #
#			setdefault()的使用					  #
#									  #
#									  #
###################################################################

dict = {}
dict.setdefault("a")
print(dict)
dict["a"] = "apple"
dict.setdefault("a","None")
print(dict)
#字典的setdefault()可以创建和添加新的元素并设置默认值。
