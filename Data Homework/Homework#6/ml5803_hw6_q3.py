#Question 3 - CompactString

class CompactString:
    def __init__(self,string):
        if (string != ""):
            count = 0
            comp_elem = string[0]
            self.dll = DoublyLinkedList()
            for elem in string:
                if comp_elem == elem:
                    count += 1
                else:
                    self.dll.add_last((comp_elem,count))
                    comp_elem = elem
                    count = 1
            self.dll.add_last((comp_elem, count))
        else:
            self.dll = DoublyLinkedList()

    def __add__(self, other):
        temp = CompactString("")
        new = temp.dll
        for i in self.dll:
            new.add_last(i)
        for j in other.dll:
            if(j[0] == new.last_node().data[0]):
                temp_num = new.last_node().data[1] + j[1]
                temp_char = new.last_node().data[0]
                new.delete(new.last_node())
                new.add_last((temp_char,temp_num))
            else:
                new.add_last(j)
        return new

    def __lt__(self,other):
        if len(self.dll)<=0:
            return True
        elif len(other.dll) <= 0:
            return False
        self_pointer = self.dll.first_node()
        other_pointer = other.dll.first_node()
        while(self_pointer is not self.dll.trailer and other_pointer is not other.dll.trailer):
            if self_pointer.data[0] > other_pointer.data[0]:
                return False
            elif self_pointer.data[0] < other_pointer.data[0]:
                return True
            elif self_pointer.data[0] == other_pointer.data[0] and self_pointer is self.dll.last_node() and other_pointer is other.dll.last_node():
                return self_pointer.data[1] < other_pointer.data[1]
            elif self_pointer.data[0] == other_pointer.data[0] and self_pointer is self.dll.last_node():
                return True
            elif self_pointer.data[0] == other_pointer.data[0] and other_pointer is other.dll.last_node():
                return False
            elif self_pointer.data[0] == other_pointer.data[0] and self_pointer.data[1] != other_pointer.data[1]:
                return self_pointer.data[1] < other_pointer.data[1] and self_pointer.next.data[0] < other_pointer.data[0] or self_pointer.data[1] > other_pointer.data[1] and ((self_pointer.data[1] > other_pointer.data[1]) and (other_pointer.next.data[0] > self_pointer.data[0]))
            self_pointer = self_pointer.next
            other_pointer = other_pointer.next
        return False

    def __le__(self,other):
        if len(self.dll)<=0:
            return True
        elif len(other.dll) <= 0:
            return False
        self_pointer = self.dll.first_node()
        other_pointer = other.dll.first_node()
        while(self_pointer is not self.dll.trailer and other_pointer is not other.dll.trailer):
            if self_pointer.data[0] > other_pointer.data[0]:
                return False
            elif self_pointer.data[0] < other_pointer.data[0]:
                return True
            elif(self_pointer.data[0] == other_pointer.data[0] and self_pointer is self.dll.last_node() and other_pointer is other.dll.last_node()):
                return self_pointer.data[1] <= other_pointer.data[1]
            elif (self_pointer.data[0] == other_pointer.data[0] and self_pointer is self.dll.last_node()):
                return True
            elif (self_pointer.data[0] == other_pointer.data[0] and other_pointer is other.dll.last_node()):
                return False
            elif self_pointer.data[0] == other_pointer.data[0] and self_pointer.data[1] != other_pointer.data[1]:
                return self_pointer.data[1] < other_pointer.data[1] and self_pointer.next.data[0] < other_pointer.data[0] or self_pointer.data[1] > other_pointer.data[1] and ((self_pointer.data[1] > other_pointer.data[1]) and (other_pointer.next.data[0] > self_pointer.data[0]))
            self_pointer = self_pointer.next
            other_pointer = other_pointer.next
        return False

    def __gt__(self,other):
        return not(self<=other)

    def __ge__(self, other):
        return not(self<other)

    def __str__(self):
        string = ""
        for i in self.dll:
            for j in range(i[1]):
                string+=i[0]
        return string

    def __repr__(self):
        return str(self)

class Empty(Exception):
    pass

class DoublyLinkedList:
    class Node:
        def __init__(self, prev=None, data=None, next=None):
            self.prev = prev
            self.data = data
            self.next = next

        def disconnect(self):
            self.data = None
            self.next = None
            self.prev = None

    def __init__(self):
        self.header = DoublyLinkedList.Node()
        self.trailer = DoublyLinkedList.Node()
        self.header.next,self.trailer.prev = self.trailer,self.header
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0

    def first_node(self):
        if(self.is_empty()):
            raise Empty("List is empty")
        return self.header.next

    def last_node(self):
        if (self.is_empty()):
            raise Empty("List is empty")
        return self.trailer.prev

    def add_first(self, elem):
        return self.add_after(self.header,elem)

    def add_last(self, elem):
        return self.add_after(self.trailer.prev,elem)

    def add_after(self, node, elem):
        prev = node
        succ = node.next
        new_node = DoublyLinkedList.Node()
        new_node.data = elem
        new_node.prev = prev
        new_node.next = succ
        prev.next = new_node
        succ.prev = new_node
        self.size += 1
        return new_node

    def add_before(self, node, elem):
        return self.add_after(node.prev,elem)

    def delete(self, node):
        if (self.is_empty()):
            raise Empty("List is empty")
        prev = node.prev
        succ = node.next
        prev.next = succ
        succ.prev = prev
        self.size -= 1
        data = node.data
        node.disconnect()
        return data

    def __iter__(self):
        if self.is_empty():
            return
        cursor = self.first_node()
        while(cursor is not self.trailer):
            yield cursor.data
            cursor = cursor.next

    def __str__(self):
        return '[' + '<-->'.join([str(x) for x in self]) + ']'

    def __repr__(self):
        return str(self)

x = CompactString("aaaabccc")
y = CompactString("aaabccc")
print(x<y)
print(x>y)
print(x<=y)
print(x>=y)
print()

x = CompactString("bbbbaaaac")
y = CompactString("bbbbbaaaacc")
print(x<y)
print(x>y)
print(x<=y)
print(x>=y)

print()
x = CompactString("bbbbaaaac")
y = CompactString("bbbbaaaac")
print(x<y)
print(x>y)
print(x<=y)
print(x>=y)