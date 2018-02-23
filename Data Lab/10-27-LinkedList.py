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

class LinkedStack:
    def __init__(self):
        self.link = DoublyLinkedList()
        self.size = 0

    def __len__(self):
        return self.size

    def push(self,elem):
        self.link.add_last(elem)
        self.size += 1

    def is_empty(self):
        return len(self) == 0

    def pop(self):
        if(self.size == 0):
            raise EmptyCollection("LinkedStack is empty")
        else:
            self.size -= 1
            return(self.link.delete(self.link.trailer.prev))

    def top(self):
        if (self.size == 0):
            raise EmptyCollection("LinkedStack is empty")
        else:
            return self.link.trailer.data

class LeakyStack():
    def __init__(self,max):
        self.link = DoublyLinkedList()
        self.size = 0
        self.max = max

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0

    def push(self,e):
        if self.size < self.max:
            self.link.add_first(e)
            self.size += 1
        else:
            self.link.delete(self.link.trailer.prev)
            self.link.add_first(e)

    def top(self):
        if(self.is_empty()):
            raise EmptyCollection("LeakyStack is empty")
        else:
            return self.link.last_node().data

    def pop(self):
        self.size -= 1
        return self.link.delete(self.link.trailer.prev)

s = LeakyStack(5)
s.push(2)
s.push(13)
s.push(3)
s.push(8)
s.push(5)

def reverse_list1(lnk_lst):
    f_point = lnk_lst.first_node()
    e_point = lnk_lst.last_node()
    while(f_point is not e_point or f_point.prev is not e_point):
        f_point.data,e_point.data = e_point.data, f_point.data
        f_point = f_point.next
        e_point = e_point.prev

def reverse_list2(lnk_lst):
    point = lnk_lst.first_node()
    while(point is not lnk_lst.trailer):
        point.next, point.prev = point.prev, point.next
        point = point.prev

def reverse_list3(lnk_lst):
    point = lnk_lst.first_node()
    to_move = lnk_lst.first_node().next
    lnk_lst.add_last(lnk_lst.delete(point))
    while(to_move is not point):
        temp = to_move.next
        lnk_lst.add_last(lnk_lst.delete(to_move))
        to_move = temp