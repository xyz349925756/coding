#！/usr/bin/python
# -*- coding:utf-8 -*-
from tkinter import *   #将Tkinter模块中的符号都导入进来，其中包括使用Tkinter接口的必需符号等
root = Tk()  #建立一个Tk根部件，初始化Tkinter
word = Label(root,text="hello,world!") #创建一个标签部件，并赋值给word变量。
word.pack() #调用word的park方法
root.mainloop()#创建一个最简单的Tkinter窗口。

