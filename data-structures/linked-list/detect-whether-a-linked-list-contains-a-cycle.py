"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as:

    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""
def has_cycle(head):
    if head is None:
        return False

    if head.next is None:
        return False

    fast = head.next
    slow = head
    while fast.next is not None:
        if fast.next.next is None:
            return False
        if fast == slow:
            return True

        fast = fast.next.next
        slow = slow.next

    return False