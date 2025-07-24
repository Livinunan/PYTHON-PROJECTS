a=int(input("pin"))
b=p=0
t =a
for i in range (1,5):
    a=a//10    
    if i==2:
        n2=a%10
    if i==4:
        n4=a%10
for j in range (1,5):
    r=t%10
    t=a//10
    if i==2:
        p=p*10+n2
    if i==4:
        p=p*10+n4
    else:
        p=p*10+r
for k in range (1,5):
    r=p%10
    p=p//10
    b=b*10+r
print (b)