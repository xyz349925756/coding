#！/usr/bin/python
# -*- coding:utf-8 -*-
from tkinter import *

class App:   #定义了一个APP类
    def __init__(self,master):   #定义了窗体
        frame = Frame(master)
        frame.pack()

        self.hello = Button(frame,text="Hello",fg="blue",command = self.hello)
        self.hello.pack(side=LEFT)

        self.quit = Button(frame,text="Quit",fg = "red",command = frame.quit)
        self.quit.pack(side=RIGHT)

    def hello(self):
        print("未知选项")

root = Tk()

root.wm_title("标题")   #设置标题
root.wm_minsize(200,200)   #设置窗口大小

app = App(root)

root.mainloop()