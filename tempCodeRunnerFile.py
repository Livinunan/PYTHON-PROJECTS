a=int(input("enter no"))
f=0
for i in range (2,a//2,1):
    if a%i==0:
        f=1
if f==0:
    print("the number is prime")
else:
    print("the number is no prime")   