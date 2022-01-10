#！ /usr/bin/python
##################################################################
#				字符串的反转				#			
##################################################################
"""
字符串的反转是指把字符串中最后一个字符移到第一位，按照倒序的方式依次前移，并通过循环对字符
串进行反转。
JAVA代码如下：
public static String reverse(String s)
{
    int length = s.length();
    StringBuffer result = new StringBuffer(length);
    for (int i = length - 1;i >= 0;i--):
          result.append(s.charAt(i));
    return result.toString();    
}
"""

def reverse(s): #定义reverse（s）函数，s是表示需要反转的字符串。
    out = ""     #定义了一个返回变量out，用于存放反转后的结果
    li = list(s)  #创建列表li，字符串的字符成为列表的元素
    for i in range(len(li),0,-1):   #从列表最后一个处理并依次链接到变量out中。
        out += "".join(li[i-1])
    return out
print(reverse("hello"))
