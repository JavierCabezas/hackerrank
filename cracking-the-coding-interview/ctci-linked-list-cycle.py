#In this approach I take advantage that on the constraits its defined that the list it, at most, 100 items  long.
def next_node_none(node):
    return node.next is None

def advance_node(node):
    return node.next

def has_cycle(head):
    if head is None:
        return False

    node = head
    for i in range(101):
        if next_node_none(node):
            return False
        else:
            node = advance_node(node)

    return True



