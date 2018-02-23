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
print(x)
print(height)