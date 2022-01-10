#！ /usr/bin/python
##################################################################
#			字符串与日期的转换				#			
##################################################################
"""时间到字符串，字符串到时间的转换"""
import time,datetime
#引用time,datetime
s=time.strftime("%Y-%m-%d %X",time.localtime())
print(time.strftime("%Y-%m-%d %X",time.localtime()))
#时间到字符串的转换
print(type(s))
#字符串到时间的转换
t=time.strptime("2015-10-27","%Y-%m-%d")
y,m,d=t[0:3]
print(datetime.datetime(y,m,d))
q=datetime.datetime(y,m,d)
print(type(q))
