#！ /usr/bin/python

###################################################################
#								 	  #
#									  #
#			导入模块的过滤					  #
#									  #
#									  #
###################################################################
import sys
d = sys.modules.copy()
import copy,string
zip(set(sys.modules) - set(d))
print(d)
