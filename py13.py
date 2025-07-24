a=int(input("enter no"))
temp=a
e=0;o=0
while(a!=0):
    r=a%10
    a=a//10
    if r%2==0:
        e=e+1
    else:
        o=o+1
if e>o:
    print("even")
else:
    print("odd")