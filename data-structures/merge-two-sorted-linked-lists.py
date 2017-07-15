"""
 Merge two linked lists
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def shouldWeCotinueLooping(headA, headB):
    return headA is not None and headB is not None

def MergeLists(headA, headB):
    head = None
    first_node_selected = False
    should_we_continue = shouldWeCotinueLooping(headA, headB)

    if headA is None:
        return headB
    if headB is None:
        return headA

    while should_we_continue:
        if headA is None and headB is not None:
            node = Node(headB.data)
            should_we_continue = shouldWeCotinueLooping(headA, headB)
            headB = headB.next
        elif headB is None and headA is not None:
            node = Node(headA.data)
            should_we_continue = shouldWeCotinueLooping(headA, headB)
            headA = headA.next
        elif headA.data < headB.data:
            node = Node(headA.data)
            should_we_continue = shouldWeCotinueLooping(headA, headB)
            headA = headA.next
        else:
            node = Node(headB.data)
            should_we_continue = shouldWeCotinueLooping(headA, headB)
            headB = headB.next

        if first_node_selected is False:
            head = node
            first_node_selected = True
        else:
            last_node.next = node
        last_node = node


    return head