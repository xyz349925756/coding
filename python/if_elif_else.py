#！ /usr/bin/python

###################################################################
#								  #
#								  #
#		if...elif...else				  #
#								  #
#								  #
###################################################################


score = float(input("score:"))
if 90 <= score <= 100:
    print("A")
elif 80 <= score < 90:
    print("B")
elif 70 <= score < 80:
    print("C")
else:
    print("D")
