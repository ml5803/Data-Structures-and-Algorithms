#Question 4 - MaxStack
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

class MaxStack:
    def __init__(self):
        self.stack = ArrayStack()
        self.maxVal = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0

    def push(self, elem):
        if(len(self) == 0): #setting max for first run
            self.maxVal = elem
        currMax = self.maxVal
        item = (elem,currMax)
        if elem > self.maxVal:
            self.maxVal = elem
        self.stack.push(item)
        self.size += 1

    def pop(self):
        temp = self.stack.pop()
        if(temp[0]== self.maxVal):
            self.maxVal = temp[1]
        self.size -= 1
        return temp[0]

    def top(self):
        self.stack.top()

    def max(self):
        if len(self) == 0:
            raise Exception("MaxStack is empty")
        return self.maxVal

# maxS = MaxStack()
# maxS.push(3)
# maxS.push(1)
# maxS.push(6)
# maxS.push(4)
# print(str(maxS.max()) + " is the max value")
# print(maxS.pop())
# print(maxS.pop())
# print(str(maxS.max()) + " is the max value")
