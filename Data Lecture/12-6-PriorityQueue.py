'''
    Priority Queue ADT
'''

'''
    Data Model: A collection of priority-value pairs, that comes out in an increasing priorities order
    
    Operations:
        p = PriorityQueue() - Creates an empty priority queue
        p.insert(pri,val) - Inserts an item with priority (pri) and value (val) to p.
        p.min() - returns the pair (pri,val) with the lowest priority p, or raises an Exception, if p is empty
        p.delete_min() - removes and returns the pair (pri,val) with the lowest priority in p, or raises an Exception, 
            if p is empty.
        len(p) - return the number of items in p
        p.is_empty() returns True if length is 0
        
'''