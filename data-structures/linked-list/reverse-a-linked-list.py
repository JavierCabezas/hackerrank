"""
 Reverse a linked list
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""
def Reverse(head):
    if head is None:
        return None

    if head.next is None:
        return head

    n = head
    n_minus_one =  None
    while n is not None:
        temp = n.next
        n.next = n_minus_one
        n_minus_one = n
        n = temp

    head = n_minus_one
    return head