#！/usr/bin/python
# -*- coding:utf-8 -*-
#try...finally
try:
    f = open("hello.txt","r")
    try:
        print(f.read(5))
    except:
        print("读取文件错误")
    finally:
        print("释放资源")
        f.close()
except FileNotFoundError:
    print("文件不存在")