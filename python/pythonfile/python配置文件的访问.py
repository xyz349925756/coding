#！ /usr/bin/python
##################################################################
#			配置文件的访问					#			
##################################################################
import configparser
config = configparser.ConfigParser()
config.read("ODBC.ini")
sections = config.sections()
print("配置块:",sections)
o = config.options("ODBC 32 bit Data Sources")
print("配置项：",o)
v = config.items("ODBC 32 bit Data Sources")
print("内容:",v)
#根据配置块，配置项，返回内容
access = config.get("ODBC 32 bit Data Sources","MS Access Database")
print(access)
excel = config.get("ODBC 32 bit Data Sourcse","Excel Files")
print(excel)
dBASE = config.get("ODBC 32 bit Data Sourcse","dBASE Files")
print(dBASE)


#由于WINDOWS10上面 没有这个系统文件所以。失败
