#！ /usr/bin/python
##################################################################
#			函数1						#			
##################################################################
def arithmetic(x=1,y=1,operator="+"):
    result={
            "+" : x + y,
            "-"  : x - y,
            "*"  : x * y,
            "/"  : x / y,
    }
    return result.get(operator)
print(arithmetic(1,2))
print(arithmetic(1,2,"-"))
print(arithmetic(y=3,operator="-"))
#这里用赋值= 是因为 参数的传递。x没有这里赋值，所以必须要赋值，不然python默认就是3-这个就语法错误了
print(arithmetic(x=4,operator="-")) #这里y没有赋值也需要传递所以用“=”
print(arithmetic(y=3,x=4,operator="-"))
"""
第九行，把X=1 y=2赋值结果3
10。1-2 =-1
11.   1-3=-2
12.   4-1=3
13.   4-3=1
"""
