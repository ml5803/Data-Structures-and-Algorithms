def factors(num):
    import math
    for i in range(1,int(math.sqrt(num))):
        if(num%i==0):
            yield i

    for j in range(int(math.sqrt(num)),0,-1):
        if(num%j==0):
            yield num//j

for curr in factors(100):
    print(curr)

for curr in factors(36):
    print(curr)