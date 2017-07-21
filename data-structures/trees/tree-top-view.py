"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)"""

def topView(root):
    nodes = []
    nodes.append(root.data)

    current = root
    while current.left is not None:
        current = current.left
        nodes.append(current.data)

    while root.right is not None:
        root = root.right
        nodes.append(root.data)

    for i in sorted(nodes):
        print(i),