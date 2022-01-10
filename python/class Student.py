#! /usr/bin/python    python的编码规范
class Student:       #类名首字母大写（Student）
    __name = ""      #私有实例变量前必须有两个下划线
    def __init__(self,name):
        self.__name = name    #self相当于JAVA中的this
    def getName(self):          #方法名首字母小写（get）其后每个单词首字母大写(Name)
        return self.__name


if __name__ == "__main__":
    student = Student("borphi")  #对象名小写
    print(student.getName())
    
#第一行代码定义了一个类，类名首字母大写。
#第二行代码定义了一个私有实例变量，私有实例变量前有两个“_”（下划线）
#第四行代码使用self前缀说明__name私有实例变量属于Student类。
#第五行代码定义了一个公有的方法，方法名首字母小写，其后的单词Name首字母大写，函数的命名规则和方法名相同。
#第九行代码创建了一个student对象，对象名小写。
    #！ /usr/bin/python 这句是兼容linux  unix 操作系统的。
