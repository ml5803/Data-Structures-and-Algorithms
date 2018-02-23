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
        self.header.next, self.trailer.prev = self.trailer, self.header
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0

    def first_node(self):
        if (self.is_empty()):
            raise Empty("List is empty")
        return self.header.next

    def last_node(self):
        if (self.is_empty()):
            raise Empty("List is empty")
        return self.trailer.prev

    def add_first(self, elem):
        return self.add_after(self.header, elem)

    def add_last(self, elem):
        return self.add_after(self.trailer.prev, elem)

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
        return self.add_after(node.prev, elem)

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
        while (cursor is not self.trailer):
            yield cursor.data
            cursor = cursor.next

    def __str__(self):
        return '[' + '<-->'.join([str(x) for x in self]) + ']'

    def __repr__(self):
        return str(self)


def merge_linked_lists(lst1,lst2):
    return merge_sublists(lst1.header.next,lst2.header.next,DoublyLinkedList())

def merge_sublists(node1, node2, result):
    if node1.data is None:
        while node2.next is not None:
            result.add_last(node2.data)
            node2=node2.next
        return result
    elif node2.data is None:
        while node1.next is not None:
            result.add_last(node1.data)
            node1=node1.next
        return result

    if node1.next is None and node2.data is None:
        return result
    elif node1.next is None or node2.next is None:
        if node1.next is None:
            temp = node2
        else:
            temp = node1
        while temp.next is not None:
            result.add_last(temp.data)
            temp=temp.next
        return result
    else:
        if node1.data < node2.data:
            result.add_last(node1.data)
            return merge_sublists(node1.next,node2,result)
        else:
            result.add_last(node2.data)
            return merge_sublists(node2.next,node1,result)

# srt_lst1 = DoublyLinkedList()
# srt_lst1.add_last(1)
# srt_lst1.add_last(5)
# srt_lst1.add_last(5)
# srt_lst1.add_last(7)
#
# srt_lst2 = DoublyLinkedList()
#
# print(merge_linked_lists(srt_lst1,srt_lst2))