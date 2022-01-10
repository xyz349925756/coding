# coding --utf-8--
# /usr/bin/python

A1 = int(input("请输入持仓数："))
B1 = float(input("请输入持仓成本价："))
C1 = A1 * B1
print("\033[0;31;46m  持仓金额：\033[0m {:.3f}".format(C1))
A2 = int(input("请输入补仓数："))
B2 = float(input("请输入补仓价："))
C2 = A2 * B2
print("\033[1;35;0m补仓金额：\033[0m {:.3f}".format(C2))
print("\033[1;36m补仓后数量：\033[0m", A1 + A2)
#print("\033[1;36;43m 补仓后价位：\033[0m",round((C1 + C2) / (A1 + A2),2))
print("\033[1;36;43m 补仓后价位：\033[0m {:.3f}".format((C1 + C2) / (A1 + A2)))