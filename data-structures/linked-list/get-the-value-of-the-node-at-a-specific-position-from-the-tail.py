# Body
"""
 Get Node data of the Nth Node from the end.
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the node data of the linked list in the below method.
"""

def GetListLen(head):
    len = 0
    while head is not None:
        len += 1
        head = head.next
    return len

def GetNode(head, position):
    len = GetListLen(head)

    for i in range(len-position-1):
        head = head.next
    return(head.data)
