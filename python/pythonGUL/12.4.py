#！/usr/bin/python
# -*- coding:utf-8 -*-
from tkinter import *
root = Tk()
root.title("顶层窗口")
Button(root,text="禁用",state=DISABLED).pack(side=LEFT)
Button(root,text="取消").pack(side=LEFT)
Button(root,text="确定").pack(side=LEFT)
Button(root,text="退出",command = root.quit).pack(side=RIGHT)
root.mainloop()
#按钮
