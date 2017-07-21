def Delete(head, position):
    if head is None:
        return None

    if position == 0:
        return head.next

    jump_node = head
    for i in range(position-1):
        if jump_node.next is not None:
            jump_node = jump_node.next

    jump_node.next = jump_node.next.next

    return head
