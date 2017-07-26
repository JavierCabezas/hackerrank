class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

root = Node(1, Node(2, Node(1), Node(3)),Node(6, Node(5), Node(7)))

MAX_VAL = 100000
MIN_VAL = -100000

def is_bst_recursive(root, min, max):
    if root is None:
        return True

    if root.data < min or root.data > max:
        return False

    return is_bst_recursive(root.left, min, root.data-1) and is_bst_recursive(root.right, root.data+1, max)

def checkBST(root):
    if is_bst_recursive(root, MIN_VAL, MAX_VAL):
        print('Yes')
    else:
        print('No')

checkBST(root)