class EmptyCollection(Exception):
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
            raise EmptyCollection("List is empty")
        return self.header.next

    def last_node(self):
        if (self.is_empty()):
            raise EmptyCollection("List is empty")
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
            raise EmptyCollection("List is empty")
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

class Integer:
    def __init__(self,string):
        self.num = DoublyLinkedList()
        for elem in string:
            self.num.add_last(elem)

    def __add__(self, other):
        if len(other.num) > len(self.num):
            large = other.num
            small = self.num
            big_length = len(other.num)
            s_length= len(self.num)
        else:
            large = self.num
            small = other.num
            big_length = len(self.num)
            s_length = len(other.num)

        new_num = [0] * (big_length + 1)

        i = 1
        for elem in large:
            new_num[i] = int(elem)
            i+=1

        j = 1 + big_length - s_length
        for elem in small:
            new_num[j] = new_num[j]+int(elem)
            j+=1

        #tracks places
        for k in range(len(new_num)-1,0,-1):
            if new_num[k] > 9:
                new_num[k] = new_num[k]%10
                new_num[k-1] +=1

        if (new_num[0] == 0):
            new_num[0] = None
        return Integer(("".join([str(x) for x in new_num if x is not None])))

    def __str__(self):
        string = "".join([str(x) for x in self.num])
        return string

    def __repr__(self):
        return str(self)

    def __mul__(self, other):
        curr = Integer("0")
        num = 0
        val = [None] * (len(other.num))

        i = 0
        for elem in other.num:
            val[i] = int(elem)
            i += 1

        for i in range(len(val)):
            num += val[i] * 10**(len(val)-i-1)

        for i in range(num):
            curr = curr + self

        return Integer(str(curr))


# n1 = Integer("375")
# n2 = Integer("4029")
# n3 = n1 + n2
# print(n3)
#
# n1 = Integer("3")
# n2 = Integer("9")
# n3 = n1 * n2
# print(n3)