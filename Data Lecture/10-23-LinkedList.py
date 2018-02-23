'''
    Linked List
'''

'''
    Dynamic Arrays:
        Pros:
            -Random access
            -Efficient amoritized performance for adding and removing from the end
        Cons: 
            -Storing data continuously  in the memory can be a problem for a VERY big data set
            -Insertions and deletions at interior positions of an array are expensive
            -Amortized bounds may be unacceptable in real-time systems
'''

class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

def print_ll(lnk_lst):
    cursor = lnk_lst
    while (cursor is not None):
        print(cursor.data)
        cursor = cursor.next

head = None

head = Node()
head.data = 1

head.next = Node()
head.next.data = 2

head.next.next = Node()
head.next.next.data = 3

#Traversing Linked List
print_ll(head)

print("---INSERT 4---")

#inserting in linked list
new_node = Node()
new_node.data = 4
new_node.next = head
head = new_node

print_ll(head)

def add_first(lnk_lst,elem):
    new_node = Node()
    new_node.data = elem
    new_node.next = lnk_lst
    return new_node

head=add_first(head,5)

print("---Adding to First---")
print_ll(head)

'''
    Singly Linked List
        Data members: data, next
    Doubly Linked List - same as singly but has data member for previous node.
        Data members: prev, data, next
'''

import DoublyLinkedList

def remove_all(lnk_lst, elem):
    if lnk_lst.is_empty():
        return
    cursor = lnk_lst.first_node()
    while cursor is not lnk_lst.trailer:
        if (cursor.data == elem):
            temp = cursor.next
            lnk_lst.delete(cursor)
            cursor = temp
        else:
            cursor = cursor.next

lnk_lst = DoublyLinkedList.DoublyLinkedList()
lnk_lst.add_first(1)
lnk_lst.add_last(2)
lnk_lst.add_first(3)
print(lnk_lst)
remove_all(lnk_lst,1)
print(lnk_lst)

#assumes that linked_lst is not empty
def max_in_linked_lst(lnk_lst):
    return max_in_sublinked_lst(lnk_lst,lnk_lst.first_node())

def max_in_sublinked_lst(lnk_lst, sublist_head):
    if(sublist_head.next is lnk_lst.trailer):
        return sublist_head.data
    else:
        rest_max = max_in_sublinked_lst(lnk_lst, sublist_head.next)
        if(rest_max > sublist_head.data):
            return rest_max
        else:
            return lnk_lst.front_node.data

lnk_lst.add_first(5)
lnk_lst.add_last(8)
print(lnk_lst)
print(max_in_linked_lst(lnk_lst))