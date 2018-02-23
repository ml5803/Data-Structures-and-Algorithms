class LinkedPriorityQueue:
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next = None

    def __init__(self, head = None):
            self.head = head

    def min(self):
        return self.head

    def max(self):
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        return curr

    def removeMin(self):
        to_del = self.head
        self.head = to_del.next
        to_del = None
        return to_del

    def find(self, key):
        curr = self.head
        while curr is not None:
            if curr.key == key:
                return curr
            elif curr.next is None or curr.next.key < key:
                raise Exception("Nope." + key + " not found")
            else:
                curr = curr.next

    def insert(self,key,value):
        curr = self.head
        if key < curr.key:
            new = LinkedPriorityQueue.Node(key, value)
            new.next = curr
            self.head = new
        else:
            while curr is not None:
                if curr.next is None or curr.next.key > key :
                    new = LinkedPriorityQueue.Node(key,value)
                    new.next = curr.next
                    curr.next = new
                    break

def printQ(lpq):
    curr = lpq.head
    while curr is not None:
        print(curr.key)
        curr = curr.next

head = LinkedPriorityQueue.Node(1,"one")
lpq = LinkedPriorityQueue(head)
lpq.insert(3,"three")
lpq.insert(2,"two")
lpq.insert(0,"zero")