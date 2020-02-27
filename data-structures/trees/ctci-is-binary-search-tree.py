class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def is_bst_recursive(root, min_val: int, max_val: int):
    if root is None:
        return True

    if root.data <= min_val or root.data >= max_val:
        return False

    is_left = is_bst_recursive(root.left, min_val, root.data)
    is_right = is_bst_recursive(root.right, root.data, max_val)

    return is_left and is_right


def checkBST(root):
    return is_bst_recursive(root, -10000, 10000)


root = Node(1, Node(2, Node(1), Node(3)), Node(6, Node(5), Node(7)))

checkBST(root)
