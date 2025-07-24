import math
a = int(input("Starting number: "))
b = int(input("Ending number: "))

for j in range(a, b+1):
    f = 0
    for i in range(2, math.isqrt(j) + 1): 
        if j % i == 0:
            f = 1
            break
    if f == 0 and j > 1:  
        print(j)