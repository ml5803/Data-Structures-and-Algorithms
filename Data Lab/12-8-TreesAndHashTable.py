import random
class UnsortedArrayMap:
    class Item:
        def __init__(self,key,value = None):
            self.key = key
            self.value = value

    def __init__(self):
        self.data = []

    def __setitem__(self, key, value):
        for item in self.data:
            if item.key == key:
                item.value = value
                return
        new_item = UnsortedArrayMap.Item(key,value)
        self.data.append(new_item)

    def __getitem__(self, key):
        for item in self.data:
            if item.key == key:
                return item.value
        raise KeyError("KeyError:" + str(key))

    def __delitem__(self, key):
        for ind in range(len(self.data)):
            if(self.data[ind].key == key):
                val = self.data[ind].value
                self.data.pop(ind)
                return val
        raise KeyError("KeyError:" + str(key))

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        for item in self.data:
            yield item.key


class ChainingHashTableMap:
    def __init__(self,N=64,p=40206835204840513073):
        self.N = N
        self.n = 0
        self.table  = [None] * self.N
        self.p = p
        self.a = random.randint(1,self.p-1)
        self.b = random.randint(0,self.p-1)

    def __getitem__(self,key):
        j = self.hash_func(key)
        curr_bucket = self.table[j]
        if(curr_bucket is None):
            raise KeyError("Key Error: " + str(key))
        return curr_bucket[key]

    def __setitem__(self, key, value):
        j = self.hash_func(key)
        if self.table[j] is None:
            self.table[j] = UnsortedArrayMap()
        old_size = len(self.table[j])
        self.table[j][key] = value
        new_size = len(self.table[j])
        if new_size > old_size:
            self.n += 1
        if self.n > self.N:
            self.rehash(2*self.N)

    def __delitem__(self, key):
        j = self.hash_func(key)
        curr_bucket = self.table[j]
        if curr_bucket is None:
            raise KeyError("Key Error:" + str(key))
        del curr_bucket[key]
        self.n -= 1
        if (len(curr_bucket) == 0):
            self.table[j] = None
        if(self.n < self.N // 4):
            self.rehash(self.N//2)

    def hash_func(self,key):
        return ((self.a * hash(key)) + self.b) % self.p % self.N

    def rehash(self,new_size):
        old_data = []
        for key in self:
            val = self[key]
            p = (key,val)
            old_data.append(p)

        self.N = new_size
        self.n = 0
        self.table = [None] * self.N
        #this could be where you change self.a, self.b if you wish
        for (key,val) in old_data:
            self[key] = val

    def __iter__(self):
        for curr_bucket in self.table:
            if (curr_bucket is not None):
                for key in curr_bucket:
                    yield key

    def __len__(self):
        return self.n

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

def compare_tree(tree1,tree2):
    list1 = [x for x in tree1.inorder()]
    list2 = [x for x in tree2.inorder()]

    if len(list1) != len(list2):
        return False

    for i in range(len(list1)):
        if(list1[i] != list2[i]):
            return False

    return True

def most_frequent_a(lst):
    temp = sorted(lst)
    max_run = 0
    freq_item = lst[0]
    curr_run = 0
    curr_item = lst[0]
    for elem in temp:
        if elem == curr_item:
            curr_run += 1
        else:
            if curr_run > max_run:
                max_run = curr_run
                freq_item = curr_item
            curr_run = 1
            curr_item = elem

    if curr_run > max_run:
        max_run = curr_run
        freq_item = curr_item

    return freq_item

def most_frequent_b(lst):
    map = ChainingHashTableMap()
    for elem in lst:
        val = map.hash_func(elem)
        if map.table[val] is None:
            map[elem] = 0
        else:
            map[elem] = map[elem] + 1



def greatnum(tree,val):
    curr = tree.root
    if curr.item.data > val and curr.right is not None:
        curr=curr.right
    pass
    return -1

def rob(root):
    return robDFS(root)[1]

def robDFS(node):
    if node is None:
        return (0,0)
    L = robDFS(node.left)
    R = robDFS(node.right)
    return (L[1],R[1],max(R[1]+L[1],R[0]+L[0]+node.val))

print(most_frequent_a([1,2,3,3,1,2,3,2,2,2]))
print(most_frequent_b([1,2,3,3,1,2,3,2,2,2]))