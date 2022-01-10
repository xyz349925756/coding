#！/usr/bin/python
# -*- coding:utf-8 -*-
import odbc,dbi
import time
db = odbc.odbc("addresses/scott/tiger")
curser = db.cursor()
curser.execute("select * from address order by id desc")
for col in curser.description:
    print(col[0],col[1])
result = curser.fetchall()
for row in result:
    print(row)
    print(row[1],row[2])
    timeTuple = time.localtime(row[3])
    print(time.strftime('%Y/%m/%d',timeTuple))
