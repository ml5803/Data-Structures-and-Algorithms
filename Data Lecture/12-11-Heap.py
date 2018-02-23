'''
    Heap
'''

'''
    Let T be a binary tree. We that that T is a Heap if it satisfies:
        1. Heap order property - In every node n of T, the priority in n is less than or equal to the priorities in n's
            children.
        2. Nearly-complete property - If h is the height of T, then all levels: 0, 1, 2, ..., h-1 have the maximum 
            number of nodes possible (that is, level i has 2^i nodes), and the remaining nodes, at level h-1, reside in 
            the leftmost possible positions.
            
    Observations: Let H be a minimum heap. We have:
        1. The minimum data would be in the root of H.
        2. If H has n nodes, and the height of H is h, then h = Theta(log(n))
            Proof: 2^0+2^1+2^3 ... 2^h-2 <= n <= 2^0+2^1+2^2+2^3 ...2^h-1
                   2^(h-1) - 1 <= n <= 2^h - 1
                   
    Implementation using Array:
        left(i) = 2i
        right(i) = 2i + 1
        parent(i) = i//2
'''