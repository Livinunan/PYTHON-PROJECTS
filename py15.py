import math
a=int(input("enter no"))
f=0
for i in range (2,math.sqrt(a)):
    if a%i==0:
        f=1
        break
if f==0:
    print("the number is prime")
else:
    print("the number is not prime")   