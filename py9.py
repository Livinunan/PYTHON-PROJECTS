a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
if a < b and a < c:
    smallest = a
    if b < c:
        second_largest =b
        largest = c
    else:
        second_largest = c
        largest = b
elif b < a and b < c:
    smallest = b
    if b < c:
        second_largest = a
        largest = b
    else:
        second_largest = c
        largest = a
else:
    smallest = c
    if a < b:
        second_largest =a
        largest = b
    else:
        second_largest = b
        largest = a

if smallest == a:
    if second_largest ==b:
        a=a+b
        b=a-b
        a=a-b
    else:
        a=a+c
        c=a-c
        c=a-c
elif smallest == b:
    if second_largest == a:
        a=a+b
        b=a-b
        a=a-b
    else:
        b=b+c
        c=b-c
        c=b-c
else:
    if second_largest == a:
        a=a+c
        c=a-c
        c=a-c
    else:
        b=b+c
        c=b-c
        c=b-c

print("After swapping:")
print("First number:", a)
print("Second number:", b)
print("Third number:", c)
