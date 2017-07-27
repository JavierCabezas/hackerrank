class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

root = Node('F', None, None)
root.left = Node('D', None, None)
root.right = Node('J', None, None)
root.left.left = Node('B', Node('A'), Node('C'))
root.left.right = Node('E')
root.right.left = Node('G', None, Node('I'))
root.right.right = Node('K')


def levelOrder(root):
    visited = []
    visited.append(root)

    while len(visited) > 0:
        aux = []
        for node in visited:
            print(node.data)
            if node.left is not None:
                aux.append(node.left)
            if node.right is not None:
                aux.append(node.right)
        visited = aux

levelOrder(root)