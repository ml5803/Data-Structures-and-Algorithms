import math

'''
    The run time depends on the size of the input
        We parameterize running time by the size of the input
    The running time depends on the operators we use, and on the type
        Ignore machine dependencies -> all primitive operations count as 1
    Runtime depends on machine hardware
        We make asymptotic analysis: look at the growth order of T(n)
        The abstract model we see, divides the algorithms to classes based on their "quality".
    
    Informal Runtime Criteria:
    We compare the asymptotic order of the number of primitive operation executed by a process, as a function of its input size
        T(n) = 3n^2 +6n-15 = O(n^2)
        
    Formal:
        O definition:
            Let f(n) and g(n) be two functions mapping positive integers to positive real numbers.
            We say that f(n) = O(g(n)) if there exist positive real constant c and a positive integer constant n0 such that f(n) =< c*g(n) for all n>=n0
            Ex: 
                Show that 5n+8 = O(n)
                Proof: 
                    Take c = ___ 6
                    Take n0 = ___ 8
                    We then have .... for all n >= 8 
                                    5n+8 <= 5n+n = 6n
                    
                5n+8 <= 5n + n = 6n
                8<=n
                
                Show that 5n+8 = O(n^2)
                Proof:
                    Take c = 13
                    Take n0 = 1
                    We then have ... for all n >= 1
                                    5n+8 <= 5n^2+8n^2 = 13n^2 
                
        Big Ohm definition:
            Let f(n) and g(n) be two functions mapping positive integers to positive real numbers.
            We say that f(n) = Ohm(g(n)) if there exist positive real constant c and a positive integer constant n0 such that f(n) >= c*g(n) for all n>=n0
        
        Theta defintion:
            Let f(n) and g(n) be two functions mapping positive integers to positive real numbers.
            We say that f(n) = Ohm(g(n)) if there exist positive real constant c1,c2 positive integer constant n0 such that c2g(n) <= f(m) <= c1g(n) for all n>=n0
        
            Show that 3n^2+6n-15 = Theta(n^2)
            Proof:
                if we take c1= 9
                           c2= 3
                           n0= 2.5
                Then for all n>=n0 we have:
                    3n^2 <= 3n^2+6n-15 <= 3n^2+6n <= 3n^2+6n^2 = 9n^2
                        6n-15>=0
                        6n>=15
                        n>=2.5
                    3n^2 <= 3n^2+6n-15 <= 9n^2
                Therefore: 3n^2 +6n-15=Theta(n^2)
                
    Rule of thumb to get the order of growth:
        Drop lower-order terms
        Ignore leading constants
        
    isPrime: T1(n) = 1+2+1+5n+2 = 5n + 6 => O(n)
    isPrime2: T2(n) = 1+3+1+5n/2+2 = 2.5n+7 => O(n)
    isPrime3: T3(n) = 1+4+1+5+sqrt(n)+2 = 5sqrt(n)+8 => O(sqrt(n))
'''

'''
    Notes:
        1) a. O is used to express a "<=" relation between functions.
           b. When we say that f(n) = O(g(n)) we mean that g is an upper bound of f.
           
        2) Ohm is used to express a ">=" relation between functions
        
        O is upper bound, Ohm is lower bound
'''
def isPrime(num):
    count_div = 0
    for curr in range(1, num + 1):
        if (num % curr == 0):
            count_div += 1
    if count_div == 2:
        return True
    else:
        return False


def isPrime2(num):
    count_div = 0
    for curr in range(1, num // 2):
        if (num % curr == 0):
            count_div += 1
    if (count_div == 1):
        return True
    else:
        return False


def isPrime3(num):
    count_div = 0 #1
    for curr in range(1, int(math.sqrt(num)) + 1):
        if (num % curr == 0):
            count_div += 1
    if (count_div == 1):
        return True
    else:
        return False