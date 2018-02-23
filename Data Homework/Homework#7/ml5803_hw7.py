class ArrayQueue:
    INIT_CAPACITY = 10

    def __init__(self):
        self.data = [None] * ArrayQueue.INIT_CAPACITY
        self.front_ind = 0
        self.num_of_elems = 0

    def __len__(self):
        return self.num_of_elems

    def is_empty(self):
        return len(self) == 0

    def enqueue(self,elem):
        if(self.num_of_elems == len(self.data)):
            self.resize(2*self.data)
        back_ind = (self.front_ind + self.num_of_elems) % len(self.data)
        self.data[back_ind] = elem
        self.num_of_elems += 1

    def dequeue(self):
        if (self.is_empty()):
            raise EmptyCollection("Queue is empty")
        elem = self.data[self.front_ind]
        self.data[self.front_ind] = None
        self.front_ind += (self.front_ind + 1) % len(self.data)
        self.num_of_elems -= 1
        if (self.num_of_elems < len(self.data)//4):
            self.resize(len(self.data)//2)
        return elem

    def front(self):
        if (self.is_empty()):
            raise EmptyCollection("Queue is empty")
        return self.data[self.front_ind]

    def resize(self,new_capacity):
        old_data = self.data
        self.data = [None] * new_capacity
        old_ind = self.front_ind
        for new_ind in range(self.num_of_elems):
            self.data[new_ind] = old_data[old_ind]
            old_ind = (old_ind+1) % len(old_data)
        self.front_ind = 0

class EmptyCollection(Exception):
    pass

class EmptyTree(Exception):
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

    def __init__(self, root=None):
        self.root = root
        self.size = self.subtree_count(self.root)

    def __len__(self):
        return self.size

    def is_empty(self):
        return (len(self) == 0)

    def subtree_count(self, subtree_root):
        if(subtree_root is None):
            return 0
        else:
            left_count = self.subtree_count(subtree_root.left)
            right_count = self.subtree_count(subtree_root.right)
            return left_count + right_count + 1

    def sum_tree(self):
        return self.subtree_sum(self.root)

    def subtree_sum(self, subtree_root):
        if(subtree_root is None):
            return 0
        else:
            left_sum = self.subtree_sum(subtree_root.left)
            right_sum = self.subtree_sum(subtree_root.right)
            return left_sum + right_sum + subtree_root.data

    def height(self):
        if (self.is_empty()):
            raise EmptyCollection("Height is not defined for an empty tree")
        return self.subtree_height(self.root)

    #assuming subtree_root is not empty
    def subtree_height(self, subtree_root):
        if((subtree_root.left is None) and (subtree_root.right is None)):
            return 0
        elif(subtree_root.left is None):
            return 1 + self.subtree_height(subtree_root.right)
        elif(subtree_root.right is None):
            return 1 + self.subtree_height(subtree_root.left)
        else:
            left_height = self.subtree_height(subtree_root.left)
            right_height = self.subtree_height(subtree_root.right)
            return 1 + max(left_height, right_height)


    def preorder(self):
        yield from self.subtree_preorder(self.root)

    def subtree_preorder(self, subtree_root):
        if(subtree_root is None):
            return
        else:
            yield subtree_root
            yield from self.subtree_preorder(subtree_root.left)
            yield from self.subtree_preorder(subtree_root.right)


    def postorder(self):
        yield from self.subtree_postorder(self.root)

    def subtree_postorder(self, subtree_root):
        if(subtree_root is None):
            return
        else:
            yield from self.subtree_postorder(subtree_root.left)
            yield from self.subtree_postorder(subtree_root.right)
            yield subtree_root


    def inorder(self):
        yield from self.subtree_inorder(self.root)

    def subtree_inorder(self, subtree_root):
        if(subtree_root is None):
            return
        else:
            yield from self.subtree_inorder(subtree_root.left)
            yield subtree_root
            yield from self.subtree_inorder(subtree_root.right)


    def __iter__(self):
        for node in self.inorder():
            yield node.data


    def breadth_first(self):
        if(self.is_empty()):
            return
        nodes_q = ArrayQueue()
        nodes_q.enqueue(self.root)
        while(nodes_q.is_empty() == False):
            curr_node = nodes_q.dequeue()
            yield curr_node
            if (curr_node.left is not None):
                nodes_q.enqueue(curr_node.left)
            if (curr_node.right is not None):
                nodes_q.enqueue(curr_node.right)

    def leaves_list(self):
        if self.root is None:
            return []
        new_lst = []
        return self.sub_leaves_list(self.root,new_lst)

    def sub_leaves_list(self,subtree_node,lst):
        if subtree_node.left is None and subtree_node.right is None:
            lst.append(subtree_node.data)
            return lst
        else:
            if subtree_node.left is not None:
                lst = self.sub_leaves_list(subtree_node.left,lst)
            if subtree_node.right is not None:
                lst = self.sub_leaves_list(subtree_node.right, lst)
            return lst

    def iterative_inorder(self):
        curr = self.root
        while curr is not None:
            if curr.left is None:
                yield curr.data
                curr = curr.right
            else:
                pre = curr.left
                while pre.right is not None and pre.right is not curr:
                    pre = pre.right
                if pre.right is None:
                    pre.right = curr
                    curr = curr.left
                else:
                    pre.right=None
                    yield curr.data
                    curr = curr.right

def min_and_max(bin_tree):
    if bin_tree.root is None:
        raise EmptyTree("Tree is empty")
    return subtree_min_and_max(bin_tree,bin_tree.root)

def subtree_min_and_max(bin_tree,subtree_root):
    if subtree_root.left is None and subtree_root.right is None:
        return (subtree_root.data,subtree_root.data)
    else:
        if(not subtree_root.left is None and not subtree_root.right is None):
            curr_left = subtree_min_and_max(bin_tree,subtree_root.left)
            curr_right = subtree_min_and_max(bin_tree,subtree_root.right)
            temp_min = min(curr_left[0],curr_right[0],subtree_root.data)
            temp_max = max(curr_left[1],curr_right[1],subtree_root.data)
            return (temp_min, temp_max)
        elif subtree_root.right is None:
            curr_left = subtree_min_and_max(bin_tree, subtree_root.left)
            temp_min = min(curr_left[0], subtree_root.data)
            temp_max = max(curr_left[1], subtree_root.data)
            return (temp_min, temp_max)
        else:
            curr_right = subtree_min_and_max(bin_tree, subtree_root.right)
            temp_min = min(curr_right[0], subtree_root.data)
            temp_max = max(curr_right[1], subtree_root.data)
            return (temp_min, temp_max)

def is_height_balanced(bin_tree):
    if bin_tree.root is None:
        raise EmptyTree("Tree is empty")
    return sub_is_height_balanced(bin_tree.root)[1]

def sub_is_height_balanced(subtree_node):
    if subtree_node is None:
        return (0, True)
    else:
        left = sub_is_height_balanced(subtree_node.left)
        right = sub_is_height_balanced(subtree_node.right)
        return (max(left[0],right[0])+1,left[1] and right[1] and abs(left[0]-right[0])<= 1)

def create_expression_tree(prefix_exp_str):
    exp_lst = prefix_exp_str.split(" ")
    for i in range(len(exp_lst)):
        if exp_lst[i] not in ["*","/","+","-"]:
            exp_lst[i] = int(exp_lst[i])
    root = create_expression_tree_helper(exp_lst,0)
    tree = LinkedBinaryTree(root[0])
    return tree

def create_expression_tree_helper(lst, start):
    #continue here
    if isinstance(lst[start],int):
        return (LinkedBinaryTree.Node(lst[start]),1)
    else:
        left = create_expression_tree_helper(lst,start+1)
        right = create_expression_tree_helper(lst,start+left[1]+1)
        p_node = LinkedBinaryTree.Node(lst[start],left[0],right[0])
        height = left[1] + right[1] + 1
        return (p_node,height)

def prefix_to_postfix(exp):
    exp_tree = create_expression_tree(exp)
    format = sub_prefix_to_postfix(exp_tree.root)
    return format[:-1]

def sub_prefix_to_postfix(subtree_root):
    if (subtree_root is None):
        return ""
    else:
        string = sub_prefix_to_postfix(subtree_root.left) + sub_prefix_to_postfix(subtree_root.right) + str(subtree_root.data) + " "
        return string

#need to do q5 - exp tree

# a = LinkedBinaryTree.Node(1)
# b = LinkedBinaryTree.Node(2)
# c = LinkedBinaryTree.Node(3,a,b)
# d = LinkedBinaryTree.Node(4,c)
# not_balanced_tree = LinkedBinaryTree(d)
# print(is_height_balanced(not_balanced_tree))
#
# e = LinkedBinaryTree.Node(1)
# f = LinkedBinaryTree.Node(2)
# g = LinkedBinaryTree.Node(3,e,f)
# balanced_tree = LinkedBinaryTree(g)
# print(is_height_balanced(balanced_tree))
#
# exp_tree = create_expression_tree("* 2 + - 15 6 4")
# for i in exp_tree:
#     print(i)
#
# print(prefix_to_postfix("* 2 + - 15 6 4"))