#!/usr/bin/python
#代码缩进
x = 2   #创建变量x并赋值为1.在赋值运算符两侧各添加了一个空格，是一种良好的书写习惯。
if x == 1: #判断X值是否等于1，if表达式后输入了一个冒号，冒号后面的代码块需要缩进，本行与第一行在同一个层次。
    print("x =",x) #代码缩进 如果x等于1则输出X=1。
else:
    print("x =",x) #代码缩进
    x=x+1          #代码缩进
print("x =",x)


#上面这段代码是简单的判断，首先定义了一个变量x，并赋值为1，接着是判断的开始，if x == 1则执行下一层
#代码输出x的值，if 不等于1 则执行下一步 else 并打印结果,譬如x=2 就不符合第一个条件，代码执行else
#输出x=2  x=x+1在这并没有执行。 输出x=2并没有完，接着 执行x=x+1 即 x=2+1
#输出x=3这里print（“x =”,x）是第一层次的
