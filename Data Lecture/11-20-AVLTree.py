'''
    AVL Trees
'''

'''
    Claim #1: Let T be a binary tree. We have:
    T is a binary-search tree <-> The inorder sequence of T is sorted in an ascending order
    
    Claim #2: Let T be an AVL Tree with n nodes. We then have that height(T) = Theta(logn)
    
    Height-Balanced Property
        For every node of T, the heights of the children of n differ by at most 1.
        
    AVL Tree
        Let T be a binary tree. We say that T is an AVL Tree if:
        1. It is a binary search tree
        2. It satisfies the height-balance property
        
    Single Rotations
        1. Left Rotation
        2. Right Rotation
        
    Double Rotation
        1. RL Rotation
        2. LR Rotation
'''

'''
    AVL Insert:
    Insert k into an AVL Tree:
    -Apply the insert algorithm of k as if the tree is a regular BinarySearchTree
        As a result, the balancing property could be violated
    -Walk from the new node (with k) upwards n the insertion path.
    -Let z be the first node in this walk that is not balanced(The difference between z's two children is 2)
    -Let y be z's higher child (k was inserted into y's subtree)
    -Determine if you are in the outside-case or in the inside-case
        If you are in the outside-case, do the corresponding single rotation
        If you are in the inside-case, do the corresponding double rotation
        
'''
'''
    Practice: Make AVL Tree using 14,17,11,7,53,4,13,12,8
'''