is_binary_tree = True
def isBinaryTree(root, retval):
    if retval is True:

    if root.left is not None:
        if root.data > root.left.data:
            isBinaryTree(root.left, True):
        else:
            is_binary_tree = False

    if root.right is not None:
        if root.data < root.right.data:
            isBinaryTree(root.right)
        else:
            is_binary_tree = False


def checkBST(root):
    isBinaryTree(root, True)
    return is_binary_tree