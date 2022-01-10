#! /usr/bin/python
#使用空行分隔符代码
class A:
    def funX(self):
        print("funY()")
#这个空行表示区分方法之间的间隔
    def funY(self):
        print("funY()")
#这个空行表示主程序的入口用于创建A类的对象并调用其方法。
if __name__ == "__main__":
    a = A()
    a.funX()
    a.funY()
    
#代码创建了一个A 的类，A类中定义了2种方法funX（）和funY（）
#空行与代码缩进不同，空行不是必须的，但是方便维护和分开两段代码的含义。空行也是代码的一部分。
