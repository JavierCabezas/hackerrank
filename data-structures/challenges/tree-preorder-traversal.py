"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
#Python2 version
def preOrder(root):
    print str(root.data),
    if root.left is not None:
        preOrder(root.left)
    if root.right is not None:
        preOrder(root.right)