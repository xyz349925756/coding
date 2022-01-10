#！/usr/bin/python
# -*- coding:utf-8 -*-
from tkinter import *
root = Tk()
root.title("顶层窗口")

l=[("red",1,NORMAL),("green",2,NORMAL),("black",3,DISABLED),("blue",4,NORMAL),("yellow",5,NORMAL)]
for text,value,status in l:
    foo = IntVar()
    c = Checkbutton(root,text=text,variable=foo,state=status)
    c.pack(anchor=W)


root.mainloop()
#复选按钮，不能选择选项