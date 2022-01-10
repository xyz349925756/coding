#！/usr/bin/python
# -*- coding:utf-8 -*-
class peo:
    def __init__(self,name,age,sex):
        self.Name = name
        self.Age = age
        self.Sex = sex
    def speak(self):
        print("my name" + se1f.Name)
    def __str__(self):

        msg = "my name is :"+ self.Name + "\n" + "my age is :" + self.Age + "\n" + "my sex is :" + self.Sex + "."

        return msg
shanghai = peo("shanghai","23","man")
print(shanghai)