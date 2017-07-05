"""
 Insert Node at the end of a linked list
 head pointer input could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method
"""


def Insert(head, data):
    if head is None:
        return Node(data, None) #If we get an empty list we just return the element
    else:
        remember_my_head = head
        while head.next is not None:
            head = head.next
        head.next = Node(data, None)
    return remember_my_head