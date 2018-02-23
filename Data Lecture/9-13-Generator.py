import math
def my_range_list(start,stop,step):
    res_lst=[]
    curr=start
    while(curr<stop):
        res_lst.append(curr)
        curr+=step
    return res_lst

for elem in my_range_list(3,7,.5):
    print(elem, end = " ")

def f():
    x = 1
    yield x #like a return for an iterator.

    x += 1
    yield x

    x += 1
    yield x

    """
    * When an interpretor sees 'yield' in a function, a generator is created. 
    
    g = f() ->  f is type function, g is type generator
    next(g) -> 1
    next(g) -> 2
    next(g) -> 3
    """

def my_range(start,stop,step):
   curr = start
   while(curr < stop):
       yield curr
       curr+=step

def factors(num):
    possibleFactor = 1
    while (possibleFactor <= num):
        if(num%possibleFactor == 0):
            yield possibleFactor
        possibleFactor+=1

for elem in factors(100):
    print(elem, end = " ")
print()

def isPrime(num):
    count_div = 0
    for curr in range(1,num+1):
        if(num%curr == 0):
            count_div+=1
    if count_div == 2:
        return True
    else:
        return False

def isPrime2(num):
    count_div = 0
    for curr in range(1,num//2):
        if(num%curr == 0):
            count_div += 1
    if (count_div == 0):
        return True
    else:
        return False

def isPrime3(num):
    count_div = 0
    for curr in range(1, int(math.sqrt(num))+1):
        if (num % curr == 0):
            count_div += 1
    if (count_div == 0):
        return True
    else:
        return False