''''
1+2+3+4+...n = n(n+1)/2 -> Theta(n^2)

1+2+4+8+...n = 2n-1 -> Theta(n)

Python Garbage Collector - keeps track of reference counters. If no references, can remove.

---Master Theorem---
    T(n)= aT(n/b) + n^d
    a is # of recursive calls
    n^d is cost of each recursive cost
    n/b is what recursion it is, smaller case
    
    You compare logb(a) vs d
    Logb(a) > d -> Theta(n^logb(a))
    Logb(a) =  d -> Theta(log(n)*n^d)
    Logb(a) < d -> Theta(n^d)
    
    Restrictions: 
    1. a >= 1 - at least 1 sub-problem
    2. b > 1 - have to form sub-problems
'''''
