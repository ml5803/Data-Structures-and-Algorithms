class EmptyCollection(Exception):
    pass

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
            self.childCount = 0

        def num_children(self):
            count = 0
            if (self.left is not None):
                count += 1
            if (self.right is not None):
                count += 1
            return count

        def set_child_count(self,num):
            self.childCount = num

        def disconnect(self):
            self.item = None
            self.parent = None
            self.left = None
            self.right = None
            self.childCount = 0


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
            parent.childCount+=1
            if(key < self.root.item.key):
                curr = self.root.left
            else:
                curr = self.root.right
            while (curr is not None):
                parent = curr
                if (key < curr.item.key):
                    curr = curr.left
                    if curr is not None:
                        curr.childCount+=1
                else:
                    curr = curr.right
                    if curr is not None:
                        curr.childCount+=1
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
                self.subtree_decrease_parent_childCounts(max_of_left)
                node_to_delete.item = max_of_left.item
                self.subtree_delete(node_to_delete.left, max_of_left.item.key)
        else:
            if (num_children == 0):
                parent = node_to_delete.parent
                if (node_to_delete is parent.left):
                    parent.left = None
                else:
                    parent.right = None
                self.subtree_decrease_parent_childCounts(node_to_delete)
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
                self.subtree_decrease_parent_childCounts(node_to_delete)
                node_to_delete.disconnect()
                self.size -= 1
            else: #num_children == 2
                max_of_left = self.subtree_max(node_to_delete.left)
                self.subtree_decrease_parent_childCounts(max_of_left)
                node_to_delete.item = max_of_left.item
                self.subtree_delete(node_to_delete.left, max_of_left.item.key)

        return value

    def subtree_decrease_parent_childCounts(self,curr_root):
        parent = curr_root.parent
        while curr_root is not None:
            curr_root.childCount -= 1
            curr_root = parent

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

    def preorder(self):
        yield from self.subtree_preorder(self.root)

    def subtree_preorder(self, subtree_root):
        if subtree_root is None:
            return
        else:
            yield subtree_root
            yield from self.subtree_preorder(subtree_root.left)
            yield from self.subtree_preorder(subtree_root.right)

    def __iter__(self):
        for node in self.inorder():
            yield (node.item.key, node.item.value)

    def get_ith_smallest(self, i):
        if len(self) == 0:
            raise Exception("Tree is empty")
        elif i > len(self):
            raise Exception("Invalid value")
        else:
            if len(self) == 1:
                return self.root.item.key
            else:
                curr = self.root
                while (i!=0):
                        if(curr.left.childCount+1 >= i):
                            curr=curr.left
                        else:
                            i = i - curr.left.childCount+2
                            curr = curr.right
        return curr.item.key


def create_chain_bst(n):
    tree = BinarySearchTreeMap()
    if n == 0:
        return tree
    else:
        for i in range(n):
            tree.subtree_insert(i+1,None)
    # for i in tree.inorder():
    #     print(i.item.key)
    return tree

def create_complete_bst(n):
   bst = BinarySearchTreeMap()
   add_items(bst,1,n)
   return bst

def add_items(tree, low, high):
    if low == high:
        tree.subtree_insert(low, None)
    else:
        mid = (low+high)/2
        tree.subtree_insert(mid, None)
        add_items(tree, low, mid - 1)
        add_items(tree, mid + 1, high)

def restore_bst(prefix_lst):
    if len(prefix_lst) == 0:
        return BinarySearchTreeMap()
    stack = ArrayStack()
    tree = BinarySearchTreeMap()
    root_entry = BinarySearchTreeMap.Item(prefix_lst[0],None)
    root = BinarySearchTreeMap.Node(root_entry)
    stack.push(root)
    tree.root = root
    for i in range(1,len(prefix_lst)):
        temp = None
        while not stack.is_empty() and prefix_lst[i] > stack.top().item.key:
            temp = stack.pop()
        if temp != None:
            entry = BinarySearchTreeMap.Item(prefix_lst[i],None)
            node = BinarySearchTreeMap.Node(entry)
            temp.right = node
            stack.push(node)
        else:
            entry = BinarySearchTreeMap.Item(prefix_lst[i],None)
            node = BinarySearchTreeMap.Node(entry)
            stack.top().left = node
            stack.push(node)
    return tree

def find_min_abs_difference(bst):
    sort = [x.item.key for x in bst.inorder()]
    min = sort[1]-sort[0]
    for i in range(1,len(sort)):
        if sort[i] - sort[i-1] < min:
            min = sort[i] - sort[i-1]
    return min



