import ArrayQueue

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

