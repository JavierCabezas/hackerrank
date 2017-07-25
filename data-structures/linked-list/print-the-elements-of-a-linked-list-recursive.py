class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

head = Node(1, Node(4, Node(8, Node(16, Node(32)))))

def print_list(head):
    print(head.data)
    if(head.next is not None):
        print_list(head.next)


print_list(head)