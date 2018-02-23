class ArrayStack:
    class EmptyCollection(Exception):
        pass

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
            raise ArrayStack.EmptyCollection("Stack is empty")
        return self.data.pop()

    def top(self):
        if (self.is_empty()):
            raise ArrayStack.EmptyCollection("Stack is empty")
        return self.data[-1]

#Question 1 - StackQueue
'''
    The Queue ADT
        Mathematical model: FIFO - First In First Out
        Operations:
            Queue() - initializes an empty queue
            Q.isempty() - returns True if'f Q is empty
            len(Q) - returns the number of elements currently in Q
            Q.enqueue(elem) - add elem to back of queue
            Q.dequeue(elem) - remove and return the element at the front of queue, or raises an exception if Q is empty
            Q.front() - returns the element at the front of queue without removing, or raises an exception if Q is empty
'''
class Queue:
    def __init__(self):
        self.stack_in = ArrayStack()
        self.stack_out = ArrayStack()
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size

    def enqueue(self,elem):
        self.stack_in.push(elem)
        self.size += 1

    def dequeue(self):
        if self.stack_in.is_empty() and self.stack_out.is_empty():
            raise ArrayStack.EmptyCollection("Your queue is empty")
        elif self.stack_out.is_empty():
            while not self.stack_in.is_empty():
                self.stack_out.push(self.stack_in.pop())
        return self.stack_out.pop()

    def front(self):
        if self.stack_in.is_empty() and self.stack_out.is_empty():
            raise ArrayStack.EmptyCollection("Your queue is empty")
        elif self.stack_out.is_empty():
            while not self.stack_in.is_empty():
                self.stack_out.push(self.stack_in.pop())

        if self.stack_out.is_empty():
            raise ArrayStack.EmptyCollection("Your queue is empty")
        else:
            return self.stack_out.top()

# sq = Queue()
# sq.enqueue(1)
# sq.enqueue(2)
# sq.enqueue(3)
# print(sq.dequeue())
# print(sq.dequeue())
# print(sq.dequeue())
#print(sq.dequeue()) #EmptyCollection Exception because empty.