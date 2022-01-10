#！/usr/bin/python
# -*- coding:utf-8 -*-
import win32com.client

engine = win32com.client.Dispathch("DAO.DBEngine.36")
db = engine.OpenDatebase("addresses.accdb")
rs = db.OpenRecordset("address")
rs = db.OpenRecordset("select * from address ")
db.Execute("""insert into address (name,address,createtime)
VALUES ("赵涛","上海","2008-3-25")
""")
while not rs.EOP:
    print((rs.Fields("address").Value).encode("gb2312"))
    rs.Movenext()