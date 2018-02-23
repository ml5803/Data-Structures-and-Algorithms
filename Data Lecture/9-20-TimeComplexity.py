import math
'''
    1. When f(n) is O(g(n)) => f<=g -> g is an upper bound of f
    2. When f(n) is Ohm(g(n)) => f>=g -> g is a lower bound of f
    3. When f(n) = Theta(g(n)) => f=g -> g is a tight bound of f
    
    Refer to 9-20
    
'''

def print_square(n):
    for i in range(1,n+1):
        line = '*'*n #n+1 because building list of asteriks of size n
        print(n) #n because depends on length of string

#total n^2
#T(n) = Theta(n^2)

def print_triangle(n):
    for i in range(1,n+1): #1,2,3...,n n(n+1)/2
        line = '*'*i #i
        print(i) #i

#total 1+2+3+4+...+n = n(n+1)/2 = .5n^2 + .5n
#T(n) = Theta(n^2)

def prefix_average(list):
    n = len(list) #1
    res_lst=[0]*n #n
    for i in range(n):
        curr_avg = sum(list[:i+1])/(i+1) # 2i
        res_lst[i] = curr_avg #1
    return res_lst #1

#T(n)=O(n^2)
y = prefix_average([2,4,6,8])
print(y)

def prefix_average2(list):
    n = len(list)  # 1
    res_lst = [0] * n  # n
    sum = 0 #1
    for i in range(n): #n
        sum += list[i] #1
        res_lst[i] = sum/(i+1) # 1
    return res_lst  # 1

#T(n)=O(n)
z = prefix_average([2,4,6,8])
print(z)