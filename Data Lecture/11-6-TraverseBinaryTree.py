'''
    Notes
'''

'''
                  5
            2           3
        1       6   4       7
    ---TRAVERSAL SEQUENCES OF A BINARY TREE:
        1. PREORDER (DLR) 
            5 3 1 6 3 4 7
        2. INORDER (LDR)
            1 2 6 5 4 3 7
        3. POSTORDER (LRD)
            1 6 2 4 7 3 5
        4. BREATH-FIRST: level by level, each from left to right
            5 2 3 1 6 4 7
'''
import LinkedBinaryTree

l_ch1=LinkedBinaryTree.LinkedBinaryTree.Node(1)
r_ch1=LinkedBinaryTree.LinkedBinaryTree.Node(3)
l_ch2=LinkedBinaryTree.LinkedBinaryTree.Node(2,l_ch1,r_ch1)
l_ch3=LinkedBinaryTree.LinkedBinaryTree.Node(5)
r_ch2=LinkedBinaryTree.LinkedBinaryTree.Node(6,l_ch3)
root=LinkedBinaryTree.LinkedBinaryTree.Node(4,l_ch2,r_ch2)

tree = LinkedBinaryTree.LinkedBinaryTree(root)
x = tree.sum_of_a_tree()
height = tree.height()
# print(x)
# print(height)

for elem in tree:
    print(elem)

def seq1():
    yield 1
    yield 2
    yield from seq2()

def seq2():
    yield 3
    yield 4
