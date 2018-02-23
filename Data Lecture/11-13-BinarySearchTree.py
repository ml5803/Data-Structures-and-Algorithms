'''
    Binary Search Tree
'''

'''
    Definition: 
    Let T be a binary tree.
    We say that T is a Binary Search Tree, if for each node in T:
    1. All keys stored in the left subtree of n are less than the key stored in n
    2. All keys stored in the right subtree of n are greater than the key stored in n
'''

class BinarySearchTreeMap:
    class Item:
        def __init__(self, key, value=None):
            self.key = key
            self.value = value

    class Node:
        def __init__(self,item):
            self.item = item
            self.left = None
            self.right = None
            self.parent = None

        def disconnect(self):
            self.item = None
            self.left = None
            self.right = None
            self.parent = None

        def number_of_children(self):
            count = 0
            if self.left is not None:
                count += 1
            if self.right is not None:
                count +=1

    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0

    #return the value associated to key or raise a KeyError if key is not present
    def __getitem__(self, key):
        node = self.subtree_find(self.root,key)
        if node is None:
            raise KeyError("KeyError: " + str(key))
        else:
            return node.item.value


    #return the node containing key or None if key is not present
    def subtree_find(self,subtree_root,key):
        cursor = subtree_root
        while cursor is not None:
            if cursor.item.key == key:
                return cursor
            elif cursor.item.key > key:
                cursor = cursor.left
            else: #cursor.item.key < key
                cursor = cursor.right
        return None

    #updates the value if key is already in the tree
    def __setitem__(self, key, value):
        node = self.subtree_find(self.root,key)
        if(node is not None):
            node.item.value = value
        else:
            self.subtree_insert(key,value)

    #assumes key is not in the tree
    def subtree_insert(self,key,value):
        new_item =BinarySearchTreeMap.Item(key,value)
        new_node = BinarySearchTreeMap.Node(new_item)

        if self.is_empty():
            self.root = new_node
            self.size = 1
        else:
            parent = self.root
            if self.root.item.key > key:
                cursor = self.root.left
            else:
                cursor = self.root.right

            while(cursor is not None):
                parent = cursor
                if cursor.item.key > key:
                    cursor = cursor.left
                else:
                    cursor = cursor.right

            new_node.parent = parent
            if parent.item.key > key:
                parent.left = new_node
            else:
                parent.right = new_node
            self.size +=1

    #raises an exception if key is not in the tree
    def __delitem__(self,key):
        node = self.subtree_find(key)
        if node is None:
            raise KeyError("KeyError: " + key)
        else:
            self.subtree_delete(self.root,key)

    #assumes that the key is in the tree and returns the value associated with key
    def subtree_delete(self,subtree_root,key):
        node_to_delete = self.subtree_find(subtree_root,key)
        value = node_to_delete.item.value
        number_children = node_to_delete.number_of_children()

        if node_to_delete is self.root:
            if number_children == 0:
                self.root = None
                self.size = 0
                node_to_delete.disconnect()
            elif number_children ==1:
                if self.root.left is not None:
                    self.root = self.root.left
                else:
                    self.root = self.root.right
                self.root.parent = None
                self.size -= 1
                node_to_delete.disconnect()
            else:  # number_children == 2
                max_of_left = self.subtree_max(node_to_delete.left)
                node_to_delete.item = max_of_left.item
                self.subtree_delete(node_to_delete.left, max_of_left.item.key)

        else:
            if number_children == 0:
                parent = node_to_delete.parent
                if node_to_delete is parent.left:
                    parent.left = None
                else:
                    parent.right = None
                node_to_delete.disconnect()
                self.size-=1
            elif number_children == 1:
                parent = node_to_delete.parent
                if node_to_delete.right is None:
                    child = node_to_delete.left
                else:
                    child = node_to_delete.right

                child.parent = parent
                if node_to_delete is parent.left:
                    parent.left = child
                else:
                    parent.right = child
            else: #number_children == 2
                max_of_left = self.subtree_max(node_to_delete.left)
                node_to_delete.item = max_of_left.item
                self.subtree_delete(node_to_delete.left,max_of_left.item.key)

        return value

    def subtree_max(self,subtree_root):
        curr = subtree_root
        while curr.right is not None:
            curr = curr.right
        return curr

    def __iter__(self):
        for node in self.inorder():
            yield node.item.key

    def inorder(self):
        yield from self.subtree_inorder(self.root)

    def subtree_inorder(self,subtree_root):
        if subtree_root is None:
            return
        else:
            yield from self.subtree_inorder(subtree_root.left)
            yield subtree_root
            yield from self.subtree_inorder(subtree_root.right)
'''
    CLAIM: Let T be a binary tree. We have:
    T is a binary-search tree <-> The inorder sequence of T is sorted in an ascending order
'''