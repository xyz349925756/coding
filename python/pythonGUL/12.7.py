#！/usr/bin/python
# -*- coding:utf-8 -*-
from tkinter import *
root = Tk()
root.title("顶层窗口")
l = [("red",1),("green",2),("black",3),("blue",4),("yellow",5)]
for text,value in l:
    foo = IntVar()
    c = Checkbutton(root,text=text,variable=foo)
    c.pack(anchor = W)
root.mainloop()