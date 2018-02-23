'''
    Hash Tables
    More info -> https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/tutorial/
                 http://www.orcca.on.ca/~yxie/courses/cs2210b-2011/htmls/notes/05-hashtable.pdf
'''
'''
    Hashing is implemented in two steps:
        1) An element is converted into an integer by using a hash function. This element can be used as an index to 
           store the original element, which falls into the hash table.
        2) The element is stored in the hash table where it can be quickly retrieved using hashed key.

        hash = hashfunc(key)
        index = hash % array_size
    
    Good Hash Function:
        1) Uniform Distribution Property:
            Each randomly chosen key is equally likely to be mapped to any slot, independent of the slots other keys are
            mapped to.
            
    Collison Resolution Schemes:
    1) Chaining - Each slot would hold a secondary structure, to where all keys that are mapped to that slot would 
       be placed.
    2) Open Addressing - If a slot is already taken, we will try to find another slot for the key.

    Hash Functions:
        Arbitary Domain ---------> Integer(32 Bit) -----------> Indices Domain 
        [     U     ] coding function  [     ] compression function [      ]
        
    Coding function approaches- h: U -> 32-bit integer
        1) Integer Casting: Given an object we take the U lower bytes in its internal representation and consider them 
           as a 32 bit integer.
            Problem : This approach takes only the lower 4 bytes into account, ignoring the rest of the data
        2) Component Sum: x = (x(n-1)....x2,x1,x0)
            h1(x) = x0+x1+x3...x(n-1)
            Problem: Ignores the position of the components
        3) Polynomial Accumulation:  x = (x(n-1)....x2,x1,x0)
            h1(x) = x0 + x1*z + x2 * z^2 + x3 * z^3 ... x(n-1) * z^(n-1) for some value z
            Fun Fact : If you take z = 33, 50,000 English words have at most 6 collisions
            
    Compression function- h2: 32-bit Integers -> [0,1,...,N-1}
        1) Division Method: h2(x) = x mod N -> N is usually a prime number
        2) Mad Method (Multiply, Add, Divide)- 
            h2(x) = [(ax + b) mod p] mod N
            where p is a prime number > |U|
                  a is a random number {1,2,3...,p-1}
                  b is a random number {0,1,2...,p-1}
'''
'''
    Runtime: Find/Insert/Delete
    
    Worst-case: If all keys are mapped to the same slot, the secondary structure would be of the size n, therefore since
        all operations start with searching for the key, this scan could cost Theta(n)
    Best-case: Theta(1)
    Expected time - Average case:
        I) Under the following assumptions:
            1) The keys in the Map were chosen randomly
            2) The hash function we use satisfies the uniform distribution property
        
        II) We define load factor of the table:
               (α) alpha = n/N
               alpha = load factor 
            Under our assumptions the average size of our secondary storage is alpha.
        
        III) Runtime of Find by average case
            Theta(1+alpha)
                1 - calculating the hash function + accessing the slot
                alpha - scanning the secondary structure
            Insert and Delete also take Theta(1+alpha) because they are dominated by Find.
            
        IV) If we keep alpha <= 1 (by always maintaining n <= N) then Theta(1+alpha)avg becomes Theta(1)avg.
        
    Probing Schemes:
        Linear Probing - h(x,i) = h(x) + i 
            First try: h(x)
            Second try: h(x) + 1 
            Third try: h(x) + 2
            
        Quadratic Probing - h(x,i) = (h(x) + i^2) mod N
            Taking quadratic steps
        Double Hashing - h(x,i) = (h'(x) + h''(x) * i) mod N
            First hash -> Initial place
            Second hash -> Number of steps
            h''(x) and N has to be co-prime to avoid endless cycle
'''
