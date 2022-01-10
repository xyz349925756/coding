#！ /usr/bin/python
##################################################################
#			函数2						#			
##################################################################
#参数可以是变量，元组，列表等内置数据
def arithmetic(args=[],operator="+"):
    x = args[0]
    y = args[1]
    result = {
            "+":x + y,
            "-":x - y,
            "*":x * y,
            "/":x / y
        }
    return result.get(operator)
print(arithmetic([1, 2]))
print(type(arithmetic([1,2])))

print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

def append(args=[]):#定义了一个append()函数，默认值是args列表
    args.append(0) #在列表中追加一个元素0
    print(args)

append() #输出默认列表
append([1]) #追加列表【1】，append默认追加(0)元素结果是【1，0】
append() #再次调用append，此时使用的还是以前的args，因此args在原有的基础上将再加上一个元素0
#结果【0，0】
print("$$$$$$$$$$$$$$$$$这里的结果是预料之外的$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

def append(args=[]):
    if len(args) <= 0:      #这里添加if语句是避免结果计算不准。len()判断列表args的长度是否大于0.
        args = []            #如果args小于0，那么args就重置。即取消了函数的绑定。
    args.append(0) 
    print(args)

append() 
append([1]) 
append() 
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

#传递可变参数
def func(*args):
    print(args)
func(1,2,3)
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

#*必须在**前面。
def search(*t,**d):  #这里是*t 对应最后一行的"one""three"组成一个元组
    #**d与“one=1”,"two=2","three=3"对应。生成一个字典{one:"1",two:"2":three:"3"}
    keys = d.keys()
    values = d.values()
    print(keys)    #输出【'one', 'two', 'three'】
    print(values) #['3','2','1']
    for arg in t:
        for key in keys:
            if arg ==key:
                print("find:",d[key])
search("one","three",one="1",two="2",three="3")











