#！ /usr/bin/python
##################################################################
#			文件和流						#			
##################################################################
import sys
sys.stdin = open("hello.txt","r")
for line in sys.stdin.readlines():
    print(line)
"""对象stdin表示流的标准输入，"""
#stdout 标准输出
import sys
sys.stdout = open(r"./hello.txt","a")  #调用open以追加模式打开当前目录下的hello.txt文件，
#并把hello.txt设置为终端输出设备。默认的终端输出设备是系统的控制台。
print("goodbye") #向文件追加输入googbye
sys.stdout.close()#关闭对象stdout
#stderr错误输出
import sys,time
sys.stderr = open("record.log","a")
f = open(r"./hello3.txt","r")
t = time.strftime("%Y-%m-%d %X",time.localtime())
context = f.read()
if context:
    sys.stderr.write(t+""+context)
else:
    raise Exception(t + "异常信息")

