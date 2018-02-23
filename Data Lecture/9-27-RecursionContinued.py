'''
 start assumption with WHEN CALLING
'''
def count_up3(start,end):
    if start == end:
        print(start)
    else:
        count_up3(start,(start+end)//2)
        count_up3((start+end)//2+1,end)

# when calling countdown on a smaller range
# it would print the numbers in that range in a decreasing order
def count_down(start,end):
    if start == end:
        print(end)
    else:
        print(end)
        count_down(start,end-1)

# when calling count_up_and_down on a smaller range
# it would print the numbers in that range in an increasing order followed by decreasing order
def count_up_and_down(start,end):
    if(start==end):
        print(end)
    else:
        print(start)
        count_up_and_down(start+1,end)
        print(start)

def factorial(n):
    if(n==1):
        return 1
    else:
        return n * factorial(n-1)

# When calling sum_list with a list shorter than lst, it would return sum of all elements in that list
def sum_list(lst):
    if len(lst)==1:
        return lst[0]
    else:
        return lst[0] + sum_list(lst[1:])

# Can use indicies to make this Theta(n).

'''
    When adding recursion trees, you add local cost of each call.
    Recursive calls mutiple times increase the asymptotic runtime.
'''


# Theta(n)
def power1(x, n):
    if (n == 1):
        return x
    else:
        rest = power1(x, n - 1)
        return x * rest


# Theta(n)
def power2(x, n):
    if (n == 1):
        return x
    else:
        rest1 = power2(x, n // 2)
        rest2 = power2(x, n // 2)
        if (n % 2 == 1):
            return x * rest1 * rest2
        else:
            return rest1 * rest2


# Theta(logn)
def power3(x, n):
    if (n == 1):
        return x
    else:
        rest = power3(x, n // 2)
        if (n % 2 == 0):
            return rest * rest
        else:
            return x * rest * rest