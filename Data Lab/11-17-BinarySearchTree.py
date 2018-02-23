'''
    The Queue ADT
        Mathematical model: FIFO - First In First Out
        Operations:
            Queue() - initializes an empty queue
            Q.isempty() - returns True if'f Q is empty
            len(Q) - returns the number of elements currently in Q
            Q.enqueue(elem) - add elem to back of queue
            Q.dequeue(elem) - remove and return the element at the front of queue, or raises an exception if Q is empty
            Q.front() - returns the element at the front of queue without removing, or raises an exception if Q is empty
'''
class EmptyCollection(Exception):
    pass

class ArrayQueue:
    INIT_CAPACITY = 10

    def __init__(self):
        self.data = [None] * ArrayQueue.INIT_CAPACITY
        self.front_ind = 0
        self.num_of_elems = 0

    def __len__(self):
        return self.num_of_elems

    def is_empty(self):
        return (len(self) == 0)

    def enqueue(self, elem):
        if (self.num_of_elems == len(self.data)):
            self.resize(2 * len(self.data))
        back_ind = (self.front_ind + self.num_of_elems) % len(self.data)
        self.data[back_ind] = elem
        self.num_of_elems += 1

    def dequeue(self):
        if (self.is_empty()):
            raise EmptyCollection("Queue is empty")
        elem = self.data[self.front_ind]
        self.data[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % len(self.data)
        self.num_of_elems -= 1
        if (self.num_of_elems < len(self.data) // 4):
            self.resize(len(self.data) // 2)
        return elem

    def front(self):
        if (self.is_empty()):
            raise EmptyCollection("Queue is empty")
        return self.data[self.front_ind]

    def resize(self, new_capacity):
        old_data = self.data
        self.data = [None] * new_capacity
        old_ind = self.front_ind
        for new_ind in range(self.num_of_elems):
            self.data[new_ind] = old_data[old_ind]
            old_ind = (old_ind + 1) % len(old_data)
        self.front_ind = 0



class EmptyCollection(Exception):
    pass

class LinkedBinaryTree:
    class Node:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.left = left
            if (self.left is not None):
                self.left.parent = self
            self.right = right
            if (self.right is not None):
                self.right.parent = self
            self.parent = None

    def __init__(self,root=None):
        self.root = root
        self.size = self.subtree_count(self.root)

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0

    def subtree_count(self,subtree_root):
        if(subtree_root is None):
            return 0
        else:
            left_count = self.subtree_count(subtree_root.left)
            right_count = self.subtree_count(subtree_root.right)
            return left_count + right_count + 1

    def sum_of_a_tree(self):
        return self.subtree_sum(self.root)

    def subtree_sum(self, subtree_root):
        #total cost = # of nodes in the recursion = # of black nodes + # of green nodes <= n+2n = 3n
                                                           #n                  #2n
        #b/c each black node can spawn a maximum of 2 green nodes but not all nodes are black nodes so <= 2n.
        if(subtree_root is None):
            return 0
        else:
            left_sum = self.subtree_sum(subtree_root.left)
            right_sum = self.subtree_sum(subtree_root.right)
            return left_sum + right_sum + subtree_root.data

    def height(self):
        if(self.is_empty()):
            raise EmptyCollection("Height is not defined for an empty tree")
        return self.subtree_height(self.root)

    #Assuming subtree_root is not empty
    def subtree_height(self,subtree_root):
        #Theta(n)
        if(subtree_root.left is None and subtree_root.right is None):
            return 0
        elif(subtree_root.left is None):
            return self.subtree_count(subtree_root.right) + 1
        elif(subtree_root.right is None):
            return self.subtree_count(subtree_root.left) + 1
        else:
            left_height = self.subtree_height(subtree_root.left)
            right_height = self.subtree_count(subtree_root.right)
            return max(left_height,right_height) + 1

    def __iter__(self):
        for node in self.inorder():
            yield node.data

    def preorder(self):
        yield from self.subtree_preorder(self.root)

    def subtree_preorder(self,subtree_root):
        if subtree_root is None:
            return
        else:
            yield subtree_root
            yield from self.subtree_preorder(subtree_root.left)
            yield from self.subtree_preorder(subtree_root.right)

    def inorder(self):
        yield from self.subtree_inorder(self.root)

    def subtree_inorder(self,subtree_root):
        if subtree_root is None:
            return
        else:
            yield from self.subtree_inorder(subtree_root.left)
            yield subtree_root
            yield from self.subtree_inorder(subtree_root.right)

    def postorder(self):
        yield from self.subtree_postorder(self.root)

    def subtree_postorder(self,subtree_root):
        if subtree_root is None:
            return
        else:
            yield from self.subtree_postorder(subtree_root.left)
            yield from self.subtree_postorder(subtree_root.right)
            yield subtree_root

    def breadth_first(self):
        #have a queue
        #remove first item, add children
        if self.is_empty():
            return
        nodes_q = ArrayQueue.ArrayQueue()
        nodes_q.enqueue(self.root)
        while(nodes_q.is_empty() == False):
            curr = nodes_q.dequeue()
            yield curr
            if curr.left is not None:
                nodes_q.enqueue(curr.left)
            if curr.right is not None:
                nodes_q.enqueue(curr.right)



class BinarySearchTreeMap:

    class Item:
        def __init__(self, key, value=None):
            self.key = key
            self.value = value

    class Node:
        def __init__(self, item):
            self.item = item
            self.parent = None
            self.left = None
            self.right = None

        def num_children(self):
            count = 0
            if (self.left is not None):
                count += 1
            if (self.right is not None):
                count += 1
            return count

        def disconnect(self):
            self.item = None
            self.parent = None
            self.left = None
            self.right = None


    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0


    # raises exception if not found
    def __getitem__(self, key):
        node = self.subtree_find(self.root, key)
        if (node is None):
            raise KeyError(str(key) + " not found")
        else:
            return node.item.value

    # returns None if not found
    def subtree_find(self, subtree_root, key):
        curr = subtree_root
        while (curr is not None):
            if (curr.item.key == key):
                return curr
            elif (curr.item.key > key):
                curr = curr.left
            else:  # (curr.item.key < key)
                curr = curr.right
        return None


    # updates value if key already exists
    def __setitem__(self, key, value):
        node = self.subtree_find(self.root, key)
        if (node is None):
            self.subtree_insert(key, value)
        else:
            node.item.value = value

    # assumes key not in tree
    def subtree_insert(self, key, value=None):
        item = BinarySearchTreeMap.Item(key, value)
        new_node = BinarySearchTreeMap.Node(item)
        if (self.is_empty()):
            self.root = new_node
            self.size = 1
        else:
            parent = self.root
            if(key < self.root.item.key):
                curr = self.root.left
            else:
                curr = self.root.right
            while (curr is not None):
                parent = curr
                if (key < curr.item.key):
                    curr = curr.left
                else:
                    curr = curr.right
            if (key < parent.item.key):
                parent.left = new_node
            else:
                parent.right = new_node
            new_node.parent = parent
            self.size += 1


    #raises exception if key not in tree
    def __delitem__(self, key):
        if (self.subtree_find(self.root, key) is None):
            raise KeyError(str(key) + " is not found")
        else:
            self.subtree_delete(self.root, key)

    #assumes key is in tree + returns value assosiated
    def subtree_delete(self, node, key):
        node_to_delete = self.subtree_find(node, key)
        value = node_to_delete.item.value
        num_children = node_to_delete.num_children()

        if (node_to_delete is self.root):
            if (num_children == 0):
                self.root = None
                node_to_delete.disconnect()
                self.size -= 1

            elif (num_children == 1):
                if (self.root.left is not None):
                    self.root = self.root.left
                else:
                    self.root = self.root.right
                self.root.parent = None
                node_to_delete.disconnect()
                self.size -= 1

            else: #num_children == 2
                max_of_left = self.subtree_max(node_to_delete.left)
                node_to_delete.item = max_of_left.item
                self.subtree_delete(node_to_delete.left, max_of_left.item.key)

        else:
            if (num_children == 0):
                parent = node_to_delete.parent
                if (node_to_delete is parent.left):
                    parent.left = None
                else:
                    parent.right = None

                node_to_delete.disconnect()
                self.size -= 1

            elif (num_children == 1):
                parent = node_to_delete.parent
                if(node_to_delete.left is not None):
                    child = node_to_delete.left
                else:
                    child = node_to_delete.right

                child.parent = parent
                if (node_to_delete is parent.left):
                    parent.left = child
                else:
                    parent.right = child

                node_to_delete.disconnect()
                self.size -= 1

            else: #num_children == 2
                max_of_left = self.subtree_max(node_to_delete.left)
                node_to_delete.item = max_of_left.item
                self.subtree_delete(node_to_delete.left, max_of_left.item.key)

        return value

    # assumes non empty subtree
    def subtree_max(self, curr_root):
        node = curr_root
        while (node.right is not None):
            node = node.right
        return node


    def inorder(self):
        for node in self.subtree_inorder(self.root):
            yield node

    def subtree_inorder(self, curr_root):
        if(curr_root is None):
            pass
        else:
            yield from self.subtree_inorder(curr_root.left)
            yield curr_root
            yield from self.subtree_inorder(curr_root.right)

    def __iter__(self):
        for node in self.inorder():
            yield (node.item.key, node.item.value)

    def subtree_insert_recursive(self,subtree_node,key,value):
        if (subtree_node.left is None and subtree_node.right is None):
            new_item = BinarySearchTreeMap.Item(key,value)
            new = BinarySearchTreeMap.Node(new_item)
            if subtree_node.item.key > value:
                subtree_node.left = new
            else:
                subtree_node.right = new
        elif subtree_node.left is None:
            if subtree_node.item.key > key:
                new_item = BinarySearchTreeMap.Item(key, value)
                new = BinarySearchTreeMap.Node(new_item)
                subtree_node.left = new
            else:
                self.subtree_insert_recursive(subtree_node.right,key,value)
        elif subtree_node.right is None:
            if subtree_node.item.key < key:
                new_item = BinarySearchTreeMap.Item(key, value)
                new = BinarySearchTreeMap.Node(new_item)
                subtree_node.right = new
            else:
                self.subtree_insert_recursive(subtree_node.left, key, value)
        elif subtree_node.item.key == key:
            subtree_node.item.value = value
        else:
            if subtree_node.item.key > key:
                self.subtree_insert_recursive(subtree_node.left,key,value)
            else:
                self.subtree_insert_recursive(subtree_node.right,key,value)

    def insert(self,key,value):
        if self.is_empty():
            new_item = BinarySearchTreeMap.Item(key, value)
            new = BinarySearchTreeMap.Node(new_item)
            self.root = new
            self.size += 1
        else:
            self.subtree_insert_recursive(self.root,key,value)

def is_bst(tree):
    if tree.is_empty():
        raise Exception("Nope. Tree empty")
    else:
        return sub_is_bst(tree.root)[0]

def sub_is_bst(subtree_node):
    if subtree_node.left is None and subtree_node.left is None:
        return (True, subtree_node.item.key, subtree_node.item.key)
    elif subtree_node.right is None:
        left = sub_is_bst(subtree_node.left)
        if left[1] > subtree_node.item.key:
            return (False,subtree_node.item.key,left[2])
        else:
            return (True,left[1],left[2])
    elif subtree_node.left is None:
        right = sub_is_bst(subtree_node.right)
        if right[2] < subtree_node.item.key:
            return (True,right[1],right[2])
        else:
            return (False,subtree_node.item.key,right[2])
    else:
        left = sub_is_bst(subtree_node.left)
        right = sub_is_bst(subtree_node.right)
        if left[1] >= right[2] or right[2] <= left[1]:
            return (False,min(left[1],right[1],max(left[2],right[2])))
        return (True,min(left[1],right[1],max(left[2],right[2])))

def fca_bst(bst,node_a,node_b):
    curr = bst.root
    while curr is not None:
        if curr.item.key <= node_a.item.key and curr.item.key <= node_b.item.key:
            curr=curr.left
        elif curr.item.key >= node_a.item.key and curr.item.key >= node_b.item.key:
            curr=curr.right
        else:
            break
        return curr.item.key

s = BinarySearchTreeMap()
s.insert(5,1)
s.insert(1,2)
s.insert(0,3)
s.insert(4,5)
s.insert(31,4)

s.insert(30,300)
for i in s:
    print(i)

print(is_bst(s))

print(fca_bst(s,s.root.left.left,s.root.right.right))