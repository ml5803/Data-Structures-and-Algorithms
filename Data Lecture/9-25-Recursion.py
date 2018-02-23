'''
    Searching
'''

# T(n) = Theta(# of Iteration)
# Tworst(n) = Theta(n)

def linear_search(lst,val):
    for i in range(len(lst)):
        if(lst[i]==val):
            return i

    return None

#Tworst(n) = Theta(log(n))
def binary_search(srt_lst, val):
    left = 0
    right = len(srt_lst)-1
    ind = None
    found = False

    while(found == False and left <= right):
        mid = (left+right)//2
        if(srt_lst[mid]==val):
            found = True
            ind = mid
        elif(srt_lst[mid] > val):
            right = mid
        else: #srt_lst[mid] < val
            left = mid
    return None

'''
    -----RECURSION-----
    In computer science: A problem solving technique, closely related to mathematical induction
    where we define the solution as a combination of solutions to smaller instances of the same problem.
    
    -----DEVELOPING A RECURSIVE ALGORITHM-----
    Step 1: The Base Case:
        Solve the problem for the smallest possible input
    Step 2: The Recursive Step:
        Define the recursion hypothesis - assume that "when calling the function on a smaller input, it does its job"
            *In the case of count_up: Assume that "When calling count_up in a smaller range it would print all numbers in that
            range in an increasing order
        Based on this assumption, find how to combine calls to smaller instances, in order to solve the problem for the given input
'''

#start<=end
def count_up(start,end):
    if(start==end):
        print(start)
    else:
        print(start)
        count_up(start+1,end)


def count_up2(start,end):
    if start == end:
        print(start)
    else:
        count_up(start,end-1)
        print(end)