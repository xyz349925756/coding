#！/usr/bin/python
# -*- coding:utf-8 -*-
from tkinter import *
root = Tk()
root.title("顶层窗口")
foo = IntVar()
for text,value in [("red",1),("green",2),("black",3),("blue",4),("yellow",5)]:
    r = Radiobutton(root,text=text,value=value,variable=foo)
    r.pack(anchor=W)
foo.set(2)

root.mainloop()

#单选按钮
