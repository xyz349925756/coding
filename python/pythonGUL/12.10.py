#！/usr/bin/python
# -*- coding:utf-8 -*-
from tkinter import *
root = Tk()
root.title("顶层窗口")


l = Listbox(root,height=6,width=15)
scroll = Scrollbar(root,command=l.yview)
l.configure(yscrollcommand=scroll.set)
l.pack(side=LEFT)
scroll.pack(side=RIGHT,fill=Y)
for item in range(20):
    l.insert(END,item)


root.mainloop()
#滚动条