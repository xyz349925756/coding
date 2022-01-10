#！/usr/bin/python
# -*- coding:utf-8 -*-
from tkinter import *
root = Tk()
root.title("顶层窗口")

l= Listbox(root,width=15)
l.pack()
for item in ["apple","bananan","orange","peach","banana"]:
    l.insert(END,item)

root.mainloop()
#列表框