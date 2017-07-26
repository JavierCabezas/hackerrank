class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

head = Node(1, Node(4, Node(8, Node(16, Node(32)))))

def ReversePrint(head):
    if head is not None:
        ReversePrint(head.next)
        print(head.data)

ReversePrint(head)

