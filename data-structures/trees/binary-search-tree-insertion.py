class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

root = Node(4, None, None)
root.left = Node(2, None, None)
root.right = Node(7, None, None)
root.left.left = Node(1, None, None)
root.left.right = Node(3, None, None)


def insert(r, val):
    if r is None:
        r = Node(val)
    elif r.data >= val:
        if r.left is None:
            r.left = Node(val)
        else:
            insert(r.left, val)
    elif r.data < val:
        if r.right is None:
            r.right = Node(val)
        else:
            insert(r.right, val)

    return r