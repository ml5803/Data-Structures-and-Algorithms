import LinkedBinaryTree

l_ch1=LinkedBinaryTree.LinkedBinaryTree.Node(3)
r_ch1=LinkedBinaryTree.LinkedBinaryTree.Node(4)
l_ch2=LinkedBinaryTree.LinkedBinaryTree.Node('+',l_ch1,r_ch1)
r_ch2=LinkedBinaryTree.LinkedBinaryTree.Node(2)
root=LinkedBinaryTree.LinkedBinaryTree.Node('*',l_ch2,r_ch2)
tree = LinkedBinaryTree.LinkedBinaryTree(root)

def eval_exp_tree(tree):
    return eval_exp_subtree(tree.root)

def eval_exp_subtree(subtree_node):
    if subtree_node.left is None and subtree_node.right is None:
        return subtree_node.data
    else:
        left = eval_exp_subtree(subtree_node.left)
        right = eval_exp_subtree(subtree_node.right)
        if subtree_node.data == "+":
            return left + right
        elif subtree_node.data == "-":
            return left - right
        elif subtree_node.data == "*":
            return left * right
        elif subtree_node.data == "/":
            return left / right
        else:
            raise Exception("Unsupported operation: " + str("op"))

print(eval_exp_tree(tree))

