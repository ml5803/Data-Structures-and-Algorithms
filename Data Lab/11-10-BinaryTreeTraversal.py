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
        nodes_q = ArrayQueue()
        nodes_q.enqueue(self.root)
        while(nodes_q.is_empty() == False):
            curr = nodes_q.dequeue()
            yield curr
            if curr.left is not None:
                nodes_q.enqueue(curr.left)
            if curr.right is not None:
                nodes_q.enqueue(curr.right)

    def tree_child_dist(self):
        return self.subtree_child_dist(self.root)

    def subtree_child_dist(self, curr_root):
        if curr_root.left is None and curr_root.right is None:
            return [1, 0, 0]
        else:
            if curr_root.right is None:
                # has 1 child
                lst = self.subtree_child_dist(curr_root.left)
                lst[1] += 1
                return lst
            elif curr_root.left is None:
                lst = self.subtree_child_dist(curr_root.right)
                lst[1] += 1
                return lst
            else:
                left = self.subtree_child_dist(curr_root.left)
                right = self.subtree_child_dist(curr_root.right)
                lst = [0] * 3
                lst[0] = left[0] + right[0]
                lst[1] = left[1] + right[1]
                lst[2] = left[2] + right[2] + 1
                return lst

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

class ArrayBoostQueue:
    def __init__(self):
        self.dll  = DoublyLinkedList()

    def __len__(self):
        return len(self.dll)

    def is_empty(self):
        return len(self.dll) == 0

    def enqueue(self,elem):
        self.dll.add_last(elem)

    def dequeue(self):
        return self.dll.delete(self.dll.first_node())

    def first(self):
        return self.dll.first_node()

    def boost(self,k):
        if k >= len(self.dll):
            self.dll.add_first(self.dll.delete(self.dll.last_node()))
        else:
            node = DoublyLinkedList.Node(k)
            curr = self.dll.last_node()
            for i in range(k):
                curr = curr.prev
            #curr is the item you are adding in front of.
            pre = curr.prev
            node.prev = pre
            pre.next = node
            node.next = curr
            curr.prev = node

def recreate_tree(preorder,inorder):
    pass

def sub_recreate_tree(sub_preorder,sub_inorder):
    if len(sub_preorder) == 1 and len(sub_inorder) == 1:
        return LinkedBinaryTree.Node(sub_preorder[0])
    else:
        pass

def words_keep_numbers_flip(lst):
    stack = ArrayStack()
    last = len(lst) - 1
    point = 0
    while point < len(lst):
        if isinstance(lst[point],int):
            stack.push(lst[point])
            lst[point], lst[last] = lst[last],lst[point]
            lst.pop()
            point-=1
            last-= 1
        point+=1
    while not stack.is_empty():
        lst.append(stack.pop())
    print(lst)

# print(words_keep_numbers_flip(["Keep",3,"this","order",2,1]))

a = LinkedBinaryTree.Node(1)
b = LinkedBinaryTree.Node(2)
c = LinkedBinaryTree.Node(3,a,b)
d = LinkedBinaryTree.Node(4,c)
tree = LinkedBinaryTree(d)
print(tree.tree_child_dist())

boost = ArrayBoostQueue()
boost.enqueue(1)
boost.enqueue(2)
boost.enqueue(3)
boost.enqueue(4)
boost.boost(2)
print(boost.dll.last_node().data)
print(boost.dequeue())
print(boost.dequeue())
print(boost.dequeue())
print(boost.dequeue())
