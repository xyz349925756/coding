#！/usr/bin/python
#############################################################
#                                                           #
#                字符串的换行                                 #
#                                                           #
#############################################################
#写法一
sql = "select id,name \
from dept \
where name = 'A'"
print(sql)

#写法二
sql = "select id,name " \
      "from dept " \
      "where name = 'A'"
print(sql)
