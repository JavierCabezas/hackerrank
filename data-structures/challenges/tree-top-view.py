"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)"""

nodes_per_position = {}

def topView(root):
    get_heights_and_positions(root)
    for pos_x, nodes in nodes_per_position.items():
        for node in nodes:
            max_h = -1
            if node[1] > max_h:
                node_to_print = node[0]
        print(node_to_print),


def get_heights_and_positions(root, pos_x = 0):
    global nodes_per_position
    hleft = hright = 0
    if root.left is not None:
        hleft = 1 + get_heights_and_positions(root.left, pos_x-1)
    if root.right is not None:
        hright = 1 + get_heights_and_positions(root.right, pos_x+1)

    hnode = max(hleft, hright)
    if not pos_x in nodes_per_position:
        nodes_per_position[pos_x] = []
    nodes_per_position[pos_x].append((root.data, hnode))

    return hnode
