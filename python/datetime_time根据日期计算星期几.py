#！ /usr/bin/python
##################################################################
#		根据时间计算是星期几					#			
##################################################################
import time
import datetime
today = int(time.strftime("%w"))
print("星期",today)
anyday = datetime.datetime(2015,10,14)
print("起始时间:",anyday)
