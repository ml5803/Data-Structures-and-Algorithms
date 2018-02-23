#Question 5 - Permutation
class EmptyCollection(Exception):
    pass

class ArrayQueue:
    INITIAL_CAPACITY = 10

    def __init__(self):
        self.data = [None] * ArrayQueue.INITIAL_CAPACITY
        self.num_of_elems = 0
        self.front_ind = 0

    def __len__(self):
        return self.num_of_elems

    def __str__(self):
        return str(self.data)

    def is_empty(self):
        return (self.num_of_elems == 0)

    def enqueue(self, elem):
        if (self.num_of_elems == len(self.data)):
            self.resize(2 * len(self.data))
        back_ind = (self.front_ind + self.num_of_elems) % len(self.data)
        self.data[back_ind] = elem
        self.num_of_elems += 1

    def dequeue(self):
        if (self.is_empty()):
            raise EmptyCollection("Queue is empty")
        value = self.data[self.front_ind]
        self.data[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % len(self.data)
        self.num_of_elems -= 1
        if(self.num_of_elems < len(self.data) // 4):
            self.resize(len(self.data) // 2)
        return value

    def first(self):
        if self.is_empty():
            raise EmptyCollection("Queue is empty")
        return self.data[self.front_ind]

    def resize(self, new_cap):
        old_data = self.data
        self.data = [None] * new_cap
        old_ind = self.front_ind
        for new_ind in range(self.num_of_elems):
            self.data[new_ind] = old_data[old_ind]
            old_ind = (old_ind + 1) % len(old_data)
        self.front_ind = 0

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

def permutations(lst):
    queue = ArrayQueue()
    stack = ArrayStack()
    for i in lst:
        if len(queue) == 0:
            queue.enqueue([i])
        else:
            while len(queue)>0:
                temp = queue.dequeue()
                for j in range(len(temp)+1):
                    stack.push(temp[:j]+[i]+temp[j:])
        while len(stack) > 0:
            queue.enqueue(stack.pop())

    l = []
    for i in range(len(queue)):
        l.append(queue.dequeue())
    return l

# print(permutations([1,2,3]))