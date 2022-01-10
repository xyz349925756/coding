#！ /usr/bin/python
##################################################################
#			字符串的查找替换                         			#			
##################################################################
sentence = "This is a apple!"
print(sentence.find("a"))
sentence ="This is a apple!"
print(sentence.rfind("a"))
print("#######################")
sentence = "hello world,hello China"
print(sentence.replace("hello","hi")) #把hello替换为hi
print(sentence.replace("hello","hi",1)) #把hello替换为hi ，只替换一次。
print(sentence.replace("abc","hi"))#把abc替换为hi ，里面没有abc这个字符串所以返回原值sentence
"""replace 在操作的过程中先备份字符串再变更，所以上面第三局输出原句"""
