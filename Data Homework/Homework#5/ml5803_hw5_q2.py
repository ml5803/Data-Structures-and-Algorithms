#Question 2 - MidStack
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

class ArrayDeque:
    class EmptyCollection(Exception):
        pass

    INIT_CAPACITY = 10

    def __init__(self):
        self.data = [None] * ArrayDeque.INIT_CAPACITY
        self.front = 0
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def first(self):
        if (self.is_empty()):
            raise EmptyCollection("deque is empty")
        return self.data[self.front]

    def last(self):
        if (self.is_empty()):
            raise EmptyCollection("deque is empty")
        back = (self.front+self.size-1)%len(self.data)
        return self.data[back]

    def resize(self,new_capacity):
        old_data = self.data
        self.data = [None] * new_capacity
        old_ind = self.front
        for new_ind in range(self.size):
            self.data[new_ind] = old_data[old_ind]
            old_ind = (old_ind+1) % len(old_data)
        self.front = 0

    def add_first(self,elem):
        if self.size == len(self.data):
            self.resize(2*len(self.data))
        avail = (self.front-1)%len(self.data)
        self.data[avail] = elem
        self.front = (self.front-1)%len(self.data)
        self.size += 1

    def add_last(self,elem):
        if (self.size == len(self.data)):
            self.resize(2 * self.data)
        avail = (self.front + self.size)%len(self.data)
        self.data[avail] = elem
        self.size += 1

    def delete_first(self):
        if (self.is_empty()):
            raise EmptyCollection("deque is empty")
        temp = self.data[self.front]
        self.data[self.front]=None
        self.front=(self.front+1) % len(self.data)
        self.size -= 1
        if self.size < len(self.data)//4:
            self.resize(len(self.data)//2)
        return temp

    def delete_last(self):
        if (self.is_empty()):
            raise EmptyCollection("deque is empty")
        back = (self.front + self.size -1) % len(self.data)
        temp = self.data[back]
        self.data[back] = None
        self.size -= 1
        if self.size < len(self.data)//4:
            self.resize(len(self.data)//2)
        return temp

class MidStack:
    def __init__(self):
        self.stack = ArrayStack()
        self.dq = ArrayDeque()
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size

    def top(self):
        if (self.is_empty()):
            raise EmptyCollection("MidStack is empty")
        return self.dq.last()

    def push(self,elem):
        if self.stack.is_empty():
            self.stack.push(elem)
        elif self.dq.is_empty():
            self.dq.add_last(elem)
        elif len(self.stack) <= len(self.dq):
            self.stack.push(self.dq.delete_first())
            self.dq.add_last(elem)
        else:
            self.dq.add_last(elem)
        self.size += 1

    def pop(self):
        if (self.is_empty()):
            raise EmptyCollection("MidStack is empty")
        if self.dq.is_empty():
            temp = self.stack.pop()
        else:
            temp = self.dq.delete_last()
            self.stack.push(self.dq.delete_first())
        self.size -= 1
        return temp

    def mid_push(self,elem):
        if len(self.stack) == len(self.dq) + 2:
            self.dq.add_first(elem)
        else:
            self.stack.push(elem)
        self.size += 1

x = MidStack()
x.push(2)
x.push(4)
x.push(6)
x.push(8)
x.mid_push(10)
print(x.pop(),end=',')
print(x.pop(),end=',')
print(x.pop(),end=',')
print(x.pop(),end=',')
print(x.pop())

y = MidStack()
y.push(2)
y.push(4)
y.push(6)
y.push(8)
y.push(10)
y.mid_push(12)
print(y.pop(),end=',')
print(y.pop(),end=',')
print(y.pop(),end=',')
print(y.pop(),end=',')
print(y.pop(),end=',')
print(y.pop())


