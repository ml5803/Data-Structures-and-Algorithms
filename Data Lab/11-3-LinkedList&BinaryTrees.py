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

def flatten_linked_lst(lnk_lst):
    new = DoublyLinkedList()
    return flatten_sub_linked(new,lnk_lst,lnk_lst.first_node())


def flatten_sub_linked(new, lnk_lst, node):
    if(node is lnk_lst.last_node() and isinstance(node.data, int)):
        new.add_last(node.data)
        print("am i running")
        print("if",new)
    else:
        print("else",new)
        if isinstance(node.data,int):
            new.add_last(node.data)
            flatten_sub_linked(new,lnk_lst,node.next)
            print("elseif",new)
        else:
            print("elseelse",new)
            flatten_sub_linked(new,node.data,node.data.first_node())
    return new

lnk_lst1 = DoublyLinkedList()
elem1 = 1
lnk_lst1.add_last(elem1)
elem2 = DoublyLinkedList()
elem2.add_last(2)
elem2.add_last(3)
lnk_lst1.add_last(elem2)
elem3= 4
lnk_lst1.add_last(elem3)
lnk_lst2 = flatten_linked_lst(lnk_lst1)
print(lnk_lst1)
print(lnk_lst2)

input()