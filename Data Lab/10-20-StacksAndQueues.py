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

    def second_top(stack):
        last = stack.pop()
        second_last = stack.top()
        stack.push(last)
        return second_last

def balanced_expression(str):
    strStack = ArrayStack()
    for i in range(0,len(str)):
        if str[i] in ("(","[","{"):
            strStack.push(str[i])
        elif str[i] == ")" and strStack.top() == "(":
            strStack.pop()
        elif str[i] == "]" and strStack.top() == "[":
            strStack.pop()
        elif str[i] == "}" and strStack.top() == "{":
            strStack.pop()

    return strStack.is_empty()

print(balanced_expression("{{([])}}([])"))
print(balanced_expression("{}{}{"))

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
        old_ind = self.front_ind
        for new_ind in range(self.size):
            self.data[new_ind] = old_data[old_ind]
            old_ind = (old_ind+1) % len(old_data)
        self.front_ind = 0

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
        self.data[avail] = item
        self.size += 1

    def delete_first(self):
        if (self.is_empty()):
            raise EmptyCollection("deque is empty")
        answer = self.data[self.front]
        self.data[self.front]=None
        self.front=(self.front+1) % len(self.data)
        self.size -= 1
        return answer

    def delete_last(self):
        back = (self.front + self.size -1) % len(self.data)
        self.data[back] = None
        self.size -= 1


class MatrixPosition():
    def __init__(self, row = 1, col = 1, direction = ""):
        self.row = row
        self.col = col
        self.direction = direction

    def __eq__(self,other):
        return (self.row == other.row and self.col == other.col and self.direction == other.direction)

    def __repr__(self):
        return "(" + str(self.row) + "," + str(self.col) + ")"

temp_file = open("maze.txt")
lines = temp_file.readlines()
temp_file.close()

maze =[]
for item in lines:
    maze.append(item.split())

def viewMaze():
    for row in maze:
        for item in row:
            print(item, " ", end = "")
        print()

viewMaze()

mazeStack = ArrayStack()
mazeStack.push(MatrixPosition(2,2,"start"))
