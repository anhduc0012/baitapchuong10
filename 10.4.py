import math
x=int(input("Nhập x:"))
n=int(input("Nhập n:"))
S=((math.pow(x,2)+x+1)**n+(math.pow(x,2)-x+1)**n)
print(S)