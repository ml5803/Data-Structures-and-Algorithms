'''
    Abstraction: Separate interface from the implementation
        Interface - ADT (abstract data type)
        Implementation - Data Structure
'''

'''
    ---The stack ADT---
        Follows the LIFO (Last in, First out) mathematical model
        Operations:
            *Stack: creates an empty new stack
            *s.empty(): return True if'f (if and only if) is empty 
            *len(s): returns number of elements in stack
            *s.push(elem): adds elem to top of s
            *s.pop(): removes and returns the top element in s, following the LIFO model or raises an exception if s is empty
            *s.top(): returns top element in s without removing or raise and exception if s is empty
'''
class EmptyCollection(Exception):
    pass

class ArrayStack:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return (len(self)==0)

    def push(self,elem):
        self.data.append(elem)

    def pop(self):
        if(self.is_empty()):
            raise EmptyCollection("Stack is empty")
        return self.data.pop()

    def top(self):
        if (self.is_empty()):
            raise EmptyCollection("Stack is empty")
        return self.data[-1]

S = ArrayStack()
S.push(7)
S.push(5)
S.push(10)
print(S.pop())

#assumes that stack contains at least two elements
def second_top(stack):
    last = stack.pop()
    second_last = stack.top()
    stack.push(last)
    return second_last

def print_in_reverse(s):
    chars_stack = ArrayStack()
    for ch in s:
        chars_stack.push(ch)

    while (not chars_stack.is_empty()):
        ch = chars_stack.pop()
        print(ch,end="")

print_in_reverse("abcd")

'''
    Infix, Prefix, and Postfix Notations (Polish Notation)
    
    Infix:
        3
        2+3
        (5-3)*4
        5-(3*4)
        [(5+2)*(8-3)]/4
    Prefix: <op> <arg1> <arg2>
        3
        +23   
        *-534
        -5*34
        /*+52-834
    Postfix: <arg1> <arg2> <op>
        3
        23+
        53-4*
        534*-
        52+83-*4/
'''

def eval_postfix_exp(exp_str):
    operators = "+-*/"
    exp_lst = exp_str.split()
    S  = ArrayStack()
    for token in exp_lst:
        if(token not in operators):
            S.push(int(token))
        else:
            arg2 = S.pop()
            arg1 = S.pop()
            if token == "+":
                res = arg1 + arg2
            elif token == "-":
                res = arg1 - arg2
            elif token == "*":
                res = arg1 * arg2
            elif token == "/":
                res = arg1 / arg2
            S.push(res)
    return S.pop()

print()
print(eval_postfix_exp("2 2 + 7 *"))