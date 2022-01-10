import odbc, dbi                                    # 导入ODBC模块和驱动程序
import time

db = odbc.odbc('addresses/scott/tiger')                 # 打开数据库连接
curser = db.cursor()                                    # 产生cursor游标
curser.execute("select * from address order by id desc")
for col in curser.description:                          # 显示行描述
    print (col[0], col[1])
result = curser.fetchall()
for row in result:                                      # 输出各字段的值
    print (row)
    print (row[1], row[2])
    timeTuple = time.localtime(row[3])
    print (time.strftime('%Y/%m/%d', timeTuple))
